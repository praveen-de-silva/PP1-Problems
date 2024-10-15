def makeBoard():
    board = set()
    for i in range(8):
        for j in range(8):
            board.add((i, j, ))
    
    return board

def getPoint(cell):
    return ord(cell[0])-97, int(cell[1])-1

def getCell(point):
    return f'{chr(point[0] + 97)}{point[1]+1}'

def isTruePoint(point):
    if 0 <= point[0] <= 7 and 0 <= point[1] <= 7:
        return True
    return False

def allMoves(point, points):
    k1 = -point[0]
    while  True:
        temp_point = (point[0] + k1, point[1])
        if isTruePoint(temp_point):
            points.add(temp_point)
        else:
            break
        k1 += 1

    k2 = -point[1]
    while  True:
        temp_point = (point[0], point[1] + k2)
        if isTruePoint(temp_point):
            points.add(temp_point)
        else:
            break
        k2 += 1

    k3 = k4 = 0
    while  True:
        temp_point1 = (point[0] + k3, point[1] + k3)
        temp_point2 = (point[0] + k4, point[1] + k4)
        if isTruePoint(temp_point1):
            points.add(temp_point1)
            k3 += 1
        elif isTruePoint(temp_point2):
            points.add(temp_point2)
            k4 -= 1
        else:
            break
        
    k5 = k6 = 0
    while  True:
        temp_point1 = (point[0] + k5, point[1] - k5)
        temp_point2 = (point[0] + k6, point[1] - k6)
        if isTruePoint(temp_point1):
            
            points.add(temp_point1)
            k5 += 1
        elif isTruePoint(temp_point2):
            points.add(temp_point2)
            k6 -= 1
        else:
            break
        
def getRemains(string):
    cells_str = string.strip().split()
    all_points = makeBoard()
    movables = set()

    for cell in cells_str:
        point = getPoint(cell)
        allMoves(point, movables)

    remains = all_points - movables
    return sorted(remains)


if __name__=='__main__':
    file_inp = open(input().strip(), 'r')
    file_out = open('Output.txt', 'a')

    data = file_inp.readline().strip()
    remains = [getCell(x) for x in getRemains(data)]

    out_str = '\n'.join(remains)
    file_out.write(out_str)
    print(out_str)

    file_inp.close()
    file_out.close()
