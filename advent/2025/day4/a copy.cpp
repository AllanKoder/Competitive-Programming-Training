#include <bits/stdc++.h>

std::vector<std::vector<int>> roll_neighbors(const std::vector<std::string>& grid)
{
    const int ROWS = grid.size();
    const int COLS = grid[0].size();

    std::vector<std::vector<int>> output(ROWS, std::vector<int>(COLS, 0));
    
    std::vector<int> dx = {-1, -1, -1, 0, 0, 1, 1, 1};
    std::vector<int> dy = {-1, 0, 1, 1, -1, 1, 0, -1};

    
    for (int y = 0; y < ROWS; y++)
    {
        for (int x = 0; x < COLS; x++)
        {
            for (int d = 0; d < dx.size(); d++)
            {
                int new_x = x + dx[d];
                int new_y = y + dy[d];
                if (new_x < 0 || new_x >= COLS || new_y < 0 || new_y >= ROWS) continue;
                if (grid[new_y][new_x] != '@') continue;

                output[y][x] += 1;
            }
        }
    }

    return output;
}

int main()
{
    std::vector<std::string> grid;

    std::string s;
    while (std::cin >> s)
    {
        grid.push_back(s);
    }

    auto neighbors = roll_neighbors(grid);

    int counter = 0;
    for (int i = 0; i < neighbors.size(); i++)
    {
        for (int j = 0; j < neighbors[0].size(); j++)
        {
            if (neighbors[i][j] < 4 && grid[i][j] == '@')
            {
                counter++;
                std::cout << "X";
            }
            else
            {
                std::cout << grid[i][j];
            }
        }
        std::cout << "\n";
    }
    std::cout << counter << "\n";
}