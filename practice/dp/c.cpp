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

    int n;
    cin >> n;

    // ABC

    vector<pair<string, int>> string_and_cost;
    rep(i, 0, n)
    {
        int c;
        string s;
        cin >> c >> s;
        string_and_cost.emplace_back(s, c);
    }

    const int INF = 1e9;
    vector<vector<vector<int>>> dp(2, vector<vector<int>>(2, vector<int>(2, INF)));

    dp[0][0][0] = 0;

    rep(has_a, 0, 2)
    {
        rep(has_b, 0, 2)
        {
            rep(has_c, 0, 2)
            {
                rep(i,0,n)
                {
                    auto p = string_and_cost[i];

                    bool new_has_a = has_a || count(p.first.begin(), p.first.end(), 'A');
                    bool new_has_b = has_b || count(p.first.begin(), p.first.end(), 'B');
                    bool new_has_c = has_c || count(p.first.begin(), p.first.end(), 'C');
                    
                    dp[new_has_a][new_has_b][new_has_c] = 
                    min(dp[new_has_a][new_has_b][new_has_c], dp[has_a][has_b][has_c] + p.second);
                }
            }
        }
    }
    

    cout << (dp[1][1][1] != INF ? dp[1][1][1] : -1) << "\n";

}