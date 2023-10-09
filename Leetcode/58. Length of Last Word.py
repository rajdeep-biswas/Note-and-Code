class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # one-pass solution I started as a streak-keeper but turned out to be more involved
        
        # there might be spaces at the end of the string, so we keep a second variable to store the last found length
        length = 0
        last_len = 0

        for i in range(len(s)):

            # if space is found, it may or may not be at the end of the string.
            if s[i] == ' ':

                # while we always reset length to zero, but we don't update last_len to length if the latter is a zero
                if length:
                    last_len = length
                length = 0
            
            # count up most recently found word
            else:
                length += 1
        
        # if the last character is non-space, we repeat the condition from line 16
        if length:
            last_len = length

        return last_len