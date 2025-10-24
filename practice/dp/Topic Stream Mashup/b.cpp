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

    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    vector<char> letters(k);
    unordered_set<char> letters_set;

    for (int i = 0; i < k; i++)
    {
        cin >> letters[i];
        letters_set.insert(letters[i]);
    }

    unsigned long long current_count = 0;
    unsigned long long total_count = 0;
    for (int i = 0; i <= n; i++)
    {
        if (i == n || letters_set.count(s[i]) == 0)
        {
            total_count += (current_count * (current_count+1))/2;
            current_count = 0;
        }
        else
        {
            current_count++;
        }
    }

    cout << total_count;
}

