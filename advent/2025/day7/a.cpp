#include <bits/stdc++.h>

using ull = unsigned long long;

bool within_bounds(int y, int x, int size_y, int size_x)
{
    return x >= 0 && y >= 0 && x < size_x && y < size_y;
}

ull bfs_split_counter(int starting_x, const std::vector<std::string>& matrix)
{
    std::set<std::pair<int, int>> visited;
    std::queue<std::pair<int,int>> queue;
    queue.push({0, starting_x});

    int size_y = matrix.size();
    int size_x = matrix[0].size();

    ull counter = 0;
    while (queue.size())
    {
        auto [pos_y, pos_x] = queue.front();
        // std::cout << pos_y << " " << pos_x << "\n";
        queue.pop();

        if (visited.count({pos_y, pos_x}) != 0) continue;
        visited.emplace(pos_y, pos_x);

        int new_y = pos_y + 1;
        if (!within_bounds(new_y, pos_x, size_y, size_x)) continue;

        if (matrix[new_y][pos_x] == '.')
        {
            queue.push({new_y, pos_x});
        }
        else
        {
            std::array<int, 2> dxs = {-1, 1};
            for (auto dx : dxs)
            {
                int new_x = pos_x + dx;
                if (!within_bounds(new_y, new_x, size_y, size_x)) continue;
                queue.push({new_y, new_x});
            }
            counter++;
        }
    }

    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[0].size(); j++)
        {
            if (visited.count({i, j}) != 0)
            {
                std::cout << "|";
            }
            else
            {
                std::cout << matrix[i][j];
            }
        }
        std::cout << "\n";
    }

    return counter;
}

int main() 
{
    std::vector<std::string> matrix;
    std::string row;
    while(std::getline(std::cin, row))
    {
        matrix.push_back(row);
    }

    int starting_x = 0;
    for (int x = 0; x < matrix[0].size(); x++)
    {
        if (matrix[0][x] == 'S')
        {
            starting_x = x;
            break;
        }
    }

    ull answer = bfs_split_counter(starting_x, matrix);

    std::cout << "Answer: " << answer << "\n";
}