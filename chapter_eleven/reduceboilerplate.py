from collections import defaultdict


class StatsList(list):

    def mean(self):
        return sum(self) / len(self)

    def median(self):
        sorted_list = sorted(self)
        mid = len(sorted_list) // 2

        if len(sorted_list) % 2 == 0:
            return (sorted_list[mid] + sorted_list[mid - 1]) / 2
        else:
            return sorted_list[mid]

    # def mode(self):
    #     frequency = defaultdict(int)
    #     for i in self:
    #         frequency[i] += 1
    #     frequency = dict(frequency)

    #     return sorted(frequency.items(), key=lambda x: x[1], reverse=True)[0][0]

    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
        mode_freq = max(freqs.values())
        modes = []
        for item, value in freqs.items():
            if value == mode_freq:
                modes.append(item)
        return modes
