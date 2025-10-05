#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
int d;
long long m;
map<tuple<int,bool,bool,long long>, long long> memo;
string L_str, R_str;
int n;

long long dp(int i, bool is_low, bool is_high, long long mod) {
    if (i == n) return mod == 0 ? 1 : 0;

    auto key = make_tuple(i, is_low, is_high, mod);
    if (memo.count(key)) return memo[key];

    int low_limit = is_low ? L_str[i] - '0' : 0;
    int high_limit = is_high ? R_str[i] - '0' : 9;
    bool is_even = (i+1) % 2 == 0;

    long long res = 0;
    for (int j = low_limit; j <= high_limit; ++j) {
        if (is_even && j != d) continue;
        if (!is_even && j == d) continue;

        bool next_low = is_low && (j == low_limit);
        bool next_high = is_high && (j == high_limit);

        long long next_mod = (mod * 10 + j) % m; // compute modulo on the fly
        res = (res + dp(i+1, next_low, next_high, next_mod)) % MOD;
    }

    return memo[key] = res;
}

long long solve(string l_str, string r_str, int dd, long long mm) {
    d = dd;
    m = mm;

    n = r_str.size();
    while (l_str.size() < n) l_str = '0' + l_str; // pad L

    L_str = l_str;
    R_str = r_str;

    memo.clear();
    return dp(0, true, true, 0);
}

int main() {
    cin >> m >> d;
    string l, r;
    cin >> l >> r;

    cout << solve(l, r, d, m) << endl;
    return 0;
}
