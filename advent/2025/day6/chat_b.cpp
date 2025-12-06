#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<string> grid;
    string line;
    while (getline(cin, line)) {
        grid.push_back(line);
    }

    int R = grid.size();
    int C = grid[0].size();

    // Find columns that contain *only spaces*
    vector<bool> empty_col(C, true);
    for (int c = 0; c < C; c++) {
        for (int r = 0; r < R; r++) {
            if (grid[r][c] != ' ') {
                empty_col[c] = false;
                break;
            }
        }
    }

    // Split into groups by empty columns
    vector<pair<int,int>> groups;
    int c = 0;
    while (c < C) {
        while (c < C && empty_col[c]) c++;
        if (c >= C) break;
        int start = c;
        while (c < C && !empty_col[c]) c++;
        int end = c - 1;
        groups.push_back({start, end});
    }

    long long total = 0;

    // Process each group
    for (auto [L, Rc] : groups) {

        // Operator is in bottom row
        char op = 0;
        for (int c2 = L; c2 <= Rc; c2++) {
            if (grid.back()[c2] == '+' || grid.back()[c2] == '*') {
                op = grid.back()[c2];
                break;
            }
        }
        if (!op) continue; // shouldn't happen on AoC inputs

        // Read numbers column-wise (right-to-left)
        vector<long long> numbers;

        for (int col = Rc; col >= L; col--) {
            // Skip operator column or any column that's just space in all but last row
            bool all_spaces = true;
            for (int r = 0; r < R-1; r++) {
                if (grid[r][col] != ' ') {
                    all_spaces = false;
                    break;
                }
            }
            if (all_spaces) continue;

            // Build this number from top to bottom
            string num = "";
            for (int r = 0; r < R-1; r++) {
                if (isdigit(grid[r][col])) {
                    num.push_back(grid[r][col]);
                }
            }
            if (!num.empty()) {
                numbers.push_back(stoll(num));
            }
        }

        // Evaluate the problem
        long long result = (op == '+') ? 0 : 1;
        for (long long x : numbers) {
            if (op == '+') result += x;
            else result *= x;
        }

        total += result;
    }

    cout << total << "\n";
    return 0;
}
