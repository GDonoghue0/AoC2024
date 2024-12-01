#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <utility>

class Solution {
private:
    std::string input_file;

public:
    Solution(const std::string& file = "input1.txt") : input_file(file) {}

    std::pair<std::vector<int>, std::vector<int> > read_input() {
        std::ifstream file(input_file);
        std::vector<int> list1, list2;

        if (file.is_open()) {
            int a, b;
            while (file >> a >> b) {
                list1.push_back(a);
                list2.push_back(b);
            }
            file.close();
        }
        return std::make_pair(list1, list2);
    }

    int get_distance() {
        std::pair<std::vector<int>, std::vector<int> > data = read_input();
        std::vector<int>& list1 = data.first;
        std::vector<int>& list2 = data.second;

        std::sort(list1.begin(), list1.end());
        std::sort(list2.begin(), list2.end());

        int distance = 0;
        for (size_t i = 0; i < list1.size(); ++i) {
            distance += std::abs(list1[i] - list2[i]);
        }

        return distance;
    }
};

int main() {
    Solution solution("input1.txt");
    std::cout << "Total Distance: " << solution.get_distance() << std::endl;
    return 0;
}
