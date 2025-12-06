#include <bits/stdc++.h>

using ull = unsigned long long; 

// I hated this one btw

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

void pad_right(std::string& s, size_t desired_length)
{
    s.append(desired_length - s.size(), ' ');
}

int main() 
{
    std::vector<std::string> raw_input;

    std::string s;
    while(std::getline(std::cin, s))
    {
        raw_input.push_back(s);
    }

    std::vector<std::vector<ull>> num_rows;
    size_t row_index;
    for (int i = 0; i < raw_input.size()-1; i++)
    {
        std::string s = raw_input[i];

        std::vector<ull> row;
        std::stringstream ss(s);
        std::string num;
        while(std::getline(ss, num, ' '))
        {
            if (num == "") continue;
            row.push_back(std::stoull(num));
        }
        num_rows.push_back(row);
    }

    std::vector<std::string> operations;
    std::stringstream ss(raw_input.back());
    while(std::getline(ss, s, ' '))
    {
        if (s == "") continue;
        operations.push_back(s);
    }
    
    std::vector<size_t> max_sizes_per_col;
    for (int i = 0; i < num_rows[0].size(); i++)
    {
        size_t biggest_size = 0;
        for (int j = 0; j < num_rows.size(); j++)
        {
            biggest_size = std::max(biggest_size, std::to_string(num_rows[j][i]).size());
        }
        max_sizes_per_col.push_back(biggest_size);
    }
    
    // The starting index for each of the rows for a numb character
    std::vector<size_t> col_string_start_index(max_sizes_per_col.size(), 0);
    col_string_start_index[0] = 0;
    for (int i = 1; i < max_sizes_per_col.size(); i++)
    {
        col_string_start_index[i] = max_sizes_per_col[i-1] + col_string_start_index[i-1] + 1;
    }

    std::vector<std::vector<ull>> final_cols;
    for (int col_i = 0; col_i < num_rows[0].size(); col_i++)
    {
        std::vector<ull> values;
        for (int num_i = 0; num_i < max_sizes_per_col[col_i]; num_i++)
        {
            // Now handle attaining the number!
            std::string s = "";
            size_t character_i = num_i + col_string_start_index[col_i];
            // Loop downwards to build the string to append
            for(int row_i = 0; row_i < num_rows.size(); row_i++)
            {
                s += raw_input[row_i][character_i];
            }

            // std::cout << ", col: " << col_i << ", starting: " 
            //     << col_string_start_index[col_i] << ", value: " << s 
            //     << ", max_size:" << max_sizes_per_col[col_i] << "\n"; 
            ull value = std::stoull(s);
            values.push_back(value);
        }
        final_cols.push_back(values);
    }

    ull total = 0;
    for (int col_i = 0; col_i < final_cols.size(); col_i++)
    {
        ull result = accumulate_col<ull>(final_cols[col_i], operations[col_i]);
        // std::cout << result << " \n";
        total += result;
    }

    std::cout << "Answer: " << total << "\n";

    // std::cout << std::stoull("   4") << "\n";
    // std::cout << "\nmatrix:\n";
    // for(auto c: final_cols)
    // {
    //     for (auto i : c)
    //     {
    //         std::cout << i  << " ";
    //     }
    //     std::cout << "\n";
    // }


    // for(auto c: max_sizes_per_col)
    // {
    //     std::cout << c << " ";
    // }
}