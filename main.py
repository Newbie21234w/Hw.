class BlueTeam:
    protect = "base"
    push = "enemies"
    target = "time_limit"

sd1 = BlueTeam
print(sd1.protect)
print(sd1.push)
print(sd1.target)

sd2 = BlueTeam
print(sd2.protect)
print(sd2.push)
print(sd2.target)

sd3 = BlueTeam
print(sd3.protect)
print(sd3.push)
print(sd3.target)

class RedTeam:
    attack = "enemy"
    push = "enemies"
    target = "enemy's base"


sd1 = RedTeam
print(sd1.attack)
print(sd1.push)
print(sd1.target)

sd2 = RedTeam
print(sd2.attack)
print(sd2.push)
print(sd2.target)

sd3 = RedTeam
print(sd3.attack)
print(sd3.push)
print(sd3.target)