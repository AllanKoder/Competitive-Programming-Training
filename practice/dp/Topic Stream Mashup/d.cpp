#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<(b);++i)
typedef vector<int> vi;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vi lectures(n);
    vi ps_lectures(n+1, 0);
    vi is_awake(n);

    rep(i,0,n) {
        cin >> lectures[i];
        ps_lectures[i+1] = ps_lectures[i] + lectures[i];
    }

    rep(i,0,n) cin >> is_awake[i];

    vector<vector<ll>> dp(n+1, vector<ll>(2, 0));

    rep(i,0,n) {
        rep(used,0,2) {
            dp[i+1][used] = max(dp[i+1][used], dp[i][used]);

            if (is_awake[i])
                dp[i+1][used] = max(dp[i+1][used], dp[i][used] + lectures[i]);

            if (!used) {
                int r = min(n, i + k);
                ll sum_awake = ps_lectures[r] - ps_lectures[i];
                dp[r][1] = max(dp[r][1], dp[i][0] + sum_awake);
            }
        }
    }

    cout << max(dp[n][0], dp[n][1]) << "\n";
}
