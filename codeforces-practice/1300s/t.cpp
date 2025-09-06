#include <iostream>
#include <vector>
#include <cmath>

int main()
{
    size_t n;
    std::cin >> n;

    std::vector<unsigned long long> nums(n);
    for (size_t i = 0; i < n; i++)
    {
        std::cin >> nums[i];
    }

    // Sieve of Eratosthenes up to 10^6
    const size_t MAX_PRIME = 1000000;
    std::vector<bool> sieve(MAX_PRIME + 1, true);
    sieve[0] = sieve[1] = false;

    for (size_t i = 2; i * i <= MAX_PRIME; i++)
    {
        if (sieve[i])
        {
            for (size_t j = i * i; j <= MAX_PRIME; j += i)
            {
                sieve[j] = false;
            }
        }
    }

    for (auto m : nums)
    {
        unsigned long long root = static_cast<unsigned long long>(std::sqrt(m) + 0.5);
        if (root * root == m && root <= MAX_PRIME && sieve[root])
        {
            std::cout << "YES\n";
        }
        else
        {
            std::cout << "NO\n";
        }
    }
}
