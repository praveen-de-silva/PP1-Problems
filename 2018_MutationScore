# ========================
# PROGRAM : Mutation Score
# ========================

parntDNA = input().strip()
childDNA = input().strip()

# A --> T
# G --> C

compLet1 = ['A', 'T']
compLet2 = ['G', 'C']

score = 0

for i in range(len(parntDNA)):
    if childDNA[i]!=parntDNA[i] and ((childDNA[i] in compLet1 and parntDNA[i] in compLet1) or (childDNA[i] in compLet2 and parntDNA[i] in compLet2)):
        score += 2
    elif childDNA[i]=='_' and parntDNA[i]!='_':
        score += 6
    elif childDNA[i]!=parntDNA[i]:
        score += 4

print(score)
    