'''
programmers_완주하지 못한 선수
해쉬를 사용해서 풀어야 하는 문제
zip, collections_Counter, 해시를 사용해 해결 가능
'''

import collections

def solutions(participant, completion):

    answer = ""

    # zip을 사용해 두 list간의 원소를 비교하려 하므로 정렬을 해줘야 한다
    '''
    participant.sort()
    completion.sort()

    # zip함수를 이용해 반복문에서 각 리스트를 튜플로 묶는다
    for part, comp in zip(participant, completion):
    
    # 중복에 의해 두 리스트의 원소가 다른경우 participant의 원소 리턴
        if part != comp :
            return part
   
    # 모든 원소가 같은경우 마지막 원소만 다르므로 participant의 마지막 원소 리턴
    return participant[-1]
    '''

    # Collections.Counter()를 사용한 코드
    '''
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

    Counter -> 컨테이너에서 동일한 값의 개수를 세는데 사용하는 객체
    list, dictionary, 값 = 개수(a=2, b=3, c=3...등), 문자열을 입력으로 받는다
    
    메소드로는 update(), elements(), most_common(n), subtract()
    연산으로는 +, -, &, | 가 있다.
    
    참고 : https://excelsior-cjh.tistory.com/94
    '''

    #Hash를 사용한 코드
    '''
    dict = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for comp in completion:
        temp -= hash(com)
    
    answer = dic[temp]
    return answer
    
    -> 각 단어는 자신만의 해시값을 가진다는 점을 이용해 해결한 문제
    결과적으로 1개의 이름만 다르기 때문에 마지막에 남은 temp값이 
    두개의 리스트중 다른 원소의 값이 됨
    '''