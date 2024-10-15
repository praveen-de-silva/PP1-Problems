def isAnagram(word1, word2):
    # check whether given words are anagram
    if len(word1)==len(word2): # check lenths 
        for char in word1:
            if char not in word2: # check chars
                return False
        return True
    return False

def readData(file_name):
    with open(file_name) as file:
        return file.read()

def writeData(file_name, out_str):
    with open(file_name, 'w') as file:
        file.write(out_str) # output file writting
    

if __name__ == '__main__':
    # == read files ==
    all_data = readData(input().strip()).strip().split('\n')
    out_str = ''

    for inp_data in all_data:
        word1, word2 = inp_data.strip().split()
        
        if isAnagram(word1, word2):
            out_str += 'Anagram\n'
        else:
            out_str += 'Not Anagram\n'

    # == Output ==
    writeData('Output.txt', out_str)
    print(out_str)


