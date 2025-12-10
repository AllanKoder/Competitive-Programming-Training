#include <bits/stdc++.h>

using ull = unsigned long long;

struct Pos
{
    ull x;
    ull y;

    std::vector<Pos> points_between(const Pos &other) const
    {
        std::vector<Pos> out;

        long dx = (other.x > x) - (other.x < x); // +1, 0, or -1
        long dy = (other.y > y) - (other.y < y); // +1, 0, or -1

        // Only 1-direction movement allowed
        if (dx != 0 && dy != 0)
            return out;

        ull cx = x;
        ull cy = y;

        while (cx != other.x || cy != other.y)
        {
            cx += dx;
            cy += dy;
            out.push_back({cx, cy});
        }

        return out;
    }

    friend std::ostream &operator<<(std::ostream &os, const Pos &p)
    {
        os << "(" << p.x << "," << p.y << ")";
        return os;
    }
};

struct Edge
{
    Pos from;
    Pos to;

    friend std::ostream &operator<<(std::ostream &os, const Edge &e)
    {
        os << e.from << "," << e.to;
        return os;
    }
};

std::vector<Edge> vectors_to_edges(const std::vector<Pos> &coords)
{
    std::vector<Edge> output;
    output.reserve(coords.size());

    for (int i = 0; i < coords.size(); i++)
    {
        int next_coord_i = (i + 1) % coords.size();
        output.push_back({coords[i], coords[next_coord_i]});
    }

    return output;
}

// Yes, this function was assisted with help
bool rectangle_intersects_an_edge(
    Pos p1, Pos p2,
    const std::vector<Edge> &edges)
{
    ull left = std::min(p1.x, p2.x);
    ull right = std::max(p1.x, p2.x);
    ull bottom = std::min(p1.y, p2.y);
    ull top = std::max(p1.y, p2.y);

    for (const auto &e : edges)
    {
        Pos a = e.from;
        Pos b = e.to;

        // Check if either endpoint is inside the rectangle interior
        auto inside = [&](const Pos &p)
        {
            return (p.x >= left && p.x <= right &&
                    p.y >= bottom && p.y <= top);
        };

        bool a_inside = inside(a);
        bool b_inside = inside(b);

        // Case 1: One endpoint inside, one outside → intersects
        if (a_inside != b_inside)
            return true;

        // Case 2: Both inside → no boundary intersection
        if (a_inside && b_inside)
            continue;

        // Case 3: Both endpoints outside, check intersection with rectangle borders

        // Horizontal edge: y = a.y, x from a.x to b.x
        if (a.y == b.y)
        {
            ull y = a.y;
            if (y < bottom || y > top)
                continue; // no possible intersection vertically

            ull x1 = std::min(a.x, b.x);
            ull x2 = std::max(a.x, b.x);

            // Check if the projected x-range overlaps the rectangle horizontally
            if (x2 >= left && x1 <= right)
                return true;
        }
        else // Vertical edge: x = a.x, y from a.y to b.y
        {
            ull x = a.x;
            if (x < left || x > right)
                continue; // no possible intersection horizontally

            ull y1 = std::min(a.y, b.y);
            ull y2 = std::max(a.y, b.y);

            // Check if projected y-range overlaps vertically
            if (y2 >= bottom && y1 <= top)
                return true;
        }
    }

    return false;
}

ull largest_rectangle(
    const std::vector<Pos> &coords,
    const std::vector<Edge> &edges)
{
    ull best_area = 0;

    for (int i = 0; i < coords.size(); i++)
    {
        Pos pos1 = coords[i];
        for (int j = i + 1; j < coords.size(); j++)
        {
            Pos pos2 = coords[j];

            ull highest_x = std::max(pos1.x, pos2.x);
            ull lowest_x = std::min(pos1.x, pos2.x);
            ull highest_y = std::max(pos1.y, pos2.y);
            ull lowest_y = std::min(pos1.y, pos2.y);

            ull candidate_area =
                (highest_x - lowest_x + 1) *
                (highest_y - lowest_y + 1);

            // Only check interior of the rectangle
            Pos adjusted_p1{lowest_x + 1, lowest_y + 1};
            Pos adjusted_p2{highest_x - 1, highest_y - 1};

            if (rectangle_intersects_an_edge(adjusted_p1, adjusted_p2, edges))
                continue;

            best_area = std::max(best_area, candidate_area);
            // std::cout << "Best: " << best_area << ", " << pos1 << " " << pos2 << "\n";
        }
    }

    return best_area;
}

// --- Parse input ---
std::vector<Pos> raw_string_to_coords(const std::vector<std::string> &raw_inputs)
{
    std::vector<Pos> coords;

    for (auto s : raw_inputs)
    {
        std::stringstream ss(s);
        Pos c;

        std::string string_digit;
        getline(ss, string_digit, ',');
        c.x = std::stoull(string_digit);

        getline(ss, string_digit, ',');
        c.y = std::stoull(string_digit);

        coords.push_back(c);
    }

    return coords;
}

int main()
{
    std::vector<std::string> raw_inputs;
    std::string s;
    while (std::getline(std::cin, s))
    {
        raw_inputs.push_back(s);
    }

    std::vector<Pos> coords = raw_string_to_coords(raw_inputs);
    std::vector<Edge> edges = vectors_to_edges(coords);
    ull area = largest_rectangle(coords, edges);

    std::cout << "Answer: " << area << "\n";
}
