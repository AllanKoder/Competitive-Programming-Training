#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    string s;
    cin >> s;

    unordered_set<char> m;
    for (auto c: s)
    {
        m.insert(c);
    }

    cout << ((m.size() % 2 == 1) ? "IGNORE HIM!" : "CHAT WITH HER!");
}

