#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


typedef struct Cube {
    int down = 0;
    int up = 1;
    int left = 2;
    int right = 3;
    int back = 4;
    int front = 5;
};

Cube rotate_left(Cube c)
{
    Cube new_cube = c;
    new_cube.up = c.right;
    new_cube.left = c.up;
    new_cube.down = c.left;
    new_cube.right = c.down;
    return new_cube;
}
Cube rotate_forward(Cube c)
{
    Cube new_cube = c;
    new_cube.front = c.up;
    new_cube.up = c.back;
    new_cube.back = c.down;
    new_cube.down = c.front;
    return new_cube;
}


const int N = 6;
bool bfs(int starting_row, int starting_col, vector<string>& matrix)
{
    vi dx = {-1, 1, 0, 0};
    vi dy = {0, 0, 1, -1};

    using p = pair<int,int>;
    deque<pair<p, Cube>> queue;

    set<p> visited;
    set<int> faces;
    queue.push_back({{starting_row,starting_col}, Cube()});

    while (queue.size())
    {
        auto [coord, cube] = queue.front();
        queue.pop_front();
        int row = coord.first;
        int col = coord.second;

        if (matrix[row][col] == '.') continue;
        if (visited.count(coord)) continue;
        visited.insert(coord);
        faces.insert(cube.down);

        rep(k, 0, 4)
        {
            int new_y = dy[k] + row;
            int new_x = dx[k] + col;
            if (new_x < 0 || new_x >= N || new_y < 0 || new_y >= N) continue;
            p new_coord {new_y, new_x};
            
            if (k == 0) queue.push_back({new_coord, rotate_left(cube)});
            if (k == 1) queue.push_back({new_coord, rotate_left(rotate_left(rotate_left(cube)))});
            if (k == 2) queue.push_back({new_coord, rotate_forward(rotate_forward(rotate_forward(cube)))});
            if (k == 3) queue.push_back({new_coord, rotate_forward(cube)});
        }

    }

    return faces.size() == 6;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    vector<string> matrix(N);

    rep(i,0,N)
    {
        cin >> matrix[i];
    }

    rep(i, 0, N)
    {
        rep(j,0, N)
        {
            if (matrix[i][j] == '#')
            {
                if (bfs(i,j, matrix))
                {
                    cout << "can fold";
                    return 0;
                }
            }
        }
    }

    cout << "cannot fold";
}

