'''
https://programmers.co.kr/learn/courses/30/lessons/42839

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers     return
"17"        3
"011"       2

입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
'''


from itertools import permutations
import math

def prime_number(n):
    num = math.sqrt(n)
    if n < 2:
        return False
    for k in range(2, int(num)+1):
        if n % k == 0:
            return False
    return True
    

def solution(numbers):
    answer = []
    for i in range(1 ,len(numbers)+1):
        lst = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(lst)):
            if prime_number(int(j)):
                answer.append(int(j))
    return len(set(answer))


'''
풀이
우선 뽑은 카드로 배열을 만드는 permutations(조합)을 이용함
조합되는 숫자의 개수를 정해서 permutations 두번째 인자에 넣음
map으로 string을 합치고 list로 만듦
조합한 숫자의 앞자리가 0인 str를 set을 사용해 int로 바꾸면 없어짐
list 내의 공통 str를 set으로 단일화 시켜서 다시 list로 만듦
true가 나오면 j를 answer list에 포함시킴
'''