#include <bits/stdc++.h>

using ull = unsigned long long;

struct Pos
{
    ull x;
    ull y;

    friend std::ostream& operator<<(std::ostream& os, const Pos& p)
    {
        os << "(" << p.x << "," << p.y << ")";
        return os;
    }
};

std::vector<Pos> raw_string_to_coords(const std::vector<std::string>& raw_inputs)
{
    std::vector<Pos> coords;

    for (auto s: raw_inputs)
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

    // for (auto c: coords)
    // {
    //     std::cout << "x:" << c.x << " y:" << c.y << "\n";
    // }
    return coords;
}

ull largest_rectangle(const std::vector<Pos>& coords)
{
    ull best_area = 0;
    for (int i = 0; i < coords.size(); i++)
    {
        Pos pos1 = coords[i];
        for (int j = i+1; j < coords.size(); j++)
        {
            Pos pos2 = coords[j];
            ull highest_x = std::max(pos1.x, pos2.x);
            ull lowest_x = std::min(pos1.x, pos2.x);

            ull highest_y = std::max(pos1.y, pos2.y);
            ull lowest_y = std::min(pos1.y, pos2.y);

            // std::cout << pos1 << pos2 << " " << highest_x << " " <<  lowest_x  << " " << highest_y  << " " << lowest_y << "\n";

            ull candidate_area = (highest_x - lowest_x + 1) * (highest_y - lowest_y + 1);
            best_area = std::max(candidate_area, best_area);
        }
    }

    return best_area;
}

int main()
{
    std::vector<std::string> raw_inputs;
    std::string s;
    while(std::getline(std::cin, s))
    {
        raw_inputs.push_back(s);
    }

    std::vector<Pos> coords = raw_string_to_coords(raw_inputs);
    ull area = largest_rectangle(coords);

    std::cout << "Answer: " << area << "\n";
}