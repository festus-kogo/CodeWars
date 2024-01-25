# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    # your code
    if strarr == "" or k < 1 or k > len(strarr):
        return ""
    
    elif k == 1:
        max_str = ""
        max_len = 0

        for i, l in enumerate(strarr):
            # print(f"at index {i} is {l} and length is {len(l)}")
            if len(l) > max_len:
                max_str = l
                max_len = len(l)
        return max_str
    
    else:
        strarr1 = []

        for i in range(len(strarr) - 1):
            strarr1.append(''.join(strarr[i:i + k]))
        max_str1 = ""
        max_len1 = 0

        for l1 in strarr1:
            # print(f"at index {i1} is {l1} and length is {len(l1)}")
            if len(l1) > max_len1:
                max_str1 = l1
                max_len1 = len(l1)
        return max_str1

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))