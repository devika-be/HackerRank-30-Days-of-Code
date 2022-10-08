#Problem Link : https://www.hackerrank.com/challenges/30-more-exceptions/problem?isFullScreen=true

#Ans:

#Write your code here

class Calculator:
    def power(self, n, p):
        '''Checks whether n or p are negative'''
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
