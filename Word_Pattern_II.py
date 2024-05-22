"""
Example 1:
Input: pattern = "abab", str = "redblueredblue"
Output: true

Example 2:
Input: pattern = "aaaa", str = "asdasdasdasd"
Output: true

Example 3:
Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
"""


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        P = len(pattern)
        N = len(s)

        def canMatch(pindex, sindex, lookup, rlookup):
            if sindex == N and pindex == P:
                return True
            if sindex == N or pindex == P:
                return False

            if pattern[pindex] in lookup:
                m = lookup[pattern[pindex]]
                if s[sindex: sindex + len(m)] == m:
                    return canMatch(pindex + 1, sindex + len(m), lookup, rlookup)
                return False

            for end in range(sindex, N):
                m = s[sindex: end + 1]
                if m in rlookup:
                    continue

                lookup[pattern[pindex]] = m
                rlookup[m] = pattern[pindex]

                if canMatch(pindex + 1, end + 1, lookup, rlookup):
                    return True

                del lookup[pattern[pindex]]
                del rlookup[m]

            return False

        return canMatch(0, 0, {}, {})


def main():
    solution = Solution()
    pattern = input("Enter the pattern: ")
    s = input("Enter the string: ")
    result = solution.wordPatternMatch(pattern, s)
    print(f"Pattern matches the string: {result}")


if __name__ == "__main__":
    main()
