#Lab06-5 (Skyscraper)

height = 0 # ความสูงตึก
count = 0 # นับจำนวนที่เห็น

while True:
    num = int(input())
    if num == -1:
        break
    else:
        if num > height:
            height = num
            count += 1 

print(count)