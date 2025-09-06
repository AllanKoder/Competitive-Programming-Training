#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int count;
    std::cin >> count;

    std::vector<std::pair<int,int>> vec;
    for (int i = 0; i < count; i++)
    {
        int price, quality;
        std::cin >> price >> quality;
        vec.emplace_back(price,quality);
    }

    std::sort(vec.begin(), vec.end());

    for (int i = 0; i < count - 1; i++)
    {
        if (vec[i+1].second < vec[i].second)
        {
            std::cout << "Happy Alex";
            return 0;
        }
    }
    std::cout << "Poor Alex";
}
