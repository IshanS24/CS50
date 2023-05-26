bandA = 0
bandB = 0
bandC = 0
bandD = 0
temp = [["Band A", "10 or below"], ["Band B", "11-20"], ["Band C", "21-30"], ["Band D", "31 or above"]]

for i in range (0, len(temp)):
    if temp[i][1] <=10 :
        bandA = bandA + 1
    if temp[i][1] >= 11 and temp[i][1] <=20:
        bandB = bandB + 1
    if temp[i][1] >= 21 and temp[i][1] <=30:
        bandC = bandC + 1
    if temp[i][1] >= 31:
        bandD = bandD + 1  

print("Band A: " + bandA)
print("Band B: " + bandB)
print("Band C: " + bandC)
print("Band D: " + bandD)

