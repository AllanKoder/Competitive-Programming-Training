#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    unsigned int v, e;
    std::cin >> v >> e; 
    std::string trail;
    std::cin >> trail;

    std::vector<std::pair<int,int>> edges;
    edges.reserve(e);
    for (unsigned int i = 0; i < e; i++) {
        int from_pos, to_pos;
        std::cin >> from_pos >> to_pos;
        edges.emplace_back(from_pos, to_pos);
    }

    std::sort(edges.begin(), edges.end());

    std::vector<long long> max_happiness(v, -1);
    max_happiness[0] = 0;

    for (unsigned int i = 0; i < e; i++) {
        int from = edges[i].first;
        int to   = edges[i].second;

        if (max_happiness[from] == -1)
            continue;

        int addition = 0;
        if (to < v-1) {
            addition = (trail[to] == 'X' ? 1 : -1);
        }

        long long new_happiness = max_happiness[from] + addition;
        if (max_happiness[to] == -1 || new_happiness > max_happiness[to]) {
            max_happiness[to] = new_happiness;
        }
    }

    std::cout << max_happiness[v-1] << "\n";
}
