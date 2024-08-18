# =============
# PROGRAM : GPA
# =============
from math import fabs

# Varables & Inputs
n, m = map(int, input().strip().split())
obtained = input().strip().split()
weights = list(map(int, input().strip().split()))
grades = dict()

for _ in range(m):
    inpGrade, inpPoint = input().strip().split()
    grades[inpGrade] = float(inpPoint)


def calcuteGrade(GPA):
    """calculate the Grade"""
    minDif = GPA
    for grd in grades.keys():
        dif = fabs(grades[grd]-GPA)

        if dif<minDif:
            minDif=dif
            grade = grd
    return grade


# obtain GPA
pwTot = 0
for i in range(len(obtained)):
    pwTot += grades[obtained[i]] * weights[i]

wTot = sum(weights)
GPA = pwTot / wTot
grade = calcuteGrade(GPA)


# Output
print(f'{GPA:.2f}\n{grade}')