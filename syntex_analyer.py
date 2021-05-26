import os 
path = os.getcwd() + '/syntex_analyzer_logs/'
file_list = os.listdir(path)
f_name = len(file_list) + 1
f_name = str(f_name) + '.log'
log_file = open('syntex_analyzer_logs/' + f_name, 'w')

import lexical_analyzer
import LR_Tabel
import Grammer
from collections import deque

tokens = lexical_analyzer.lexical_analyzer_fn()
LR_tabel = LR_Tabel.LR_Tabel_fn()
grammer = Grammer.grammer_fn()
tokens = deque(tokens)

token_str = ''
for t, n in tokens:
    token_str += t
    if t != '$':
        token_str += " "
token_str += '\n'
log_file.write(token_str)
print(tokens)


stack = [0]
#stack = []
i = 0
#i = 0
log_str = ''
while i < 200:
    log_str = '-' * 15 + 'steps :' + str(i) + '-' * 15 + '\n'
    print(log_str)
    log_file.write(log_str)
    log_str = 'stack : ' + str(stack)[1:-1] + '\n'
    print(log_str)
    log_file.write(log_str)
    log_str = 'tokens : ' + str(list(tokens)[1:-1]) + '\n'
    print(log_str)
    log_file.write(log_str)

    if type(stack[-1]) == int:
        state = stack[-1]
        token = tokens[0][0]
        action = LR_tabel[state][token]
        log_str = '## state :' + str(state) + '| token :' + str(token) + '| action :' + str(action) + '\n'
        print(log_str)
        log_file.writelines(log_str)
        if action == 'acc':
            log_str = '-' * 16 + 'accept!' + '-' * 16 + '\n'
            print(log_str)
            log_file.write(log_str)
            break
        if action[0] == 's':
            stack.append(token)
            stack.append(int(action[1:]))
            tokens.popleft()
        elif action[0] == 'r':
            
            to_reduce , from_reduce = grammer[int(action[1:])]
            from_reduce = from_reduce.split()
            temp = len(stack) - 1

            for seq_reduce in reversed(from_reduce):
                if type(stack[temp]) == int:
                    temp -= 1
                if seq_reduce == stack[temp]:
                    temp -= 1
                else:
                    log_file.write('error')
                    print('error')

            for _ in range(len(stack) - temp -1):
                stack.pop()
            stack.append(to_reduce)
    else:
        state = stack[-2]
        token = stack[-1]
        action = LR_tabel[state][token]
        log_str = '## state :' + str(state) + '| token :' + str(token) + '| action :' + str(action) + '\n'
        print(log_str)
        log_file.write(log_str)
        stack.append(int(action))
    i += 1


