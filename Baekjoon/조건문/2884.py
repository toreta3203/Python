# 알람 시계

hours, minutes = map(int, input().split())

diff = minutes - 45


if diff < 0 :
    if hours == 0:
        hours = 24
    minutes = 60 + diff
    hours -= 1
elif diff >= 0:
    minutes = diff

print (hours, minutes)

# if diff < 0:
#     hours -= 1
#     minutes = 60 - abs(diff)
#     if hours < 0:
#         hours = 23

# print (hours, minutes)