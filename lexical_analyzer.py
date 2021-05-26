def get_seperator_token_name(cur_char):
    if cur_char == '(':
        return 'lparen'
    elif cur_char == ')':
        return 'rparen'
    elif cur_char == '{':
        return 'lbrace'
    elif cur_char == '}':
        return 'rbrace'
    elif cur_char == '[':
        return 'lbracket'
    elif cur_char == ']':
        return 'rbracket'
    elif cur_char == ',':
        return 'comma'
    elif cur_char == '.':
        return 'period'
    elif cur_char == ';':
        return 'semi'

#id 의 start symbol 확인
def D_id_start(char_token):
    if (char_token in define_alphabet) or char_token == '_':
        return True
    return False


#digit인지 판별
def D_digit(char_token):
    if char_token in define_digit:
        return True
    return False

#identifer 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Identifier(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_Identifier',token)
    #id-start
    if D_id_start(token[0]):
        for i in range(1,len(token)):
            if not(D_id_start(token[i]) or D_digit(token[i])):
                #not id-start or digit
                return False
        #all char is id-start or digit
        return True
    #not id-start
    return False
#keyword 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Keyword(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_Keyword',token)
    for keyword in define_keyword:
        #keyword = 'if'
        for i in range(len(keyword)):
            #i = 0 1
            if token == keyword[:i+1]:
                return True
    return False
#operator 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Operator(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_Operator',token)
    for operator in define_operator:
        #operator = <=
        for i in range(len(operator)):
            #i = 0 1
            if token == operator[:i+1]:
                return True
    return False
#integer 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Integer(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_Integer',token)   

    if token[0] == '0':
        if len(token) > 1:
            return False
        return True
    elif token[0] in ['+','-']:
        #정수의 부호symbol은 이전 토큰이 operator일때 + - 을 정수의 부호로 지정한다
        if len(tokens) > 0:
            if tokens[-1][0] != 'OPERATOR':
                return False
        else:
            return False

        if len(token) == 1:
            return True
        if token[1] == '0':
            if len(token) > 2:
                #+01
                return False
            #+0
            return True

    #sign 있는 정수
    if token[0] in ['+','-']:
        #정수의 부호symbol은 이전 토큰이 operator일때 + - 을 정수의 부호로 지정한다
        if len(tokens)> 0:
            if tokens[-1][0] != 'OPERATOR':
                return False
        else:
            return False
        # +10 -123
        if len(token) > 2:
            if token[-1] not in define_digit:
                #not digit
                return False
            #all digit
            return True
        # +1
        elif len(token) > 1:
            if token[1] in define_non_zero_digit:
                return True
            return False
        elif len(token) == 1:
            return True


    #sign 없는 정수 1~9 & 0~9*
    if token[0] in define_non_zero_digit:
        if len(token) > 1:
            #추가된 symbol을 확인한다. 1~9 & 0~9
            if token[-1] not in define_digit:
                    #not digit
                return False
            #all digit
            return True
        else:
            #맨처음 판별 1~9
            return True

#boolean 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Boolean(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_Boolean',token)
    for boolean in define_boolean:
        #boolean = false
        for i in range(len(boolean)):
            #i = 0 .. 4
            if token == boolean[:i+1]:
                return True
    return False
#char 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Char(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_Char',token)
    #token = '1
    if token[0] == "'":
        #1 char
        if token[1] in define_alphabet + define_special + define_digit + [' ']:
            #'1'3
            if len(token) > 3:
                return False
            #'1'
            elif len(token) == 3:
                #'1'
                if token[2] == '\'':
                    return True
                #'11
                else:
                    PrintError(token,10)
                    return False
            #'1
            elif len(token) == 2:
                return True
        #'\n'
        elif token[1] == '\\':
            #'\n'1
            if len(token) > 4:
                return False
            #'\n '\n'
            elif len(token) == 4:
                if token[1:3] in define_escape_sequence:
                    #'\n'
                    if token[3] == '\'':
                        return True
                    #'\n1
                    else:
                        return False
                #'\x'
                else:
                    PrintError(token,12)
                    return False
            #'\n
            elif len(token) == 3:
                #'\n
                if token[1:3] in define_escape_sequence:
                    return True
                #'\x
                else:
                    PrintError(token,12)
                    return False
            #'\
            else:
                return True
        #'' , ''1
        elif token[1] == "'":
            if len(token) == 2:
                return True
            elif len(token) == 3:
                return False
    return False

#string 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_String(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_String',token)
    if token[0] == '"':
        #"123"1
        #"1
        if token[-2] == '"' and len(token) > 2:#end string whatever next_symbol
            #"123\"1
            if token[-3] == '\\':
                return True
            #"123"1
            else:
                return False
            return False
        #""1
        elif len(token) == 3 and token[1] == '"':
            return False
        #"\x"
        elif len(token) > 2:
            if token[1] == '\\':
                if token[1:] not in define_escape_sequence:
                    PrintError(token,30)
            return True
        else:
            return True
    return False

