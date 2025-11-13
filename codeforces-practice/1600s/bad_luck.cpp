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

    int r, s, p;
    cin >> r >> s >> p;
    auto dp = vector(r+1, vector(s+1, vector(p+1, 0.0)));
    
    dp[r][s][p] = 1.0;
    for (int r_i = r; r_i >= 0; r_i--)
    {
        for (int s_i = s; s_i >= 0; s_i--)
        {
            for (int p_i = p; p_i >= 0; p_i--)
            {
                if (dp[r_i][s_i][p_i] == 0.0) continue;
                
                int total = r_i*p_i + s_i*p_i + r_i*s_i;
                if (total == 0) continue;

                
                double current = dp[r_i][s_i][p_i];
                if (r_i > 0 && p_i > 0)
                {
                    dp[r_i-1][s_i][p_i] += current * (r_i*p_i)/(total);
                }
                if (s_i > 0 && p_i > 0)
                {
                    dp[r_i][s_i][p_i-1] += current * (s_i*p_i)/(total);
                }
                if (r_i > 0 && s_i > 0)
                {
                    dp[r_i][s_i-1][p_i] += current * (r_i*s_i)/(total);
                }
            }
        }
    }

    double rocks = 0;
    double papers = 0;
    double scissors = 0;
    rep(i,1,r+1)
    {
        rocks += dp[i][0][0];
    }
    rep(i,1,s+1)
    {
        scissors += dp[0][i][0];
    }
    rep(i,1,p+1)
    {
        papers += dp[0][0][i];
    }
    
    cout << setprecision(12) << endl;
    cout << rocks << " " << scissors << " " << papers << endl;
}

