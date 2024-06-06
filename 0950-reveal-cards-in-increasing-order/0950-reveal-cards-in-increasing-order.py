from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Step 1: Sort the deck
        sorted_deck = sorted(deck)
        
        # Step 2: Initialize deque with indices
        index_deque = deque(range(len(deck)))
        
        # Step 3: Create an array to hold the result
        result = [0] * len(deck)
        
        # Step 4: Place cards into the result array
        for card in sorted_deck:
            # Place the current smallest card in the position indicated by the front of the deque
            result[index_deque.popleft()] = card
            if index_deque:
                # Move the next index to the back of the deque
                index_deque.append(index_deque.popleft())
        
        return result

        