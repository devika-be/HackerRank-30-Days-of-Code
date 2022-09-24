#Problem Link: https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

#Ans:

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

for _ in range(N):
    listChars = [char for char in input()]
    word_1 = ""
    word_2 = ""
    check = True

    for i in range(len(listChars)):
        if check:
            word_1 += listChars[i]
        else:
            word_2 += listChars[i]
        check = not check

    print(word_1, word_2)
