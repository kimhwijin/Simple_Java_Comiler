import os 
#INPUT STRING의 SYNTEX ANALYZER과정을 LOG에 저장한다.
path = os.getcwd() + '/syntex_analyzer_logs/'
file_list = os.listdir(path)
f_name = len(file_list) + 1
f_name = str(f_name) + '.log'
log_file = open('syntex_analyzer_logs/' + f_name, 'w')

import lexical_analyzer
import LR_Tabel
import Grammer
from collections import deque

#lexical analyzer의 token을 저장한다.
tokens = lexical_analyzer.lexical_analyzer_fn()
#http://jsmachines.sourceforge.net/machines/slr.html
#생성된 LR tabel을 list[number]['key_name'] == action 형식으로 저장한다.
LR_tabel = LR_Tabel.LR_Tabel_fn()
#syntex grammer을 list == (LEFT , Right tokens) 튜플 형식으로 저장한다.
grammer = Grammer.grammer_fn()
#토큰을 popleft를 위해 deque로 변환한다.
tokens = deque(tokens)

#parsing된 토큰을 로그에 저장한다.
token_str = ''
for t, n in tokens:
    token_str += t
    if t != '$':
        token_str += " "
token_str += '\n'
log_file.write(token_str)
#print(tokens)


#맨처음 스택에 0 을 넣어 초기화한다.
stack = [0]

#step의 최대값을 지정한다. 최대값이 넘어갈경우 while문을 빠져나감.
i = 0
log_str = ''
while i < 500:
    #step별로 stack과 남아있는 tokens을 로그에 저장한다
    log_str = '-' * 15 + 'steps :' + str(i) + '-' * 15 + '\n'
    #print(log_str)
    log_file.write(log_str)
    log_str = 'stack : ' + str(stack)[1:-1] + '\n'
    #print(log_str)
    log_file.write(log_str)
    log_str = 'tokens : ' + str(list(tokens)[1:-1]) + '\n'
    #print(log_str)
    log_file.write(log_str)

    #stack top 이 int일경우
    if type(stack[-1]) == int:
        #stack top 에 lr tabel state를 저장한다.
        state = stack[-1]
        #tokens의 맨처음 토큰을 저장한다.
        token = tokens[0][0]
        #LR table에서 state와 token에 맞는 action을 저장한다.
        action = LR_tabel[state][token]
        #현재 state, token, action을 로그에 저장한다.
        log_str = '## state :' + str(state) + '| token :' + str(token) + '| action :' + str(action) + '\n'
        #print(log_str)
        log_file.writelines(log_str)

        #LR table에 action이 없으면 문법오류를 반환한다.
        if action == None:
            print(token, 'SyntaxError : Invalid syntax')
            break

        #action이 acc 이면 accept 과정
        if action == 'acc':
            #로그에 accept를 저장하고 종료한다.
            log_str = '-' * 16 + 'accept!' + '-' * 16 + '\n'
            print(log_str)
            log_file.write(log_str)
            break
        #action이 s로 시작하면
        if action[0] == 's':
            #맨처음 토큰과 action number를 stack top에 저장한다.
            stack.append(token)
            stack.append(int(action[1:]))
            #토큰리스트의 맨처음 토큰을 pop한다.
            tokens.popleft()

        #action이 r로 시작하면
        elif action[0] == 'r':
            #grammer list에서 목적 grammer로 reduce한다
            to_reduce , from_reduce = grammer[int(action[1:])]
            #합쳐지는 non - terminal들 list
            from_reduce = from_reduce.split()
            temp = len(stack) - 1

            #합쳐지는 non-terminal들을 거꾸로 stack의 non-terminal과 확인한다.
            for seq_reduce in reversed(from_reduce):
                if type(stack[temp]) == int:
                    temp -= 1
                if seq_reduce == stack[temp]:
                    temp -= 1
                else:
                    #stack에 이상하게 저장되어있으면 error를 출력한다.
                    log_file.write('error')
                    #print('error')
            #합쳐지는 non-terminal의 처음 non-terminal위치 만큼 stack pop한다.
            for _ in range(len(stack) - temp -1):
                stack.pop()
            #stack에 목적 non-terminal을 추가한다.
            stack.append(to_reduce)

    #stack top 이 non-terminal 일경우
    else:
        #알맞는 action을 stack에 추가한다.
        state = stack[-2]
        token = stack[-1]
        action = LR_tabel[state][token]
        log_str = '## state :' + str(state) + '| token :' + str(token) + '| action :' + str(action) + '\n'
        #print(log_str)
        log_file.write(log_str)
        stack.append(int(action))
    #step up
    i += 1


