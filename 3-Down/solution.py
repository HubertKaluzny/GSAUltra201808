def solution(s):
    minScore = pow(2, len(s))
    for a in range(0, len(s)):
        for b in range(a + 1, len(s)):
            for c in range(b + 1, len(s)):
                groups = []
                groups.append(s[:a])
                groups.append(s[a:b])
                groups.append(s[b:c])
                groups.append(s[c:])

                if '' in groups:
                    continue

                score = 0
                for g in groups:
                    score += longestPalindrome(g)

                if score < minScore:
                    minScore = score
    return minScore

def longestPalindrome(s):
    charSet = list(set(s))

    palindromeLength = 0
    hasMiddle = False

    for char in charSet:
        count = s.count(char)
        while count > 3:
            palindromeLength += 2
            count -= 2

        if count == 1 and not hasMiddle:
            palindromeLength += 1
            hasMiddle = True

        if count == 2:
            palindromeLength += 2
        elif count == 3:
            if hasMiddle:
                palindromeLength += 2
            else:
                hasMiddle = True
                palindromeLength += 3


    return palindromeLength
