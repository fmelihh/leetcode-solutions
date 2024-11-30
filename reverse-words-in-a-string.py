# Problem Url: https://leetcode.com/problems/reverse-words-in-a-string, Medium


class Solution:
    def reverseWords(self, s: str) -> str:
        end_pointer = 0
        start_pointer = 0
        cum_index = 0
        while start_pointer < len(s) and s[start_pointer] != '|':
            if s[start_pointer].isalnum():
                for i in range(start_pointer, len(s)):
                    if s[i].isalnum():
                        end_pointer = i
                    else:
                        break

                if end_pointer < start_pointer:
                    break

                new_start_pointer = len(s[start_pointer : end_pointer+1]) + 1
                s = s[start_pointer : end_pointer+1] + "|" + s[0:start_pointer] + s[end_pointer + 1:]

                end_pointer = 0
                cum_index += new_start_pointer
                start_pointer = cum_index

            start_pointer += 1

        return " ".join(" ".join(s.split("|")).split())


if __name__ == "__main__":
    s = Solution()
    s.reverseWords("the sky is blue")  # "blue is sky the"
    s.reverseWords("  hello world  ")  # "world hello"
    s.reverseWords("a good   example")  # "example good a"
