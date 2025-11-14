#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, p;
    cin >> n >> p;
    p--; // convert to 0-based

    string s;
    cin >> s;

    int half = n / 2;

    // If cursor in right half, mirror it to left half
    if (p >= half) p = n - 1 - p;

    vector<int> bad;
    long long edit_cost = 0;

    // Collect mismatches
    for (int i = 0; i < half; i++) {
        int j = n - 1 - i;
        if (s[i] != s[j]) {
            bad.push_back(i);
            int diff = abs(s[i] - s[j]);
            edit_cost += min(diff, 26 - diff);
        }
    }

    if (bad.empty()) {
        cout << 0 << "\n";
        return 0;
    }

    int L = bad.front();
    int R = bad.back();

    long long movement = 0;
    if (L == R) {
        movement = llabs(p - L);
    } else {
        movement = (R - L) + min( (long long)abs(p - L), (long long)abs(p - R) );
    }

    cout << movement + edit_cost << "\n";
    return 0;
}
