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

// --- PrefixSum2D ---
class PrefixSum2D
{
private:
    std::vector<std::vector<ull>> prefix;

    ull sum_range(Pos bottom_right) const
    {
        ull x = bottom_right.x;
        ull y = bottom_right.y;

        if (x >= prefix[0].size() || y >= prefix.size())
            return 0;

        return prefix[y][x];
    }

public:
    PrefixSum2D(const std::vector<std::vector<char>> &grid)
    {
        size_t H = grid.size();
        size_t W = H ? grid[0].size() : 0;
        prefix.assign(H, std::vector<ull>(W, 0));

        for (size_t y = 0; y < H; ++y)
        {
            for (size_t x = 0; x < W; ++x)
            {
                ull val = (grid[y][x] == '#') ? 1ULL : 0ULL;

                ull up = (y > 0) ? prefix[y - 1][x] : 0;
                ull left = (x > 0) ? prefix[y][x - 1] : 0;
                ull diag = (x > 0 && y > 0) ? prefix[y - 1][x - 1] : 0;

                prefix[y][x] = val + up + left - diag;
            }
        }
    }

    ull sum_range(Pos pos1, Pos pos2) const
    {
        ull x1 = std::min(pos1.x, pos2.x);
        ull y1 = std::min(pos1.y, pos2.y);
        ull x2 = std::max(pos1.x, pos2.x);
        ull y2 = std::max(pos1.y, pos2.y);

        ull total = sum_range({x2, y2});
        ull up = (y1 > 0) ? sum_range({x2, y1 - 1}) : 0;
        ull left = (x1 > 0) ? sum_range({x1 - 1, y2}) : 0;
        ull diag = (x1 > 0 && y1 > 0) ? sum_range({x1 - 1, y1 - 1}) : 0;

        return total - up - left + diag;
    }
};

// --- Helpers for coordinate compression ---
std::vector<ull> compress_axis(std::vector<ull> vals)
{
    std::sort(vals.begin(), vals.end());
    vals.erase(std::unique(vals.begin(), vals.end()), vals.end());
    return vals;
}

ull get_index(const std::vector<ull> &vals, ull v)
{
    return std::lower_bound(vals.begin(), vals.end(), v) - vals.begin();
}

// --- Build compressed grid ---
struct CompressedData
{
    std::vector<std::vector<char>> grid;
    std::vector<Pos> compressed_coords;
    std::vector<ull> xs;
    std::vector<ull> ys;
};

CompressedData build_compressed_grid(const std::vector<Pos> &coords)
{
    std::vector<ull> xs, ys;
    std::vector<Pos> all_points = coords;

    for (int i = 0; i < coords.size(); i++)
    {
        int j = (i + 1) % coords.size();
        auto between = coords[i].points_between(coords[j]);
        all_points.insert(all_points.end(), between.begin(), between.end());
    }

    for (auto &p : all_points)
    {
        xs.push_back(p.x);
        ys.push_back(p.y);
    }

    xs = compress_axis(xs);
    ys = compress_axis(ys);

    size_t H = ys.size();
    size_t W = xs.size();
    std::vector<std::vector<char>> grid(H, std::vector<char>(W, '.'));

    std::vector<Pos> compressed_coords;
    compressed_coords.reserve(coords.size());

    for (auto &p : coords)
    {
        ull cx = get_index(xs, p.x);
        ull cy = get_index(ys, p.y);
        compressed_coords.push_back({cx, cy});
    }

    for (auto &p : all_points)
    {
        ull cx = get_index(xs, p.x);
        ull cy = get_index(ys, p.y);
        grid[cy][cx] = '#';
    }

    return {grid, compressed_coords, xs, ys};
}

// --- Largest rectangle using compressed coordinates ---
ull largest_rectangle(const std::vector<Pos> &coords, const PrefixSum2D &prefix_sum)
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

            ull candidate_area = (highest_x - lowest_x + 1) * (highest_y - lowest_y + 1);

            Pos adjusted_p1{lowest_x + 1, lowest_y + 1};
            Pos adjusted_p2{highest_x - 1, highest_y - 1};

            if (prefix_sum.sum_range(adjusted_p1, adjusted_p2) > 0)
                continue;

            best_area = std::max(candidate_area, best_area);
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

    auto data = build_compressed_grid(coords);
    PrefixSum2D sum(data.grid);

    ull area = largest_rectangle(data.compressed_coords, sum);

    std::cout << "Answer: " << area << "\n";
}
