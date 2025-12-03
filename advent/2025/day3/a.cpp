#include <bits/stdc++.h>

unsigned int max_joltage(const std::string& nums)
{
    int best = 0;
    for (int i = 0; i < nums.size()-1; i++)
    {
        for (int j = i+1; j < nums.size(); j++)
        {
            int candidate = (nums[i] - '0') * 10 + (nums[j] - '0');
            best = std::max(best, candidate);
        }
    }
    return best;
}

int main() {
    int total = 0;
    std::string s;
    while (std::cin >> s)
    {
        total += max_joltage(s);
    }

    std::cout << total << "\n";
}
