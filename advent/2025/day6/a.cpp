#include <bits/stdc++.h>

using ull = unsigned long long; 

template<typename T>
std::vector<std::vector<T>> get_transposed_matrix(const std::vector<std::vector<T>>& matrix)
{
    std::vector<std::vector<T>> result(matrix[0].size(), std::vector<T>(matrix.size(), 0));
    for (int i = 0; i < result.size(); i++)
    {
        for (int j = 0; j < result[i].size(); j++)
        {
            result[i][j] = matrix[j][i];
        }
    }
    return result;
}

template<typename T>
T accumulate_col(const std::vector<T>& vector, const std::string& oper)
{
    std::function<T(T,T)> add = [](T total, T other) { return total + other; };
    std::function<T(T,T)> mult = [](T total, T other) { return total * other; };

    std::function<T(T,T)> func;
    ull initial_val = 0;
    if (oper == "*") 
    {
        func = mult;
        initial_val = 1;
    }
    else if (oper == "+") 
    {
        func = add;
        initial_val = 0;
    }
    else
    {
        std::cout << "NO OPERATOR FOUND\n";
    }

    return std::accumulate(vector.begin(), vector.end(), initial_val, func);
}

int main() 
{
    std::vector<std::vector<ull>> rows;
    std::string s;
    size_t row_index;
    while (std::getline(std::cin, s))
    {
        if (s[0] == '*' || s[0] == '+') break;
        std::vector<ull> row;
        std::stringstream ss(s);
        std::string num;
        while(std::getline(ss, num, ' '))
        {
            if (num == "") continue;
            row.push_back(std::stoull(num));
        }
        rows.push_back(row);
    }
    std::vector<std::string> operations;
    std::stringstream ss(s);
    while(std::getline(ss, s, ' '))
    {
        if (s == "") continue;
        operations.push_back(s);
    }

    std::vector<std::vector<ull>> cols = get_transposed_matrix<ull>(rows);
    ull total = 0;
    for (int col_i = 0; col_i < cols.size(); col_i++)
    {
        ull result = accumulate_col<ull>(cols[col_i], operations[col_i]);
        std::cout << result << " \n";
        total += result;
    }

    std::cout << "Answer: " << total << "\n";

    // for(auto c: rows)
    // {
    //     for (auto i : c)
    //     {
    //         std::cout << i << " ";
    //     }
    //     std::cout << "\n";
    // }


}