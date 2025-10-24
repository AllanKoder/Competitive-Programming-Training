#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int ways(int n)
{
    if (n % 2 == 1) return 0;
    if (n <= 0) return 1;

    return 2 * ways(n-2);
}

int main() {


    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int n;
    cin >> n;
    int ans = ways(n);
    cout << (ans > 1 ? ans : 0) << "\n";
}

