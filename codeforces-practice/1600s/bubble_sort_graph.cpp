#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int lis(const vi& a)
{
    vi b;
    b.push_back(a[0]);
    rep(i, 1, a.size())
    {
        int index = upper_bound(b.begin(), b.end(), a[i]) - b.begin();
        if (index == b.size())
        {
            b.push_back(a[i]);
        }
        else{
            b[index] = a[i];
        }

    }
    return b.size();
}


int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);
    int n;
    cin >> n;

    vi a(n,0);
    rep(i,0,n) cin >> a[i];
    cout << lis(a) << endl;
}  

