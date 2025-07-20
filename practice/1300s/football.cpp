#include <string>
#include <iostream>


void valid(std::string& input)
{
    int counter_1 = 0;
    int counter_0 = 0;
    for(int i = 0; i < input.size(); i++)
    {
        if (input[i] == '0')
        {
            counter_1 = 0;
            counter_0 += 1;
        }
        else
        {
            counter_1 += 1;
            counter_0 = 0;
        }

        if (counter_1 >= 7 || counter_0 >= 7)
        {
            std::cout << "YES";
            return;
        }
    }
    std::cout << "NO";
}

int main()
{
    std::string input;
    std::cin >> input;
    valid(input);
}
