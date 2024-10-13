def toBin(num):
    '''convert a digit to binary'''
    quot = num
    bin_rev = ''

    while True:
        if quot==0: # breaks if quotiant is zero
            break
        
        bin_rev += str(quot%2)
        quot //= 2    
    return bin_rev[::-1].rjust(8, '0') # make 8 widthed string by reversing 'bin_rev'

def binRep(string):
    '''make the bin representation'''
    bin_vals = [] # to contain all bin representaions
    
    for char in string:
        bin_vals.append(toBin(ord(char)))

    return ' '.join(bin_vals)

if __name__=='__main__':
    # Open files
    file_inp = open(input().strip(), 'r')
    file_out = open('Output.txt', 'a')

    while True:
        inp_data = file_inp.readline().strip() # read input file data

        if inp_data=='':
            break

        bin_str = binRep(inp_data)
        file_out.write(bin_str + '\n')

    # Close files
    file_inp.close()
    file_out.close()
