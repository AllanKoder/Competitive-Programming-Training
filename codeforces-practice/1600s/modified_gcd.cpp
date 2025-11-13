#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

vi shared_divisors(int i, int j)
{  
    int k = gcd(i,j);
    set<int> s;
    for (int j = 1; j*j <= k; j++)
    {
        if (k % j == 0)
        {
            s.insert(j);
            s.insert(k/j);
        }
    }
    return vi(s.begin(), s.end());
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int low, high;
    cin >> low >> high;

    auto all_divisors = shared_divisors(low, high);

    int t;
    cin >> t;

    while (t--)
    {
        int l, r;
        cin >> l >> r;

        int left_index = lower_bound(all_divisors.begin(), all_divisors.end(), l) - all_divisors.begin();
        int right_index = upper_bound(all_divisors.begin(), all_divisors.end(), r) - all_divisors.begin();
        if (left_index == right_index)
        {
            cout << "-1" << endl;
        }
        else
        {
            cout << all_divisors[right_index-1] << endl;
        }

        // for (auto c: all_divisors)
        // {
        //     cout << c <<  " ";
        // }
    }
}

