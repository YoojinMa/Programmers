'''
https://programmers.co.kr/learn/courses/30/lessons/42584

문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices	            return
[1, 2, 3, 2, 3]	    [4, 3, 1, 1, 0]

입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
'''


'''
해석

prices 값이 5개 있고, 5초의 시간이다
각 가격의 위치는 시간을 나타낸다
첫번째 price는 1초 시점의 가격이고 그 값은 ₩1이다
두번째 price는 2초 시점의 가격이고 그 값은 ₩2이다
세번째 price는 3초 시점의 가격이고 그 값은 ₩3이다
네번째 price는 4초 시점의 가격이고 그 값은 ₩2이다
다섯번째 price는 5초 시점의 가격이고 그 값은 ₩3이다

return값은 각 초의 price 값이 떨어지지 않은 초를 의미한다
첫번째 return은 첫번째 price 값 ₩1이 4초 동안 가격이 떨어지지 않았다는 의미이다
두번째 return은 두번째 price 값 ₩2이 3초 동안 가격이 떨어지지 않았다는 의미이다
세번째 return은 세번째 price 값 ₩3이 1초 동안 가격이 떨어지지 않았다는 의미이다
네번째 return은 네번째 price 값 ₩2이 1초 동안 가격이 떨어지지 않았다는 의미이다
다섯번째 return은 다섯번째 price 값 ₩3이 0초 동안 가격이 떨어지지 않았다는 의미이다

총 5초의 시간이므로 마지막 return 값은 항상 0이다
가격보다는 가격이 감소하는 시점이 중요하다
다음 순서에 가격이 떨어져도 1초간은 가격이 떨어지지 않은 것이다
'''

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
        
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer


'''
풀이

처음 price를 stack에 쌓고 다음 price가 더 크면 쌓고, 작으면 pop으로 뺀다
빠진 값은 price가 떨어지는 시점을 의미한다

answer는 몇초 후 가격이 떨어지는지 저장하는 배열이다
stack은 price의 [인덱스]를 차례로 담아두는 배열이다

# answer = [0] * len(prices)
answer=[0]*개수 : 개수만큼 0으로 초기화된 리스트 생성한다

# for i in range(len(prices)):
for문에서 i의 범위를 prices 길이만큼 정한다

# prices[stack[-1]] > prices[i]:
stack의 가장 위에 있는 값을 인덱스로 갖는 price 값이 i를 인덱스로 갖는 price 값보다 클 때

# top = stack.pop()
stack에 현재 있는 값을 pop으로 빼서 top에 넣는다

# answer[top] = i - top
그 top에 해당하는 answer를 구한다

# stack.append(i)
stack에는 계속 i를 쌓는다

# while stack:
for문이 실행된 후의 stack에서

# top = stack.pop()
stack에 남아있는 값들을 위에서부터 하나씩 빼서 top에 넣는다 

# answer[top] = len(prices) - 1 - top
그 top에 해당하는 answer를 구한다

'''
