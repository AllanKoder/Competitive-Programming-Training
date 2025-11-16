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

    int t;
    cin >> t;

    while (t--)
    {
        int n; 
        cin >> n;
        vi p(n,0);
        string s;
        rep(i,0,n) cin >> p[i];
        cin >> s;

        if (s[0] == '1' || s[n-1] == '1')
        {
            cout << -1 << "\n";
            continue;
        }

        int mx_i = max_element(p.begin(), p.end())-p.begin();
        int mn_i = min_element(p.begin(), p.end())-p.begin();
        if (s[mx_i] == '1' || s[mn_i] == '1')
        {
            cout << -1 << "\n";
            continue;
        }

        mn_i++;
        mx_i++;
        cout << "5\n";
        cout << "1 " << mn_i << "\n";
        cout << mn_i << " " << n << "\n";
        
        cout << "1 " << mx_i << "\n";
        cout << mx_i << " " << n << "\n";
        cout << min(mx_i,mn_i) << " " << max(mn_i, mx_i) << "\n";
    }
}

