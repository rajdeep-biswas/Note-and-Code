class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        t_count = {}
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)
        
        l, r = 0, len(t)
        min_win = ''

        while r < len(s) + 1:
            s_count = {}
            for i in range(l, r):
                s_count[s[i]] = 1 + s_count.get(s[i], 0)
            flag = True
            for t in t_count:
                if t in s_count:
                    if s_count[t] < t_count[t]:
                        flag = False
                else:
                    flag = False
            # print(s[l:r], flag, t_count, s_count)
            if flag:
                if len(s[l:r]) < len(min_win) or not min_win:
                    min_win = s[l:r]
                l += 1
            else:
                r += 1

        return min_win