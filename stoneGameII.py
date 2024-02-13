class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def minimax(start, M, isAlice):
            if start >= len(piles):
                return 0

            max_stones = float("-inf") if isAlice else float("inf")
            end = min(start + 2 * M, len(piles))

            for i in range(start, end):
                stones_taken = sum(piles[start : i + 1])
                M = max(M, i - start + 1)

                if isAlice:
                    max_stones = max(
                        max_stones, stones_taken + minimax(i + 1, M, False)
                    )
                else:
                    max_stones = min(max_stones, minimax(i + 1, M, True))

            return max_stones

        return minimax(0, 1, True)
