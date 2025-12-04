#include <bits/stdc++.h>


std::vector<std::pair<int,int>> neighbors(int y, int x, int COLS, int ROWS)
{
    std::vector<std::pair<int,int>> output;
    std::vector<int> dx = {-1, -1, -1, 0, 0, 1, 1, 1};
    std::vector<int> dy = {-1, 0, 1, 1, -1, 1, 0, -1};

    for (int d = 0; d < dx.size(); d++)
    {
        int new_x = x + dx[d];
        int new_y = y + dy[d];
        if (new_x < 0 || new_x >= COLS || new_y < 0 || new_y >= ROWS) continue;
        output.push_back({new_y, new_x});
    }
    return output;
}

std::vector<std::vector<int>> roll_neighbors(const std::vector<std::string>& grid)
{
    const int ROWS = grid.size();
    const int COLS = grid[0].size();

    std::vector<std::vector<int>> output(ROWS, std::vector<int>(COLS, 0));
    
    for (int y = 0; y < ROWS; y++)
    {
        for (int x = 0; x < COLS; x++)
        {
            auto neighs = neighbors(y, x, ROWS, COLS);
            for (auto [new_y, new_x]: neighs)
            {
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
    const int MAX_ROLLS = 4;
    std::string s;
    while (std::cin >> s)
    {
        grid.push_back(s);
    }

    auto neighbors_matrix = roll_neighbors(grid);

    int counter = 0;

    bool removed = true;
    while(removed)    
    {
        removed = false;
        for (int i = 0; i < neighbors_matrix.size(); i++)
        {
            for (int j = 0; j < neighbors_matrix[0].size(); j++)
            {
                if (neighbors_matrix[i][j] < MAX_ROLLS && grid[i][j] == '@')
                {
                    counter++;
                    grid[i][j] = '.';

                    for (auto [neigh_y, neigh_x]: neighbors(i, j, grid[0].size(), grid.size()))
                    {
                        neighbors_matrix[neigh_y][neigh_x]--;
                    }

                    std::cout << "X";
                    removed = true;
                }
                else
                {
                    std::cout << grid[i][j];
                }
            }
            std::cout << "\n";
        }
    }
    std::cout << counter << "\n";
}