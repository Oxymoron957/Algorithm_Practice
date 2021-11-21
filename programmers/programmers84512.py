"""
모음 사전
https://programmers.co.kr/learn/courses/30/lessons/84512
"""

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    size = len(vowels)

    # Create dictionary
    dictionary = dict()
    num = 0
    for i in range(size):
        dictionary[vowels[i]] = num
        num += 1
        for j in range(size):
            dictionary[vowels[i]+vowels[j]] = num
            num += 1
            for k in range(size):
                dictionary[vowels[i]+vowels[j]+vowels[k]] = num
                num += 1
                for e in range(size):
                    dictionary[vowels[i]+vowels[j]+vowels[k]+vowels[e]] = num
                    num += 1
                    for t in range(size):
                        dictionary[vowels[i]+vowels[j]+vowels[k]+vowels[e]+vowels[t]] = num
                        num += 1

    return dictionary[word]+1