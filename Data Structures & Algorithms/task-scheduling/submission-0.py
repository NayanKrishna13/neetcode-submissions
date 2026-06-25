class Solution:
    from collections import Counter
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequencies = Counter(tasks)
        
        f_max = max(frequencies.values())
        count_max = sum(1 for count in frequencies.values() if count == f_max)
        return max(len(tasks), (f_max - 1) * (n + 1) + count_max)  