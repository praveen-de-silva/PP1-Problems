def block(original_string):
    '''make k widthed string blocks'''
    string_blocks = [] # to contain blocks of strings

    for i in range(0, n, k):
        string_blocks.append(original_string[i:i+k])

    return string_blocks

def removeRepeats(string):
    '''remove repeated characters'''
    seen = [] # to collect previously seen letters
    new_string = ''

    for letter in string:
        if letter not in seen:
            new_string += letter
            seen.append(letter)

    return new_string


# open files
file_read = open(input().strip(), 'r')
file_write = open('Output.txt', 'w')


# Variables :
s = file_read.readline().strip()
k = int(file_read.readline())
n = len(s)
s_blocks = block(s)
s_output_list = []


for block in s_blocks:
    block_edited = removeRepeats(block)
    s_output_list.append(block_edited)


# Output :
s_output = '\n'.join(s_output_list)
print(s_output)  
file_write.write(s_output)


# cloae files
file_read.close()
file_write.close()
