# 오븐 시계

hours, minutes = map(int, input().split())
timer = int(input())

hours += timer // 60
minutes += timer % 60

if minutes >= 60:
    hours += 1
    minutes -= 60

if hours >= 24:
    hours -= 24

print (hours, minutes)
