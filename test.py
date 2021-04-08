input_file = open('input_string.txt','r')
input_string = input_file.read() + '$'
for i in range(len(input_string)):
    print(input_string[i],end="@")
    if input_string[i] == '\n' or input_string[i] == '\t':
        print('asf') 
input_file.close()
