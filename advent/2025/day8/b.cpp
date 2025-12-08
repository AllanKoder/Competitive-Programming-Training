#include <bits/stdc++.h>

using ull = unsigned long long;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::vector<int> vi;

struct UnionFind {
vi e; std::vector<pii> st;
    UnionFind(int n) : e(n, -1) {}
    int size(int x) { return -e[find(x)]; }
    int find(int x) { return e[x] < 0 ? x : find(e[x]); }
    int time() { return sz(st); }
    void rollback(int t) {
    for (int i = time(); i --> t;)
    e[st[i].first] = st[i].second;
    st.resize(t);
    }
    bool join(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (e[a] > e[b]) std::swap(a, b);
    st.push_back({a, e[a]});
    st.push_back({b, e[b]});
    e[a] += e[b]; e[b] = a;
    return true;
}
};

struct Point
{
    int id;
    ull x;
    ull y;
    ull z;

    double distance(const Point& other) const
    {
        long long dx = (long long)x - (long long)other.x;
        long long dy = (long long)y - (long long)other.y;
        long long dz = (long long)z - (long long)other.z;

        return std::sqrt(dx*dx + dy*dy + dz*dz);
    }
    bool operator<(const Point& other) const
    {
        return id < other.id;
    }
};

struct DistancePoint
{
    double distance;
    Point p1;
    Point p2;

    DistancePoint(const Point& arg_p1, const Point& arg_p2)
        : distance(arg_p1.distance(arg_p2)),
          p1(arg_p1),
          p2(arg_p2)
    {}

    bool operator<(const DistancePoint& other) const
    {
        return distance < other.distance;
    }
};


std::vector<Point> raw_to_points(const std::vector<std::string>& raw)
{
    std::vector<Point> points;
    for (int i = 0; i < raw.size(); i++)
    {
        Point p;
        p.id = i;
        
        std::stringstream ss(raw[i]);
        std::string string_digit;

        std::getline(ss, string_digit, ',');
        p.x = std::stoull(string_digit);

        std::getline(ss, string_digit, ',');
        p.y = std::stoull(string_digit);

        std::getline(ss, string_digit, ',');
        p.z = std::stoull(string_digit);
        // std::cout << p.id << " " << p.x << " " << p.y << " " << p.z << "\n";

        points.push_back(p);
    }
    return points;
}

std::vector<DistancePoint> get_shortest_pairs(const std::vector<Point>& points)
{
    std::vector<DistancePoint> distances;
    for (int i = 0; i < points.size(); i++)
    {
        auto candidate1 = points[i];
        for (int j = i+1; j < points.size(); j++)
        {
            auto candidate2 = points[j];
            DistancePoint result(candidate1, candidate2);
            distances.push_back(result);
        }
    }

    std::sort(distances.begin(), distances.end());
    
    // for (auto c: top_k)
    // {
    //     std::cout << c.distance << " " << c.p1.id << " " << c.p2.id << "\n";
    // }
    // std::cout << "\n";
    return distances;
}

std::pair<Point, Point> last_pair_until_circuit_groups(const std::vector<Point>& points, const std::vector<DistancePoint>& point_pairs)
{
    // Collect all unique points involved
    UnionFind uf(points.size());
    ull groups = points.size();

    int union_index = -1;
    while (groups > 1)
    {
        union_index++;
        auto point1 = point_pairs[union_index].p1;
        auto point2 = point_pairs[union_index].p2;
        if (uf.find(point1.id) != uf.find(point2.id))
        {
            groups--;
        }
        uf.join(point1.id, point2.id);
        // std::cout << groups << " " << union_index << "\n";
        // std::cout << "point id's: " << point1.id << " " << point2.id << "\n";
    }

    return {point_pairs[union_index].p1, point_pairs[union_index].p2};
}

int main() 
{
    std::vector<std::string> raw_input;
    std::string s;
    while(std::getline(std::cin, s))
    {
        raw_input.push_back(s);
    }

    std::vector<Point> points = raw_to_points(raw_input);
    std::vector<DistancePoint> shortest = get_shortest_pairs(points);
    std::pair<Point, Point> circuit_groups = last_pair_until_circuit_groups(points, shortest);

    ull answer = circuit_groups.first.x * circuit_groups.second.x;
    std::cout << "Answer: " << answer << "\n";
}