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
        vi a(n);
        rep(i,0,n) cin >> a[i];
        sort(a.begin(), a.end());

        bool found = false;
        for (int i = 1; i < n-1; i+=2)
        {
            if (a[i] < a[i+1])
            {
                cout << "NO\n";
                found = true;
                break;
            }
        }

        if (!found) cout << "YES\n";
    }
}

