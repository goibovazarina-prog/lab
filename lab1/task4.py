time = int(input())
h = time // 3600
m = (time % 3600) // 60
s = time % 60
print(f"{h:02d}:{m:02d}:{s:02d}")
