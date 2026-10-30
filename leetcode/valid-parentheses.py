class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        match = {
            '}': "{",
            ")": "(",
            "]": "["
        }
        open = ['(', '[', '{'] 
        close = [')', ']', '}']

        for ch in s:
            if ch in open:
                seen.append(ch)
            elif ch in close:
                if not seen or seen[-1] != match[ch]:
                    return False
                seen.pop()
        return True if not seen else False

test1 = Solution()
test2 = Solution()
test3 = Solution()
test4 = Solution()
test5 = Solution()
print(test1.isValid('()'))
print(test2.isValid('()[]{}'))
print(test3.isValid('(]'))
print(test4.isValid('([])'))
print(test5.isValid('([)]'))