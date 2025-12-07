#include <bits/stdc++.h>

using ull = unsigned long long;

bool within_bounds(ull y, ull x, ull size_y, ull size_x)
{
    return x >= 0 && y >= 0 && x < size_x && y < size_y;
}

struct State {
    ull y;
    ull x;
    bool operator<(const State& other) const 
    {
        if (y != other.y) return other.y > y;
        return other.x > x;
    }
};


ull dp_split_counter(State pos, const std::vector<std::string>& matrix, std::map<State, ull>& cache)
{
    if (cache.count(pos) != 0)
    {
        return cache[pos];
    }

    ull size_y = matrix.size();
    ull size_x = matrix[0].size();

    if (!within_bounds(pos.y, pos.x, size_y, size_x)) return 1;

    if (matrix[pos.y][pos.x] == '.')
    {
        State down_pos(pos);
        down_pos.y++;
        cache[pos] = dp_split_counter(down_pos, matrix, cache);
        return cache[pos];
    }

    std::array<int, 2> dxs = {-1, 1};
    ull count = 0;
    cache[pos] = 0;
    for (auto dx : dxs)
    {
        State x_pos(pos);
        x_pos.x += dx;

        if (!within_bounds(x_pos.y, x_pos.x, size_y, size_x)) continue;

        cache[pos] += dp_split_counter(x_pos, matrix, cache);
    }
    return cache[pos];
}

int main() 
{
    std::vector<std::string> matrix;
    std::string row;
    while(std::getline(std::cin, row))
    {
        matrix.push_back(row);
    }

    ull starting_x = 0;
    for (ull x = 0; x < matrix[0].size(); x++)
    {
        if (matrix[0][x] == 'S')
        {
            starting_x = x;
            break;
        }
    }

    State starting_pos;
    starting_pos.x = starting_x;
    starting_pos.y = 0;
    std::map<State,ull> cache;
    ull answer = dp_split_counter(starting_pos, matrix, cache);

    std::cout << "Answer: " << answer << "\n";
}