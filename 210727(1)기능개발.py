'''
https://programmers.co.kr/learn/courses/30/lessons/42586

문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 
예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

입출력 예
progresses                  speeds                  return
[93, 30, 55]                [1, 30, 5]              [2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]      [1, 3, 2]

입출력 예 설명
입출력 예 #1
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 
하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

입출력 예 #2
모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 
어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.

따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.
'''


'''
해석

두번째 예시의 speeds는 1로 동일하므로 100-progresses를 해보면 각각
5, 10, 1, 1, 20, 1 이다
이는 배포까지 걸리는 일 수를 의미하고 앞의 수가 뒤의 수보다 작은 경우는 같이 배포할 수 없으므로 묶어보면
5 / 10, 1, 1 / 20, 1 형태이다
이를 progresses 값들로 다시 묶어보면
95 / 90, 99, 99 / 80, 99 이다
이는 각각 5일 / 10일 / 20일을 의미한다
5일 후에 1개, 10일 후에 3개, 20일 후에 2개를 배포한다
'''

# 답1
def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) > 0:
        if progresses[0] + speeds[0] * days >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
    answer.append(count)

    return answer



# 답2
def solution(progresses, speeds):
    Q=[]
    for progresses, speeds in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((progresses-100)//speeds):
            Q.append([-((progresses-100)//speeds),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


'''
풀이

# 답1
뒤에 있는 기능의 개발이 빨라도 앞에 있는 기능의 개발에 날짜를 맞춰 배포해야 한다
day는 하루하루 시간을 의미하고, count는 100% 개발이 완료된 기능의 개수를 세는 것이다
처음의 days와 count를 0으로 설정한다

# while len(progresses) > 0:
기능의 개수가 0보다 클 동안

# if progresses[0] + speeds[0] * days >= 100:
만약 (기능의 값 + 일 수 * 개발 속도)가 100보다 커지면

# progresses.pop(0)
기능을 빼내고

# speeds.pop(0)
개발 속도를 빼내고

# count += 1
count에 1을 더해준다

# else:
#   if count > 0:
기능의 개수가 0이 될 때, 만약 count가 0보다 크면

#  answer.append(count)
answer에 count를 쌓고

# count = 0
count를 0으로 초기화한다

# days += 1
일 수는 1일을 추가한다

# answer.append(count)
answer에 count를 쌓는다

'''