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

    int n, k, p;
    cin >> n >> k >> p;

    vector<ll> people(n);
    vector<ll> keys(k);

    rep(i, 0, n) cin >> people[i];
    rep(i, 0, k) cin >> keys[i];
    sort(people.begin(), people.end());
    sort(keys.begin(), keys.end());


    vector<vector<ll>> dp(n+1, vector<ll>(k+1, LONG_LONG_MAX));

    rep(key, 0, k+1) dp[n][key] = 0;

    for(int i = n-1; i >= 0; i--)
    {
        for(int key = k-1; key >= 0; key--)
        {
            // Distance
            ll distance = abs(people[i] - keys[key]) + abs(keys[key] - p);

            dp[i][key] = min(max(distance, dp[i+1][key+1]), dp[i][key+1]);
        }
    }

    cout << dp[0][0];
}

