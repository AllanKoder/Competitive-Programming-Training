#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

template<class I> vi lis(const vector<I>& S) {
if (S.empty()) return {};
vi prev(sz(S));
typedef pair<I, int> p;
vector<p> res;
rep(i,0,sz(S)) {
// change 0 => i for longest non=decreasing subsequence
auto it = lower_bound(all(res), p{S[i], i});
if (it == res.end()) res.emplace_back(), it = res.end()-1;
*it = {S[i], i};
prev[i] = it == res.begin() ? 0 : (it-1)->second;
}
int L = sz(res), cur = res.back().second;
vi ans(L);
while (L--) ans[L] = cur, cur = prev[cur];
return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vi tasks(n);
    for (int i = 0; i < n; ++i) cin >> tasks[i]; // tasks are 0,1,2 per problem

    vi p = {0,1,2};
    int best = 0;
    do {
        vi n_tasks(n);
        for (int i = 0; i < n; i++)
        {
            n_tasks[i] = p[tasks[i]];
        }
        best = max(best, (int) lis(n_tasks).size());
    } while (next_permutation(p.begin(), p.end()));

    cout << best << '\n';
    return 0;
}
