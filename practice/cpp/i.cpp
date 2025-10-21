#include <bits/stdc++.h>
using namespace std;

struct MaxTree {
    typedef pair<int, int> T;
    static constexpr int INF = INT_MAX;
    static constexpr T unit = {-INF, -1};
    T f(T a, T b) {
        if (a.first > b.first || (a.first == b.first && a.second >= b.second))
            return a;
        return b;
    }
    vector<T> s; int n;
    MaxTree(int n = 0, T def = unit) : s(2*n, def), n(n) {}
    void update(int pos, T val) {
        for (s[pos += n] = val; pos /= 2;)
            s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
    }
    T query(int b, int e) { // query [b, e)
        T ra = unit, rb = unit;
        for (b += n, e += n; b < e; b /= 2, e /= 2) {
            if (b % 2) ra = f(ra, s[b++]);
            if (e % 2) rb = f(s[--e], rb);
        }
        return f(ra, rb);
    }
};

struct MinTree {
    typedef pair<int, int> T;
    static constexpr int INF = INT_MAX;
    static constexpr T unit = {INF, -1};
    T f(T a, T b) {
        if (a.first < b.first || (a.first == b.first && a.second <= b.second))
            return a;
        return b;
    }
    vector<T> s; int n;
    MinTree(int n = 0, T def = unit) : s(2*n, def), n(n) {}
    void update(int pos, T val) {
        for (s[pos += n] = val; pos /= 2;)
            s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
    }
    T query(int b, int e) {
        T ra = unit, rb = unit;
        for (b += n, e += n; b < e; b /= 2, e /= 2) {
            if (b % 2) ra = f(ra, s[b++]);
            if (e % 2) rb = f(s[--e], rb);
        }
        return f(ra, rb);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> hs(n);
    for (int i = 0; i < n; i++) cin >> hs[i];

    MaxTree maxTree(n);
    MinTree minTree(n);

    for (int i = 0; i < n; i++) {
        maxTree.update(i, {hs[i], i});
        minTree.update(i, {hs[i], i});
    }

    int q, t;
    cin >> q >> t;

    while (q--) {
        char type;
        int l, r;
        cin >> type >> l >> r;
        l--, r--; // convert to 0-index
        if (type == 'S') {
            auto diff = maxTree.query(l, r + 1).first - minTree.query(l, r + 1).first;
            cout << (diff < t ? "SAFE\n" : "DANGER\n");
        } else {
            auto [max_val, max_i] = maxTree.query(l, r + 1);
            auto [min_val, min_i] = minTree.query(l, r + 1);
            int new_max = (max_val + min_val + 1) / 2;
            int new_min = (max_val + min_val) / 2;

            maxTree.update(max_i, {new_max, max_i});
            maxTree.update(min_i, {new_min, min_i});

            minTree.update(max_i, {new_max, max_i});
            minTree.update(min_i, {new_min, min_i});

        }
    }
}
