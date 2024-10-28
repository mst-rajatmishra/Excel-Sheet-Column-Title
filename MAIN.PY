class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based index
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result  # Get the character and prepend
            columnNumber //= 26  # Move to the next "digit"
        
        return result

# Example usage:
# sol = Solution()
# print(sol.convertToTitle(1))    # Output: "A"
# print(sol.convertToTitle(28))   # Output: "AB"
# print(sol.convertToTitle(701))  # Output: "ZY"
