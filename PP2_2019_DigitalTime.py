def changeTo24Hrs(time):
    a, b = time.split('.')

    if b[-2:]=='am':
        hours_part = a.rjust(2,'0')
    else:
        hours_part = str(int(a) + 12).rjust(2,'0')

    minutes_part = b[:2]
    return f'{hours_part}.{minutes_part}'

def findSegment(digit):
    '''formats of digits'''
    match digit:
        case '0':
            return [' _ ', '| |', '|_|']
        case '1':
            return [' '  , '|'  , '|'  ]
        case '2':
            return [' _ ', ' _|', '|_ ']
        case '3':
            return [' _ ', ' _|', ' _|']
        case '4':
            return ['   ', '|_|', '  |']
        case '5':
            return [' _ ', '|_ ', ' _|']
        case '6':
            return [' _ ', '|_ ', '|_|']
        case '7':
            return [' _ ', '  |', '  |']
        case '8':
            return [' _ ', '|_|', '|_|']
        case '9':
            return [' _ ', '|_|', ' _|']
        case '.':
            return [' '  , '.'  , '.'  ]

def getFormat(time_24hrs):
    '''get the formats to print'''
    formats = [] # contain all formats
    format_out = [] # contain all formats in oder to print
    
    for digit in time_24hrs:
        formats.append(findSegment(digit))

    for i in range(3):
        temp = []
        for j in range(5):
            temp.append(formats[j][i])
        format_out.append(temp)
    return format_out

def outDigit(time_format):
    '''get the time to print'''
    new_time_format = ''

    for x in time_format:
        new_time_format += '\n' + ' '.join(x) # to print space seperated time
    return new_time_format

if __name__ == '__main__':
    # Input and Open files
    file_inp_name = input().strip()
    file_inp = open(file_inp_name, 'r')
    file_out = open('Output.txt', 'w')

    time = file_inp.readline().strip() # time in 12hr format
    time_24hrs = changeTo24Hrs(time) # time in 24hr format
    time_24hrs_format = getFormat(time_24hrs)
    time_24hrs_print = outDigit(time_24hrs_format)

    # Output
    file_out.write(time_24hrs_print)
    print(time_24hrs_print)

    # Close files
    file_open.close()
    file_out.close()
    

        
        

