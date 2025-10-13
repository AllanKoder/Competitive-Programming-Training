#include <bits/stdc++.h>
using namespace std;

struct Cell {
    int y, x, dist, tower;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, N;
    cin >> R >> C >> N;
    vector<tuple<int,int,int>> towers;
    for (int i = 1; i <= N; i++) {
        int y, x;
        cin >> y >> x;
        towers.emplace_back(y - 1, x - 1, i);
    }

    const int INF = 1e9;
    vector<vector<pair<int,int>>> first(R, vector<pair<int,int>>(C, {INF, INF}));
    vector<vector<pair<int,int>>> second(R, vector<pair<int,int>>(C, {INF, INF}));

    queue<Cell> q;
    // sort towers to guarantee tie-breaking by tower id
    sort(towers.begin(), towers.end(),
         [](auto &a, auto &b){ return get<2>(a) < get<2>(b); });
    for (auto &[y, x, id] : towers)
        q.push({y, x, 0, id});

    int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};

    while (!q.empty()) {
        auto [y, x, dist, tower] = q.front();
        q.pop();

        if (dist > second[y][x].first)
            continue;

        // update best two
        if (make_pair(dist, tower) < first[y][x]) {
            second[y][x] = first[y][x];
            first[y][x] = {dist, tower};
        } else if (tower != first[y][x].second &&
                   make_pair(dist, tower) < second[y][x]) {
            second[y][x] = {dist, tower};
        } else continue;

        for (auto &d : dirs) {
            int ny = y + d[0], nx = x + d[1];
            if (ny < 0 || ny >= R || nx < 0 || nx >= C)
                continue;
            q.push({ny, nx, dist + 1, tower});
        }
    }

    // output
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (j) cout << ' ';
            cout << first[i][j].second;
        }
        cout << '\n';
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (j) cout << ' ';
            cout << second[i][j].second;
        }
        cout << '\n';
    }
}