#vtype 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Vtype(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    #print('D_token_Vtype',token)
    for vtype in define_vtype:
        #ex vtype = 'int' ...
        for i in range(len(vtype)):
            #i = 0 1 2
            if token == vtype[:i+1]:
                return True
    return False
#septerator 인지 판별 (buffer와 next input symbol을 가지고 토큰 가능성여부를 반환함)
def D_token_Seperator(symbol):
    #print('D_token_Seperator',symbol)
    #1 char
    if symbol == '(':
        tokens.append(('lparen','('))
    elif symbol == ')':
        tokens.append(('rparen',')'))
    elif symbol == '{':
        tokens.append(('lbrace','{'))
    elif symbol == '}':
        tokens.append(('rbrace','}'))
    elif symbol == '[':
        tokens.append(('lbracket','['))
    elif symbol == ']':
        tokens.append(('rbracket',']'))
    elif symbol == ',':
        tokens.append(('comma',','))
    elif symbol == '.':
        tokens.append(('period','.'))
    elif symbol == ';':
        tokens.append(('semi',';'))


#tokens 리스트에 type string과 token을 넣는다
def Append_Token_As_ExpectString(expect_string,bufer):
    token = ''.join(bufer)
    #print("Append_Token_As_ExpectString" , expect_string,token)

    if expect_string == 'vtype':
        tokens.append(('vtype',token))
    elif expect_string == 'keyword':
        tokens.append(('KEYWORD',token))
    elif expect_string == 'id':
        tokens.append(('id',token))
    elif expect_string == 'op':
        tokens.append(('OPERATOR',token))
    elif expect_string == 'int':
        tokens.append(('num',token))
    elif expect_string == 'char':
        tokens.append(('charactor',token))
    elif expect_string == 'bool':
        tokens.append(('boolstr',token))
    elif expect_string == 'str':
        tokens.append(('literal',token))


#첫번째를 제외한 다음 input symbol을 종합적을 판별하여 next_expect 리스트에 추가
def Discriminate_token(expect,bufer,next_symbol):
    next_expect = []
    for expect_index in range(len(expect)):
        if expect[expect_index] == 'vtype':
            if D_token_Vtype(bufer,next_symbol):
               next_expect.append('vtype')
        elif expect[expect_index] == 'keyword':
            if D_token_Keyword(bufer,next_symbol):
                next_expect.append('keyword')
        elif expect[expect_index] == 'id':
            if D_token_Identifier(bufer,next_symbol):
                next_expect.append('id')
        #elif expect[expect_index] == 'seperator':
        elif expect[expect_index] == 'op':
            if D_token_Operator(bufer,next_symbol):
                next_expect.append('op')
        elif expect[expect_index] == 'int':
            if D_token_Integer(bufer,next_symbol):
                next_expect.append('int')
        elif expect[expect_index] == 'char':
            if D_token_Char(bufer,next_symbol):
                next_expect.append('char')
        elif expect[expect_index] == 'bool':
            if D_token_Boolean(bufer,next_symbol):
                next_expect.append('bool')
        elif expect[expect_index] == 'str':
            if D_token_String(bufer,next_symbol):
                next_expect.append('str')
                
    #append token
    if len(next_expect) == 0:
        #완성형만 필터
        expect_isvaild = [False] * len(expect) 
        for expect_index in range(len(expect)):
            if expect[expect_index] == 'vtype':
                if ''.join(bufer) in define_vtype:
                    expect_isvaild[expect_index] = True
            elif expect[expect_index] == 'keyword':
                if ''.join(bufer) in define_keyword:
                    expect_isvaild[expect_index] = True
            elif expect[expect_index] == 'id':
                if ''.join(bufer) not in define_boolean + define_keyword:
                    expect_isvaild[expect_index] = True
            #elif expect[expect_index] == 'seperator':
            elif expect[expect_index] == 'op':
                if ''.join(bufer) in define_operator:
                    expect_isvaild[expect_index] = True
            elif expect[expect_index] == 'int':
                if bufer[0] in ['+','-'] and len(bufer) == 1:
                    expect_isvaild[expect_index] = False
                else: 
                    expect_isvaild[expect_index] = True
            elif expect[expect_index] == 'char':
                if bufer[0] == "'" and bufer[-1] == "'":
                    expect_isvaild[expect_index] = True
            elif expect[expect_index] == 'bool':
                if bufer in define_boolean:
                    expect_isvaild[expect_index] = True
            elif expect[expect_index] == 'str':
                if bufer[0] =='"' and bufer[-1] == '"':
                    expect_isvaild[expect_index] = True
        expect_token = expect[0]
        for i in range(len(expect)):
            if expect_isvaild[i] == True:
                expect_token = expect[i]
                break

        #print('append token',expect_token,bufer)
        Append_Token_As_ExpectString(expect_token,bufer)
        bufer = []
    expect = next_expect

    return bufer, expect


