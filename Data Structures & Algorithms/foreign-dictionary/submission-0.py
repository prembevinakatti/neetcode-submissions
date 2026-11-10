from typing import List
from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for a, b in zip(w1, w2):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break

        queue = deque([char for char in indegree if indegree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(indegree):
            return ""

        return "".join(result)