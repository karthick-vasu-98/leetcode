'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def longest_sub_str_without_char_repeat(s):
    output = ''
    str_list = list()
    try:
        if len(s) == 1:
            return 1
        
        if len(s) == 2:
            if s[0] == s[1]:
                return 0
            else:
                return 2
        
        for i in range(0, len(s)):
            sub_str = s[i]
            for j in range(1, len(s)):
                if s[j] not in sub_str:
                    sub_str += s[j]
                else:
                    print('sub_str :', sub_str)
                    break
            str_list.append(len(sub_str))
    except Exception as e:
        print('Error :', e)
    return max(str_list)

s = "pwwkew"
print(longest_sub_str_without_char_repeat(s))