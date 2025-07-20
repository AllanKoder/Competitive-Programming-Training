#include <iostream>
#include <array>
#include <vector>
#include <string>
#include <algorithm>

#include <stdio.h>


template <typename T>
class FenwickTree
{
public:
    std::vector<T> tree;

    FenwickTree(const std::vector<T>& values)
    {
        tree.assign(values.begin(), values.end());
        for (size_t i = 0; i < tree.size(); ++i)
        {   
            size_t one_indexed = i+1;
            size_t parent = one_indexed + (one_indexed & -one_indexed);
            if (parent <= tree.size())
            {
                tree[parent - 1] += tree[i];
            }
        }
    }

    friend std::ostream& operator<<(std::ostream& out, const FenwickTree<T>& ft)
    {
        for (auto v : ft.tree)
        {
            out << v << " ";
        }
        return out;
    }

    void add(size_t index, int amount)
    {
        size_t one_indexed = index + 1;
        while (one_indexed <= tree.size())
        {
            tree[one_indexed-1] += amount;
            one_indexed += (one_indexed & -one_indexed);
        }
    }

    int sum(size_t up_to)
    {
        size_t one_indexed = up_to + 1;
        int output = 0;
        while (one_indexed >= 1)
        {
            output += tree[one_indexed-1];
            one_indexed -= (one_indexed & -one_indexed);
        }
        return output;
    }
};

int main()
{
    std::vector<int> arr{1,2,3,4,5,6,7};
    FenwickTree<int> tree(arr);

    std::cout << tree << "\n";
    tree.add(0, 1);
    std::cout << tree << "\n";

    std::cout << tree.sum(3) << "\n";
    std::cout << tree.sum(5) << "\n";
    tree.add(0, 1);
    std::cout << tree.sum(6) << "\n";
}