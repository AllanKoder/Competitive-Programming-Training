#include <bits/stdc++.h>

using ull = unsigned long long;

std::vector<std::pair<ull, ull>> string_ranges_to_ulls(const std::vector<std::string>& string_ranges)
{
    std::vector<std::pair<ull, ull>> pairs_ranges;

    for (ull i = 0; i < string_ranges.size(); i++)
    {
        std::string range = string_ranges[i];
        size_t delimiter_index = range.find('-');
        ull first = std::stoull(range.substr(0, delimiter_index));
        ull second = std::stoull(range.substr(delimiter_index+1));
        pairs_ranges.push_back({first, second});
    }
    
    return pairs_ranges;
}

bool range_counts(ull numb, const std::vector<std::pair<ull,ull>>& ranges)
{
    for (auto &[low, high] : ranges)
    {
        if (low <= numb && numb <= high)
        {
            return true;
        }
    }
    return false;
}

int main() 
{
    std::vector<std::string> string_ranges;

    std::string s;
    while(std::getline(std::cin, s))
    {
        if (s == "") break;
        string_ranges.push_back(s);
    }

    std::vector<std::pair<ull, ull>> ull_ranges = string_ranges_to_ulls(string_ranges);
    ull counter = 0;
    while(std::cin >> s)
    {
        ull numb = std::stoull(s);
        if (range_counts(numb, ull_ranges))
        {   
            counter++;
        }
    }

    std::cout << "Answer: " << counter << "\n";
}