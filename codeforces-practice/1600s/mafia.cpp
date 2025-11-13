#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

bool valid(ll h, const vi& a)
{
    ll cnt = 0;
    for (int x : a) cnt += (ll)h - x;
    return cnt >= h;
}

ll solve(ll l, ll r, const vi& a)
{
    while (l < r)
    {
        ll m = (l + r) / 2;
        if (valid(m, a)) r = m;
        else l = m + 1;
    }
    return l;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vi a(n);

    ll sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
    }

    ll lo = *max_element(a.begin(), a.end());
    ll hi = sum;

    cout << solve(lo, hi, a) << "\n";
}
