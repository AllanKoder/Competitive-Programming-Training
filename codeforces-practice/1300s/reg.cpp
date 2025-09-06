#include <iostream>
#include <unordered_map>
#include <string>
#include <unordered_set>

std::unordered_map<std::string, int> str_to_count;
std::unordered_map<std::string, std::unordered_set<int>> str_to_uses;
int main()
{
    int n;
    std::cin >> n;

    auto get_prefix_index = [](const std::string& input)
    {
        for (size_t i = 0; i < input.size(); i++)
        {
            if (std::isdigit(input[i]))
            {
                return i;
            }
        }
        return input.size();
    };

    for (size_t i = 0; i < n; i++)
    {
        std::string in;
        std::cin >> in;

        size_t index = get_prefix_index(in);
        std::string base = in.substr(0, index);
        size_t num = (index == in.size()) ? 0 : std::stoi(in.substr(index));

        if (str_to_uses[base].count(num) == 0 && num >= str_to_count[base])
        {
            str_to_uses[base].insert(num);
            str_to_count[base] += 1;
            std::cout << "OK\n";
        }
        else
        {
            size_t start = str_to_count[base];
            while (str_to_uses[base].count(start) != 0)
            {
                start += 1;
            }

            str_to_count[base] = start + 1;
            std::cout << base << start << "\n";
        }
    }
}
