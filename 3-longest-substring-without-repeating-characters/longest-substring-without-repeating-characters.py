class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_sol = ''
        max_sol = temp_sol
        
        for char in s:
            if char in temp_sol:
                temp_sol = temp_sol[temp_sol.index(char) + 1:]
            
            temp_sol += char  
            max_sol = temp_sol if len(temp_sol) > len(max_sol) else max_sol
        
        return len(max_sol)