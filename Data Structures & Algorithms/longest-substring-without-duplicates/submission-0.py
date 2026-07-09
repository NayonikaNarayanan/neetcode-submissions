class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()      
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left +=1
                #left is original element + 1 th position, and right is where the 
                #"duplicate" was, and now we continue forward
            
            window.add(s[right])
            max_len = max(max_len, right-left+1)
        
        return max_len
