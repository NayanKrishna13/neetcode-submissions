class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        length = len(word)
        
        # Optimization 1: Frequency pruning (Saves massive time on impossible words)
        # If the board doesn't even contain enough of the required characters, fail early.
        board_counts = collections.Counter(char for row in board for char in row)
        word_counts = collections.Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
                
        def backtrack(x, y, k):
            # Base Case: Successfully matched the entire word
            if k == length:
                return True
                
            # Boundary and mismatch checks
            if not (0 <= x < n) or not (0 <= y < m) or board[x][y] != word[k]:
                return False
            
            # Step 1: Mark as visited by modifying the board in-place
            temp = board[x][y]
            board[x][y] = '#'
            
            # Step 2: Explore all 4 directions (Up, Down, Left, Right)
            # Short-circuiting with 'or' means it stops exploring the moment it finds a match
            found = (backtrack(x + 1, y, k + 1) or 
                     backtrack(x - 1, y, k + 1) or 
                     backtrack(x, y + 1, k + 1) or 
                     backtrack(x, y - 1, k + 1))
            
            # Step 3: Backtrack and restore the original character
            board[x][y] = temp
            
            return found

        # Start the search from every cell that matches the first letter
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
                        
        return False