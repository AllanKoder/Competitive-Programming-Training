#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    double pupils, distance, people_speed, bus_speed, capacity;
    cin >> pupils >> distance >> people_speed >> bus_speed >> capacity;
        
    std::function<double(double, ll)> time;
    time = [&](double remaining_dist, ll remaining_pupils)
    {
        if (remaining_pupils <= 0) return 0.0;

        remaining_pupils -= capacity;
        double bus_there_time = remaining_dist / (double)bus_speed;

        if (remaining_pupils <= 0) return bus_there_time;

        double people_remaining_dist = remaining_dist - bus_there_time*(double)people_speed;

        double bus_back_time = people_remaining_dist / (double)(people_speed + bus_speed);
        
        double new_remaining_dist = people_remaining_dist - bus_back_time*(double)people_speed;

        return time(new_remaining_dist, remaining_pupils) + bus_there_time + bus_back_time;
    };

    cout << time(distance, pupils) << endl;
}

