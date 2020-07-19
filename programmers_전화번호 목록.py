#전화번호 목록 - 한 번호가 다른 번호의 접두어가 되는가?

#zip을 사용한 풀이
'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False

    return True

    zip을 사용해 매우 간단히 해결, startswith()함수는 ()안의 내용이 문자열의 맨 앞에 오면 True 반환/ 그 외의 경우 False 반환
'''

#정석해쉬
'''
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
    이중포문을 사용해 phone_book을 통해 들어오는 원소를 받고, 원소를 짤라서 각 숫자별로 비교
    만약 숫자가 hash map에 있지만, phone_number는 아닐경우 False
'''

#다른방법
'''
from itertools import combinations as c
def solution(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook, key= len)
    for (a,b) in c( sortedPB,2):
        if a == b[:len(a)]:
            answer = False
    return answer
    
    itertools - 순열(permutations)과 조합(combinations)
    위 코드에서 c(sortedPB,2) 에서 2는 몇개의 아이템을 조합할지 결정하는 인자이다
    permutations는 2번째 인자가 없으면 컨테이너의 전체길이가 default
    combinations의 경우는 에러가 난다
    
    sorted(~~~, key = )의 경우
    key 파라미터의 값은 하나의 인자를 받고 정렬 목적을 위한 키를 리턴하는 함수가 되야함
    따라서 길이에 따라 phoneBook을 정렬해주고, sortedPB에 저장
    그 후, 조합을 통해 모든 조건을 비교하는데, a 가 b의 len(a)까지만 비교하게 해서 접두어 체크
'''
