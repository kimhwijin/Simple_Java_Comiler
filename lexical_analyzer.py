'''
 Input: -0
- Output: <OP, ->, <INTEGER, 0>

- Input: 0abc0
- Output: <INTEGER, 0>, <ID, abc0>

- Input: 123if
- Output: <INTEGER, 123>, <IF>

- Input: 123if0
- Output: <INTEGER, 123>, <ID, if0>

- Input: ' '
- Output: <char, >

- Input: a-1
- Output: <ID, a>, <OP, ->, <INTEGER, 1>
(Only in this example, you are required to consider the syntax of your program, i.e., the purpose of using the '-' symbol)

- Input: int main(){char if123='1';int 0a=a+-1;return -0;}
- Output: <VTYPE, int>, <ID, main>, <LPAREN>, <RPAREN>, <LBRACE>,
<VTYPE, char>, <ID, if123>, <ASSIGN>, <CHAR, 1>, <SEMI>,
<VTYPE, int>, <INTEGER, 0>, <ID, a>, <ASSIGN>, <ID, a>, <OP, +>, <INTEGER, -1>, <SEMI>,
<RETURN>, <OP, ->, <INTEGER, 0>, <SEMI>, <RBRACE>
'''

def get_seperator_token_name(cur_char):
    if cur_char == '(':
        return 'LEFT_PAREN'
    elif cur_char == ')':
        return 'RIGHT_PAREN'
    elif cur_char == '{':
        return 'LEFT_BRACE'
    elif cur_char == '}':
        return 'RIGHT_BRACE'
    elif cur_char == '[':
        return 'LEFT_BRACKET'
    elif cur_char == ']':
        return 'RIGHT_BRACKET'
    elif cur_char == ',':
        return 'COMMA'
    elif cur_char == '.':
        return 'PERIOD'
    elif cur_char == ';':
        return 'SEMI_COLON'


def D_id_start(char_token):
    if (char_token in define_alphabet) or char_token == '_':
        return True
    return False

def D_digit(char_token):
    if char_token in define_digit:
        return True
    return False

