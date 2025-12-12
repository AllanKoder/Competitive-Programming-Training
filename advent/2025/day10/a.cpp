#include <bits/stdc++.h>

struct ButtonMachine
{
    std::string target;
    std::vector<std::vector<int>> buttons_toggles;
    std::vector<int> joltage_requirements;
};


std::vector<std::vector<int>> raw_string_to_buttons(const std::string& string_input)
{
    std::vector<std::vector<int>> output;
    
    std::function<std::vector<int>(std::string s)> string_to_nums = [](std::string s)
    {
        std::vector<int> output;
        std::stringstream ss(s);
        std::string string_digit;
        while (getline(ss, string_digit, ','))
        {
            // std::cout << "stoi: " << string_digit;
            int value = std::stoi(string_digit);
            output.push_back(value);
        }
        return output;
    };

    std::stringstream ss(string_input);
    std::string s;
    while (std::getline(ss, s, ' '))
    {
        size_t start = s.find('(');
        size_t end = s.find(')');
        std::string coord_string = s.substr(start + 1, end - start - 1);
        output.push_back(string_to_nums(coord_string));
    }

    return output;
}

std::vector<int> raw_string_to_joltage(const std::string& string_input)
{
    std::vector<int> output;
    
    size_t start = string_input.find('{');
    size_t end = string_input.find('}');

    std::stringstream ss(string_input.substr(start+1, end - start - 1));
    std::string s;
    while (std::getline(ss, s, ','))
    {
        output.push_back(std::stoi(s));
    }

    return output;
}



std::vector<ButtonMachine> raw_input_to_machines(const std::vector<std::string>& raw_strings)
{
    std::vector<ButtonMachine> machines;
    for (int i = 0; i < raw_strings.size(); i++)
    {
        ButtonMachine machine;
        std::string s = raw_strings[i];
        // std::cout << "inital: " << s << "\n";
        // First, get the initial state
        int ending_i_1 = s.find(']');
        machine.target = s.substr(1, ending_i_1-1);
        // std::cout << machine.target << "\n";
        // Then, get the buttons
        int ending_i_2 = s.find('{')-1;
        int i_2_length = ending_i_2 - (ending_i_1 + 1);
        std::string raw_buttons = s.substr(ending_i_1+1, i_2_length);
        machine.buttons_toggles = raw_string_to_buttons(raw_buttons);

        // for (auto v: machine.buttons_toggles)
        // {
        //     std::cout << "(";
        //     for (auto b : v)
        //     {
        //         std::cout << b << ",";
        //     }
        //     std::cout << ")\n";
        // }
        // std::cout << "\n";
        // Finally, get the joltage requirements

        std::string raw_joltage = s.substr(ending_i_2);
        machine.joltage_requirements = raw_string_to_joltage(raw_joltage);

        // for (auto c: machine.joltage_requirements)
        // {
        //     std::cout << "requirement: " << c << "\n";
        // }

        machines.push_back(machine);
    }

    return machines;
}


struct BFS
{
    int move;
    std::string state;
};

std::string apply_buttons_toggle(const std::string& state, std::vector<int> button_toggles)
{
    std::string output(state);

    for (auto index : button_toggles)
    {
        if (output[index] == '.') 
        {
            output[index] = '#';
        }
        else
        {
            output[index] = '.';
        }
    }
    return output;
}

int min_moves_to_fix_machine(const ButtonMachine& machine)
{
    std::queue<BFS> queue;
    std::set<std::string> visited;

    BFS initial_state;
    initial_state.move = 0;
    std::string inital(machine.target.size(), '.');
    initial_state.state = inital;

    queue.push(initial_state);

    while (queue.size())
    {
        BFS state = queue.front();
        queue.pop();

        if (machine.target.compare(state.state) == 0)
        {
            return state.move;
        }

        if (visited.count(state.state))
        {
            continue;
        }
        visited.insert(state.state);

        for (auto buttons : machine.buttons_toggles)
        {
            BFS new_state;
            new_state.move = state.move + 1;
            // std::cout << "before: " << state.state << "\n";
            new_state.state = apply_buttons_toggle(state.state, buttons);
            // std::cout << "after: " << new_state.state << "\n";
            queue.push(new_state);
        }
    }

    return -1;
}

int main()
{
    std::string s;
    std::vector<std::string> raw_inputs;
    while(std::getline(std::cin, s))
    {
        raw_inputs.push_back(s);
    }

    std::vector<ButtonMachine> machines = raw_input_to_machines(raw_inputs);

    int total_moves = 0;

    for (auto m: machines)
    {
        int moves = min_moves_to_fix_machine(m);
        std::cout << "Machine moves: " << moves << "\n";
        total_moves += moves;
    }

    std::cout << "Answer: " << total_moves<< "\n";
}