def check_fisrt_let(string):
    if string[0] in ['4', '5', '6']:
        return True
    return False

def check_size(string):
    string.replace('-', '')

    if string.isdigit() and len(string)==16:
        return True
    else:
        return False

def check_sep(string):
    if '-' in string and string[4]==string[9]==string[14]=='-':
        return True
    return False

def checkExceedRepeats(string):
    string.replace('-', '')
    seq_start = 0
    count = 1

    for i in range(1, 16):
        if string[i]!=string[seq_start]:
            seq_start = i
            count = 1
        else:
            count += 1

        if count==5:
            return False
    return True
            

file_read = open(input().strip(), 'r')
file_write = open('Output.txt', 'w')

out_data = []

while True:
    file_data = file_read.readline().strip()

    if file_data == '':
        break

    if check_fisrt_let(file_data) and check_size(file_data) and check_sep(file_data) and checkExceedRepeats(file_data):
        out_data.append('Valid')
    else:
        out_data.append('Invalid')

out_data_str = '\n'.join(out_data)
file_write.write(out_data_str)

file_write.close()
file_read.close()

        