def D_token_Identifier(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_Identifier',token)
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

def D_token_Keyword(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_Keyword',token)
    for keyword in define_keyword:
        #keyword = 'if'
        for i in range(len(keyword)):
            #i = 0 1
            if token == keyword[:i+1]:
                return True
    return False

def D_token_Operator(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_Operator',token)
    for operator in define_operator:
        #operator = <=
        for i in range(len(operator)):
            #i = 0 1
            if token == operator[:i+1]:
                return True
    return False

def D_token_Integer(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_Integer',token)   
    #up to 2 digit
    #만약 token[0] 이 0 이라면, 뒤에 무엇이 오든간에 false를 반환해야함
    #token[0] 이 0 이아닌 숫자라면, next_symbol 에 따라 t/f 반환
    if token[0] in define_non_zero_digit:
        for i in range(1,len(token)):
            if token[i] not in define_digit:
                #not digit
                return False
        #all digit
        return True
    #first symbol is not non zero digit
    return False


def D_token_Boolean(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_Boolean',token)
    for boolean in define_boolean:
        #boolean = false
        for i in range(len(boolean)):
            #i = 0 .. 4
            if token == boolean[:i+1]:
                return True
    return False

def D_token_Char(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_Char',token)
    #token = '1
    if token[0] == "'":
        #1 char
        if token[1] in define_alphabet + define_special:
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
                    return False
            #'\n
            elif len(token) == 3:
                #'\n
                if token[1:3] in define_escape_sequence:
                    return True
                #'\x
                else:
                    return False
            #'\
            else:
                return True
    return False


def D_token_String(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_String',token)
    if token[0] == '"':
        #"123"1
        if token[-2] == '"':#end string whatever next_symbol
            #"123\"1
            if token[-3] == '\\':
                return True
            #"123"1
            else:
                return False
            return False
        else:
            return True
    return False

def D_token_Vtype(bufer,next_symbol):
    token = ''.join(bufer) + next_symbol
    print('D_token_Vtype',token)
    for vtype in define_vtype:
        #ex vtype = 'int' ...
        for i in range(len(vtype)):
            #i = 0 1 2
            if token == vtype[:i+1]:
                return True
    return False

def D_token_Seperator(symbol):
    print('D_token_Seperator',symbol)
    #1 char
    if symbol == '(':
        tokens.append(('LPAREN','('))
    elif symbol == ')':
        tokens.append(('RPAREN',')'))
    elif symbol == '{':
        tokens.append(('LBRACE','{'))
    elif symbol == '}':
        tokens.append(('RBRACE','}'))
    elif symbol == '[':
        tokens.append(('LBRACKET','['))
    elif symbol == ']':
        tokens.append(('RBRACKET',']'))
    elif symbol == ',':
        tokens.append(('COMMA',','))
    elif symbol == '.':
        tokens.append(('PERIOD','.'))
    elif symbol == ';':
        tokens.append(('SEMI_COLON',';'))


def Append_Token_As_ExpectString(expect_string,bufer):
    token = ''.join(bufer)
    if expect_string == 'vtype':
        tokens.append(('VTYPE',token))
    elif expect_string == 'keyword':
        tokens.append(('KEYWORD',token))
    elif expect_string == 'id':
        tokens.append(('IDENTIFIER',token))
    elif expect_string == 'op':
        tokens.append(('OPERATOR',token))
    elif expect_string == 'int':
        tokens.append(('INTIGER',token))
    elif expect_string == 'char':
        tokens.append(('CHARACTOR',token))
    elif expect_string == 'bool':
        tokens.append(('BOOLEAN',token))
    elif expect_string == 'str':
        tokens.append(('STRING',token))


#Discriminate token
def Discriminate_token(expect,bufer,next_symbol):
    next_expect = []
    for expect_index in range(len(expect)):
        if expect[expect_index] == 'vtype':
            if D_token_Vtype(bufer,next_symbol):
               next_expect.append('vtype')
        elif expect[expect_index] == 'keyword':
            if D_token_Keyword(bufer,next_symbol):
                next_expect.append('keyworld')
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
        print('append token',expect[0],bufer)
        Append_Token_As_ExpectString(expect[0],bufer)
        bufer = []
    expect = next_expect

    return bufer, expect


#Discriminate first symbol
def Discriminate_first_symbol(symbol):
    print('Discriminate_fist_symbol',symbol)
    expect = []
    bufer = []
    #priority
    if symbol in define_vtype_first_symbol:
        expect.append('vtype')
    if symbol in define_keyword_first_symbol:
        expect.append('keyword')
    if symbol in define_identifier_first_symbol:
        expect.append('id')

    if symbol in define_seperator_first_symbol:
        #seperator : 1 char, append token
        D_token_Seperator(symbol)

    if symbol in define_operator_first_symbol:
        expect.append('op')
    if symbol in define_integer_first_symbol:
        expect.append('int')
    if symbol in define_boolean_first_symbol:
        expect.append('bool')
    if symbol in define_char_first_symbol:
        expect.append('char')
    if symbol in define_string_first_symbol:
        expect.append('str')

    print('Discriminate_fist_symbol: expect : ',expect)

    return bufer,expect

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
define_integer_first_symbol = define_digit
define_boolean_first_symbol = ['t','f']
define_char_first_symbol = ["'"]
define_string_first_symbol = ['"']
define_vtype_first_symbol = set([token[0] for token in define_vtype])


input_file = open('input_string.txt','r')
input_string = input_file.read() + '$'
tokens = []
bufer = []
expect = []
index = 0

flag = 0

while(input_string[index] != '$'):
    flag = 0
    next_symbol = input_string[index]
    print(bufer,next_symbol)
    print('expect : ',expect)
    if len(expect) == 0:
        bufer,expect = Discriminate_first_symbol(next_symbol)
        if len(expect) == 0:
            #not token
            flag = 2
    else:
        bufer, expect = Discriminate_token(expect,bufer,next_symbol)
        if len(expect) == 0:
            flag = 1

    if flag == 0:
        #nomal
        bufer.append(next_symbol)
        index += 1
    elif flag == 2:
        #not token next symbol
        index += 1
        
Append_Token_As_ExpectString(expect[0],bufer)
print(tokens)