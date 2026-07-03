from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Edge case: If the destination isn't even in the word list, it's impossible
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        L = len(beginWord)
        
        # Step 1: Pre-process graph using intermediate patterns
        wordict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "_" + word[i+1:]
                wordict[pattern].append(word)
                
        # Step 2: Initialize BFS structures
        # We store tuples of (word, current_sequence_length)
        q = deque([(beginWord, 1)])
        
        # Use a set for O(1) lookups to track visited words
        visited = {beginWord}
        
        # Step 3: Standard BFS
        while q:
            current_word, steps = q.popleft()
            
            # Generate patterns for the current word
            for i in range(L):
                pattern = current_word[:i] + "_" + current_word[i+1:]
                
                # Check all words that share this matching pattern
                for neighbor in wordict[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                        
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, steps + 1))
                        
                # OPTIMIZATION: Clear the list of neighbors for this pattern once visited 
                # to prevent other paths from processing these same nodes again.
                wordict[pattern] = []
                
        return 0