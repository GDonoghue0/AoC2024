from collections import Counter

class Solution:
    def read_input(self):
        with open("input1.txt", "r") as file:
            list1, list2 = zip(*(map(int, line.split()) for line in file))
        return list(list1), list(list2)

    def get_distance(self):
        data1, data2 = self.read_input()
        data1.sort()
        data2.sort()

        return sum(abs(a - b) for a, b in zip(data1, data2))

    def get_similarity(self):
        data1, data2 = self.read_input()
        data2_counts = Counter(data2)
        print(data2_counts)

        similarity = 0
        for i in range(len(data1)):
            similarity += data1[i] * data2_counts[data1[i]]
        return similarity


print(Solution().get_distance())
print(Solution().get_similarity())