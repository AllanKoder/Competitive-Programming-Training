#include <vector>
#include <iostream>

/*
4 4
0 1
1 2
2 3
3 0

4 3
0 1
1 2
2 3


5 6
1 2
1 3
2 3
2 4
3 5
4 5
*/
int main()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> adj_list(n);

    for(int i = 0; i < m; i++)
    {
        int e1, e2;
        std::cin >> e1 >> e2;
        adj_list[e1].push_back(e2);
        adj_list[e2].push_back(e1);
    }

    // Find the shortest distance from node x to node y
    std::cout << "-----\n";
    for (auto v : adj_list)
    {
        for (auto e : v)
        {
            std::cout << e << " ";
        }
        std::cout << "\n";
    }

    // 0 is always the start
    // N is the end
    size_t ending_node = n - 1;
    std::vector<int> distances(n, INT_MAX);
    distances[0] = 0;

    for (size_t i = 0; i < n-1; i++)
    {
        // For all the edges of a node, improve the distance 
        for (size_t j : adj_list[i])
        {
            if (distances[i] == INT_MAX) continue;
            distances[j] = std::min(distances[i] + 1, distances[j]);
        }
    }
    
    std::cout << "shortest distance: " << distances[ending_node] << "\n";
}