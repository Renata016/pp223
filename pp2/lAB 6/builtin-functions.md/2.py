text = str(input())
cnt1, cnt2 = 0, 0
for char in text:
    if(char.islower()):
        cnt1 += 1
    else:
        cnt2 +=1

print(cnt1, cnt2)