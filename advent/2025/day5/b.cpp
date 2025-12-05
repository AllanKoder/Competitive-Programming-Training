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

std::vector<std::pair<ull, ull>> ranges_to_disjoint(const std::vector<std::pair<ull,ull>>& int_ranges)
{
    std::vector<std::pair<ull, ull>> merged_ranges(int_ranges);
    for (int k = 0; k < int_ranges.size(); k++)
    {
        for (int i = 0; i < merged_ranges.size(); i++)
        {
            auto one = merged_ranges[i];
            for (int j = 0; j < merged_ranges.size(); j++)
            {
                auto two = merged_ranges[j];
                if (one.second >= two.first && one.first <= two.second)
                {
                    std::pair<ull, ull> merged_range = {std::min(one.first, two.first), std::max(one.second, two.second)};
                    merged_ranges[i] = merged_range;
                    merged_ranges[j] = merged_range;
                    // std::cout << merged_ranges[i].first << "-" << merged_ranges[i].second << "\n";
                }
            }
        }
    }
    
    std::set<std::pair<ull,ull>> setted_merged(merged_ranges.begin(),merged_ranges.end());
    return std::vector<std::pair<ull,ull>>(setted_merged.begin(), setted_merged.end());
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

    ull counter = 0;
    std::vector<std::pair<ull, ull>> ull_ranges = string_ranges_to_ulls(string_ranges);
    std::vector<std::pair<ull, ull>> disjoint_ranges = ranges_to_disjoint(ull_ranges);

    counter = std::accumulate(disjoint_ranges.begin(), disjoint_ranges.end(), counter,
    [](ull current_sum, std::pair<ull,ull> p){
        return current_sum + (p.second - p.first + 1);
    });

    std::cout << "Answer: " << counter << "\n";
}