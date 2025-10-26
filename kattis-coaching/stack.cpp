#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int solve(const string& s)
{
    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    rep(i,0,n) { dp[i][i] = 2; }

    rep(length, 2, n+1)
    {
        // index
        rep(start, 0, n-length+1)
        {
            int end = start + length - 1;

            dp[start][end] = 2 + dp[start+1][end];
            
            rep(k, start + 1, end + 1)
            {
                if (s[start] == s[k])
                {
                    dp[start][end] = min(dp[start][end], dp[start+1][k-1] + dp[k][end]);
                }
            }
        }
    }

    // rep(i, 0, n)
    // {
    //     rep(j,0,n)
    //     {
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << "\n";
    // }


    return dp[0][n-1];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int T;
    cin >> T;
    cin.ignore();

    rep(_,0,T)
    {
        string s;
        getline(cin, s);
        cout << solve(s) + (int)s.size() << "\n";
    }
}

