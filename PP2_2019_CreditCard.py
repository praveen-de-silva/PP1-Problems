def checkFisrtLet(cc_str):
    '''check first letter is 4/5/6'''
    if cc_str[0] in ['4', '5', '6']:
        return True
    return False

def checkSize(cc_str_new): # 'cc_str_new' <-- 'cc_str'.replace('-', '') 
    '''check 16 digits are available'''
    if cc_str_new.isdigit() and len(cc_str_new)==16:
        return True
    else:
        return False

def checkSep(cc_str):
    '''check '-' in proper way'''
    if ('-' in cc_str and cc_str[4]==cc_str[9]==cc_str[14]=='-') or ('-' not in cc_str):
        return True
    return False

def checkExceedRepeats(cc_str_new):
    '''check consequently over repeats'''
    seq_start = 0 # index where a change occurs in conseqvance
    count = 1 # count of the consequently similar digits

    for i in range(1, 16):
        if cc_str_new[i] != cc_str_new[seq_start]: # detect a change of the sequence
            seq_start = i
            count = 1
        else:
            count += 1

        if count==5: # detect over repeats
            return False
    return True

def checkMain(card_no):
    '''check all requires'''
    card_no_new = card_no.replace('-', '')
    return checkFisrtLet(card_no) and checkSize(card_no_new) and checkSep(card_no) and checkExceedRepeats(card_no_new)
    

# open files
file_read = open(input().strip(), 'r')
file_write = open('Output.txt', 'w')

# Varibles :
output_data = []
instances = int(file_read.readline())


for _ in range(instances):
    file_data = file_read.readline().strip()

    if checkMain(file_data):
        output_data.append('Valid')
    else:
        output_data.append('Invalid')


# Output :
output_data_str = '\n'.join(output_data)
file_write.write(output_data_str)
print(output_data_str)

file_write.close()
file_read.close()

