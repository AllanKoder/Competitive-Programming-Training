#include <bits/stdc++.h>

using ull = unsigned long long;

ull max_joltage(const std::string& nums, int digits)
{
    std::vector<std::vector<ull>> dp(
        nums.size()+1,
        std::vector<ull>(digits+1, 0)
    );

    for (int i = 0; i < nums.size(); i++)
    {
        int current = nums[i] - '0';
        for (int d = 0; d < digits; d++)
        {
            for (int j = i+1; j <= nums.size(); j++)
            {
                dp[j][d+1] = std::max(dp[j][d+1], dp[i][d] * 10 + current);
            }
        }
    }

    ull best = 0;
    for (int i = 0; i <= nums.size(); i++)
        best = std::max(best, dp[i][digits]);

    return best;
}

int main() {
    ull total = 0;
    std::string s;
    while (std::cin >> s)
    {
        total += max_joltage(s, 12);
    }

    std::cout << (total);
    std::cout << "\n";
}
