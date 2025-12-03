#include <bits/stdc++.h>

using u128 = unsigned __int128;


u128 max_joltage(const std::string& nums, int digits)
{
    std::vector<std::vector<u128>> dp(
        nums.size()+1,
        std::vector<u128>(digits+1, 0)
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

    u128 best = 0;
    for (int i = 0; i <= nums.size(); i++)
        best = std::max(best, dp[i][digits]);

    return best;
}

void print128(u128 x) {
    if (x > 9) print128(x / 10);
    std::cout << (int)(x % 10);
}

int main() {
    u128 total = 0;
    std::string s;
    while (std::cin >> s)
    {
        total += max_joltage(s, 12);
    }

    print128(total);
    std::cout << "\n";
}
