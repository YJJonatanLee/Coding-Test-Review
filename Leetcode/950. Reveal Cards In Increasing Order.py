class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        answer_deck_deque = deque()

        answer_deck_deque.append(sorted_deck.pop())

        while sorted_deck:
            answer_deck_deque.appendleft(answer_deck_deque.pop())
            answer_deck_deque.appendleft(sorted_deck.pop())

        return answer_deck_deque
        
