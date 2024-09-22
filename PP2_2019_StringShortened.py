def short(string):
    "short the string; removing consequently repeaters"
    string_size = len(string)
    
    if string_size in [0,1]: # if string is only a character
        return string

    new_string = string[0]
    
    for i in range(1, string_size):
        if string[i]!=string[i-1]: # search every new characters
            new_string += string[i]

    return new_string

def checkChar(position, string):
    "check the 'index'ed character from the given 'string'"
    string_size = len(string)

    if position>string_size: # if requied position is higher than the string size
        return 'Position Out of Range' 
    return string[position-1]


try:
    # open files
    file_open = open(input().strip(), 'r')
    file_out  = open('Output2.txt', 'w')

    try:
        N_inputs = int(file_open.readline()) # no of inputs
        out_arr = [] # add results

        for _ in range(N_inputs):
            inp_str, req_pos_str = file_open.readline().strip().split() # input string and requied position (strings)

            shorted_str = short(inp_str)
            req_pos = int(req_pos_str)

            out_arr.append(checkChar(req_pos, shorted_str)) # get the result and add to the out_arr
            
    except Exception:
        print('Data error!')
        
    else:
        # Output :   
        out_str = '\n'.join(out_arr)
        file_out.write(out_str)
        print(out_str)
        
    finally:
        print('close')
        # close files:
        file_open.close()
        file_out.close()
        
except FileNotFoundError:
    print('File does not exsist!')
