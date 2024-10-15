def addData(dic, player, dots, ones, twos, threes, fours, sixes):
    dic[player] = int(ones) + int(twos)*2 + int(threes)*3 + int(fours)*4 + int(sixes)*6 # calculate players score

def setOutput(dic):
    res = ''
    for name, score in dic.items():
        res += f'{name} {score}\n' # printing structure
    return res

def findLength(arr):
    if len(arr)>0:
        max_size = 0
        for item in arr:
            if len(str(item))>max_size:
                max_size = len(str(item))
        return max_size

def readFile(file_name):
    with open(file_name) as file:
        return file.read().strip().split('\n')

def writeFile(file_name, out_str):
    with open(file_name, 'w') as file:
        file.write(out_str)

if __name__ == '__main__':
    # input
    #input_file_name = input().strip()
    inp_data = readFile('Praveen.txt')
    database = dict() # database of records

    for data in inp_data:
        # player by player analyzing
        player, dots, ones, twos, threes, fours, sixes = data.split()
        addData(database, player, dots, ones, twos, threes, fours, sixes)

    # output
    out_str = setOutput(database)
    writeFile('Output.txt', out_str)
##    print(out_str)


names = list(database.keys())
scores = list(database.values())

name_size = max(len('player'), findLength(names))
score_size = max(len('score'), findLength(scores))

line = '+' + '-'*(name_size+2) + '+' + '-'*(score_size+2) + '+\n'
title = '|' + ' Player'.ljust(name_size+2, ' ') + '|' + ' Score'.ljust(score_size+2, ' ') + '|\n'

body = ''
for player,  score in database.items():
    body += f"| {player.ljust(name_size+1, ' ')}| {str(score).ljust(score_size+1, ' ')}|\n"

print(line + title + line + body + line)