#첫번째 심볼을 통해 필터링을 거친다
def Discriminate_first_symbol(symbol):
    #print('Discriminate_fist_symbol',symbol)
    expect = []
    bufer = []
    #priority
    if symbol in define_boolean_first_symbol:
        expect.append('bool')
    if symbol in define_vtype_first_symbol:
        expect.append('vtype')
    if symbol in define_keyword_first_symbol:
        expect.append('keyword')
    if symbol in define_identifier_first_symbol:
        expect.append('id')
    #seperator 의 경우 길이 1의 토큰만 존재하므로 바로 추가한다
    if symbol in define_seperator_first_symbol:
        #seperator : 1 char, append token
        D_token_Seperator(symbol)

    if symbol in define_operator_first_symbol:
        expect.append('op')
    if symbol in define_integer_first_symbol:
        expect.append('int')
    if symbol in define_char_first_symbol:
        expect.append('char')
    if symbol in define_string_first_symbol:
        expect.append('str')

    #print('Discriminate_fist_symbol: expect : ',expect)

    return bufer,expect

#에러 출력
def PrintError(token,errorcode):
    sindex = 0
    eindex = 0
    pindex = index

    while(input_string[pindex] != '\n' and pindex != 0):
        pindex -= 1
    if pindex == 0:
        sindex = pindex
    else:
        sindex = pindex + 1

    while(input_string[pindex] != '\n'):
        pindex += 1
    eindex =  pindex
    #print(input_string[sindex:eindex])

    if errorcode == 10:
        print("TypeError" , token , ": Charactor Type can has 1 charactor")
    elif errorcode == 11:
        print("TypeError" , token , ": Charactor Type must have 1 charactor")
    elif errorcode == 12:
        print("EscapeError" , token , ": Invaild Escape Charator")
    elif errorcode == 20:
        print("IntegerValueError", token , ": Invaild Integer Value")
    elif errorcode == 30:
        print("EscapeError" , token , ": Invaild Escape Charator")
    exit(0)

#seperator
define_seperator = [';',',','.','(',')','[',']','{','}']
#escape
define_escape_sequence = ['\\n','\\t','\\r','\\v','\\b','\\a','\\f','\\\\','\\\'','\\\"']
#alphabet
define_lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
define_upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
define_alphabet = define_lower_case +  define_upper_case
#digit
define_non_zero_digit = ['1','2','3','4','5','6','7','8','9']
define_digit = ['0'] + define_non_zero_digit
#sign
define_sign = ['+','-']
#space
define_space = [' ','\t','\n']
#keyword
define_keyword = ['if','else','while','class','return']
#operator
define_assign = ['=']
define_arithmetic = ['+','-','*','/']
define_comparison = ['<','>','<=','>=','==','!=']
define_operator = define_assign + define_arithmetic + define_comparison
#special
define_special = ['!','%','^','&','*','(',')','[',']','{','}','-','+','=','|','~','`',';',':','<','>','/','#','@','_']
#boolean
define_boolean = ['false','true']
#Vtype
define_vtype = ['int','char','boolean','String']


#define first symbol
define_identifier_first_symbol = ['_'] + define_lower_case + define_upper_case
define_keyword_first_symbol = set([token[0] for token in define_keyword])
define_seperator_first_symbol = define_seperator
define_operator_first_symbol = set([token[0] for token in define_operator])
define_integer_first_symbol = define_digit + ['+','-']
define_boolean_first_symbol = ['t','f']
define_char_first_symbol = ["'"]
define_string_first_symbol = ['"']
define_vtype_first_symbol = set([token[0] for token in define_vtype])


input_file = open('input_string.txt','r')
#last char $ 을 추가한다.
input_string = input_file.read() + '\n$'
tokens = []
bufer = []
expect = []
index = 0
flag = 0
#input string index를 증가시켜 last string $ 이 나올때까지 반복한다.
while(input_string[index] != '$'):
    flag = 0
    #next input symbol
    next_symbol = input_string[index]

    #tokens에 append 하고 새로운 string을 판별할때
    if len(expect) == 0:
        #첫번째 symbol 판별식
        bufer,expect = Discriminate_first_symbol(next_symbol)
        if len(expect) == 0:
            #not token
            flag = 2
    #2번째 이상 symbol 판별
    else:
        bufer, expect = Discriminate_token(expect,bufer,next_symbol)
        if len(expect) == 0:
            flag = 1

    #정상
    if flag == 0:
        bufer.append(next_symbol)
        index += 1
    #다음 symbol이 token이 아닐때
    elif flag == 2:
        index += 1

#input 판별을 종료하고 버퍼에 남아있는 토큰을 추가한다
if expect:
    Append_Token_As_ExpectString(expect[0],bufer)

def lexical_analyzer_fn():
    for idx in range(len(tokens)):
        token , name = tokens[idx]
        if token == 'KEYWORD':
            tokens[idx] = (name, name)
        elif token == 'OPERATOR':
            if name == '=':
                tokens[idx] = ('assign', '=')
            elif name == '+' or name == '-':
                tokens[idx] = ('addsub', name)
            elif name == '*' or name == '/':
                tokens[idx] = ('multdiv', name)
            elif name in define_comparison:
                tokens[idx] = ('comp', name)
    tokens.append(('$','endstr'))
    return tokens

print(tokens)