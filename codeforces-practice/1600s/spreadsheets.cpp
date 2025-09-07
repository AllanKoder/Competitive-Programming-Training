#include <bits/stdc++.h>
using namespace std;

string solve_rc_to_excel(const string &s) {
    size_t c_index = s.find('C');
    string row = s.substr(1, c_index - 1);
    int col = stoi(s.substr(c_index + 1));

    string col_str = "";
    while (col > 0) {
        col--;  // Excel is 1-indexed
        col_str += char('A' + (col % 26));
        col /= 26;
    }
    reverse(col_str.begin(), col_str.end());

    return col_str + row;
}

string solve_excel_to_rc(const string &s) {
    size_t i = 0;
    while (i < s.size() && isalpha(s[i])) i++;

    string col_str = s.substr(0, i);
    string row_str = s.substr(i);

    int col = 0;
    for (char c : col_str) {
        col = col * 26 + (c - 'A' + 1);
    }

    return "R" + row_str + "C" + to_string(col);
}

// Detect if a string is RC-style or Excel-style
bool is_rc(const string &s) {
    int switches = 0;
    bool is_alpha = false;
    for (char c : s) {
        if (is_alpha != isalpha(c)) {
            is_alpha = isalpha(c);
            switches++;
        }
    }
    return switches == 4;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string st;
        cin >> st;

        if (is_rc(st)) {
            cout << solve_rc_to_excel(st) << "\n";
        } else {
            cout << solve_excel_to_rc(st) << "\n";
        }
    }
}
