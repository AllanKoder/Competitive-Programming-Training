#include <bits/stdc++.h>


std::vector<long long> z_function(std::string s)
{
    std::vector<long long> z(s.size(), 0);
    long long r = 0;
    long long l = 0;

    for (long long i = 1; i < s.size(); i++)
    {
        if (i <= r)
        {
            z[i] = std::min(z[i-l], r - i + 1);
        }
        while(i + z[i] < s.size() && s[i + z[i]] == s[z[i]])
        {
            z[i]++;
        }

        if (z[i] + i - 1> r)
        {
            l = i;
            r = i + z[i] - 1;
        }
    }
    std::cout << "val: " << s << " ";
    for (auto c : z)
    {
        std::cout << c << " ";
    }
    std::cout << "\n";
    return z;
}


bool is_repeated(std::string s)
{
    std::vector<long long> z = z_function(s);

    for (long long p = 1; p < s.size(); p++)
    {
        if (s.size() % p == 0 && z[p] + p == s.size())
            return true;
    }
    return false;
}

int main() {
    int total = 0;
    std::string a;
    std::getline(std::cin, a);

    std::vector<std::string> ids;
    std::stringstream ss(a);
    std::string id;

    // Split by comma
    while (std::getline(ss, id, ',')) {
        ids.push_back(id);
    }

    for (const auto& id : ids) {
        size_t dash = id.find('-');
        long long first = std::stoll(id.substr(0, dash));
        long long last = std::stoll(id.substr(dash + 1));

        for (long long i = first; i <= last; ++i) {
            std::string s = std::to_string(i);
            if (is_repeated(s)) {
                total += i;
            }
        }
    }

    std::cout << total << std::endl;
    return 0;
}