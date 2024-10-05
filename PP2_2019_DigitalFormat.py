def getDigit(digit_str):
    '''make symbols of digit arrays'''
    match digit_str:
        case '0':
            return ['+-+', '| |', '+ +', '| |', '+-+']
        case '1':
            return ['   ', '  |', '   ', '  |', '   ']
        case '2':
            return ['+-+', '  |', '+-+', '|  ', '+-+']
        case '3':
            return ['+-+', '  |', '+-+', '  |', '+-+']
        case '4':
            return ['   ', '| |', '+-+', '  |', '   ']
        case '5':
            return ['+-+', '|  ', '+-+', '  |', '+-+']
        case '6':
            return ['+-+', '|  ', '+-+', '| |', '+-+']
        case '7':
            return ['+-+', '  |', '  +', '  |', '   ']
        case '8':
            return ['+-+', '| |', '+-+', '| |', '+-+']
        case '9':
            return ['+-+', '| |', '+-+', '  |', '+-+']

def getNum(num_str):
    '''make string by-line for print'''
    num_str
    df = []
    num_df_str = ''

    for dig in num_str:
        df.append(getDigit(dig))

    for j in range(5): # firstly walks through each line of all numbers
        num_df_str += '\n'
        for i in range(len(df)): 
            num_df_str += df[i][j] + ' '
    return num_df_str        


if __name__=='__main__':
    try:
        # opening files
        file_open = open(input().strip(), 'r')
        file_out = open('Output.txt', 'w')
        out_print = '' # string for containg all output data

        try:
            while True:
                file_data = file_open.readline().strip() # read data line-by-line

                if file_data == '': # stop reading data
                    break

                out_print += getNum(file_data) # add digit-vise data
        except Exception:
            print('Data error!')
        else:
            # Output:
            file_out.write(out_print)
            print(out_print)

        # closing files
        file_open.close()
        file_out.close()
    except FileNotFoundError:
        print('File does not exsist!')
