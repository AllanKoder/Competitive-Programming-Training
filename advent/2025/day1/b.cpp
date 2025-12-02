#include <bits/stdc++.h>
#define MAX_DIAL 100

int main() {
    int total = 0;
    int dial = 50;
    std::string in;
    while(std::cin >> in)
    {
        char letter = in[0];
        int val = std::stoi(in.substr(1));

        for (int i = 0; i < val; i++)
        {
            if (letter == 'L') dial -= 1;
            if (letter == 'R') dial += 1;

            dial = (dial % MAX_DIAL + MAX_DIAL) % MAX_DIAL;
            if (dial == 0) total += 1;
        }
    }
    std::cout << total << "\n";
}