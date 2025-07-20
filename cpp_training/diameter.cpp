#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

std::unordered_map<int, std::vector<int>> adj_list;


int furthest_node = -1;
int best_distance = -1;
void dfs(int node, int prev, int distance)
{
    for (auto neighbor : adj_list[node])
    {
        if (neighbor != prev)
            dfs(neighbor, node, distance + 1);
    }
    if (distance > best_distance)
    {
        furthest_node = node;
        best_distance = distance;
    }
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

    dfs(0, -1, 0);
        std::cout << "furthest_node: " << furthest_node << "\n";
    dfs(furthest_node, -1, 0);

    std::cout << "Diameter: " << best_distance << "\n";
}




