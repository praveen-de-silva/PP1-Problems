# ====================
# PROGRAM : Mark Sheet
# ====================

def grading(marks):
    '''evaluvate the grade'''
    if 100>=marks>80: return 'A'
    elif marks>60: return 'B'
    elif marks>40: return 'C'
    elif marks>20: return 'D'
    elif marks>=0: return 'F'
    else: return None

def makeTable(data):
    '''make the table to print'''
    tableHead = '\
+-' + '-'*sizeSbjt + '-+-' + '-'*sizeGrade + '-+' + '\n' + '\
| ' + 'Name' + ' '*(sizeSbjt-4) + ' | ' + 'Grade' + ' |' + '\n' + '\
+-' + '-'*sizeSbjt + '-+-' + '-'*sizeGrade + '-+\n'

    tableBody = ''
    for sbjt, grade in data.items():
        tableBody += '\
| ' + sbjt + ' '*(sizeSbjt-len(sbjt)) + ' | ' + grade + ' '*(sizeGrade-len(grade)) + ' |' + '\n'

    tableFoot = '\
+-' + '-'*sizeSbjt + '-+-' + '-'*sizeGrade + '-+'

    table = tableHead + tableBody + tableFoot
    return table

# --------------------------------------------------------

if __name__ == '__main__':
    try:
        # Input :
        cases = int(input())


        # Variables :
        data = {}
        sizeSbjt = 0
        sizeGrade = 5

        for _ in range(cases):
            sbjt, marks = input().strip().split()
            data[sbjt] = grading(int(marks))

            if sizeSbjt<len(sbjt):
                sizeSbjt = len(sbjt)
    except:
        print('Invalid Input!')
    else:
        # Output:
        table = makeTable(data)
        print(table)