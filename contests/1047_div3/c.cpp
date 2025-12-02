#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

ll solve(ll a, ll b)
{
    ll best = (a+b)%2==0 ? (a + b) : -1;
    while (b % 2 == 0)
    {
        b /= 2;

    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    while(t--)
    {
        ll a, b;
        cin >> a >> b;
        cout << solve(a,b) << "\n";
    }
}

