#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>

using namespace std;

vector<pair<int,int>> get_neighbours(int y, int x, int height, int width)
{
    vector<pair<int,int>> output;
    if (y >= 1)
        output.push_back({y-1, x});
    if (x >= 1)
        output.push_back({y, x - 1});
    if (x < width - 1)
        output.push_back({y, x  + 1});
    if (y < height - 1)
        output.push_back({y+1, x});
    return output;
}

int main()
{
    unsigned int n, m, k;
    cin >> n >> m >> k;

    vector<string> matrix(n);

    pair<int,int> starter;
    unsigned int period_count = 0;
    for (int y = 0; y < n; y++)
    {
        string input;
        cin >> input;
        matrix[y] = input;

        for (int x = 0; x < m; x++)
        {
            if (matrix[y][x] == '.')
            {
                period_count += 1;
                starter = {y,x};
            }
        }
    }
    queue<pair<int,int>> period_queue({starter});

    unsigned int keeping = period_count - k;
    unsigned int kept = 0;
    set<pair<int,int>> visited;

    while (kept < keeping)
    {
        auto coords = period_queue.front();
        period_queue.pop();

        if (visited.count(coords)) continue;

        kept += 1;
        visited.insert(coords);

        for (auto [new_y, new_x] : get_neighbours(coords.first, coords.second, n, m))
        {
            if (matrix[new_y][new_x] == '.')
            {
                period_queue.emplace(new_y, new_x);
            }
        }
    }


    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (visited.count({i, j}) == 0 && matrix[i][j] == '.')
            {
                cout << "X";
            }
            else
            {
                cout << matrix[i][j];
            }
        }
        cout << "\n";
    }
}