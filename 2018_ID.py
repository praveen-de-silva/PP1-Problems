# ============
# PROGRAM : ID
# ============

# Input :
idNoStr = input().strip()


# Varibles :
bYear = int(idNoStr[:2]) # birth year
days = int(idNoStr[2:5])
months = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}


# determine gender
if days<500:
    gend = 'M'
    tempDays = days
else:
    gend = 'F'
    tempDays = days - 500


# determine month & date
for month in months:
    monthDays = months[month]
    if tempDays<=monthDays:
        bMonth = month # birth month
        bDay = tempDays ## birth date
        break
    tempDays -= monthDays


# Output :
print(f'19{bYear}-{str(bMonth).zfill(2)}-{str(bDay).zfill(2)}\n{gend}')