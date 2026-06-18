import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Step 1: Quick safety check
        if len(hand) % groupSize != 0:
            return False
        
        # Step 2: Build frequency map
        count_map = Counter(hand)
        
        # Step 3: Push all unique cards into a Min-Heap
        min_heap = list(count_map.keys())
        heapq.heapify(min_heap)
        
        # Step 4: Process the cards starting from the smallest
        while min_heap:
            smallest_card = min_heap[0] # Look at the smallest card
            
            # If this card has already been completely used up by previous groups, skip it
            if count_map[smallest_card] == 0:
                heapq.heappop(min_heap)
                continue
                
            # Form a group of 'groupSize' starting from this smallest card
            for i in range(groupSize):
                current_card = smallest_card + i
                
                # If a consecutive card doesn't exist or is used up, we can't form a straight
                if count_map[current_card] == 0:
                    return False
                
                # Consume one copy of this card
                count_map[current_card] -= 1
                
        return True