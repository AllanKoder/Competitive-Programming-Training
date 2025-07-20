#include <iostream>
#include <vector>

int main()
{
    int n, a, b, c;
    std::cin >> n >> a >> b >> c;

    int options[] = {a,b,c};
    std::vector<int> dp(n+1,-1);

    dp[0] = 0;
    for (int i = 0; i <= n; i++)
    {
        for (auto r: options)
        {
            if (i-r >= 0 && dp[i-r] >= 0)
            {
                dp[i] = std::max(dp[i], dp[i-r] + 1);
            }
        }
    }

    std::cout << dp[n];
}
