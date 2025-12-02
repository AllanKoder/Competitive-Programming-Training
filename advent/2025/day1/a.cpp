#include <bits/stdc++.h>
#define MAX_DIAL 100

int main() {
    int total = 0;
    int dial = 50;
    while(1)
    {
        std::string in;
        std::cin >> in;
        if (in == "") break;
        
        char letter = in[0];
        int val = std::stoi(in.substr(1));

        if (letter == 'L')
        {
            dial -= val;
        }
        else
        {
            dial += val;
        }
        
        dial = (dial % MAX_DIAL + MAX_DIAL) % MAX_DIAL;
        total += (dial == 0) ? 1 : 0;
    }
    std::cout << total << "\n";
}