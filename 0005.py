# -------------------------------------------------------------------------------------------------------------
# 5. Longest Palindromic Substring
# -------------------------------------------------------------------------------------------------------------
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
# ------------------------------------------------------------------------------------------------------------

class Solution:

    def longestPalindrome(self, s):
        length = len(s)
        mlen = 1
        mi = 0
        flag = "odd"
        for i in range(length):
            ilen, tmp = self.expand_around_odd(s, i)
            if ilen > mlen:
                mlen = ilen
                mi = i
                flag = tmp
            ilen, tmp = self.expand_around_even(s, i)
            if ilen > mlen:
                mlen = ilen
                mi = i
                flag = tmp

        if flag == "odd":
            lf = mi - (mlen - 1) // 2
            rt = mi + (mlen - 1) // 2 + 1
        if flag == "even":
            lf = mi - mlen // 2 + 1
            rt = mi + mlen // 2 + 1
        return s[lf:rt]

    def expand_around_odd(self, s, i):
        length = len(s)
        lf, rt = i, i
        while lf >= 0 and rt < length and s[lf] == s[rt]:
            lf -= 1
            rt += 1
        return rt - lf - 1, "odd"

    def expand_around_even(self, s, i):
        length = len(s)
        lf, rt = i, i+1
        while lf >= 0 and rt < length and s[lf] == s[rt]:
            lf -= 1
            rt += 1
        return rt - lf - 1, "even"

if __name__ == "__main__":
    st = "abbc"
    s = Solution()
    print(s.longestPalindrome(st))