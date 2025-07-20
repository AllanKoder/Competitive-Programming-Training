#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

std::unordered_map<int, std::unordered_map<int, int>> cache;
std::unordered_map<int, std::vector<int>> adj_list;

int longest_path_to_leaf(int node, int prev)
{
    if (cache[node].count(prev)) return cache[node][prev];

    int output = 0;
    for (auto neighbor : adj_list[node])
    {
        if (neighbor != prev)
        {
            output = std::max(output, longest_path_to_leaf(neighbor, node) + 1);
        }
    }

    cache[node][prev] = output;
    return cache[node][prev];
}

int main()
{
    int nodes, edges;
    std::cin >> nodes >> edges;

    for(int i = 0; i < edges; i++)
    {
        int node1, node2;
        std::cin >> node1 >> node2;
        adj_list[node1].push_back(node2);
        adj_list[node2].push_back(node1);
    }

    for (int j = 0; j < nodes; j++)
    {
        std::cout << longest_path_to_leaf(j, -1) << "\n";
    }
}
