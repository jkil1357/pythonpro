import random

hhp = random.randrange(50, 100)
mhp = random.randrange(50, 100)
num = 0

print("hero HP:", hhp, ", monster HP:", mhp)

while hhp > 0 and  mhp > 0:
    matt = random.randrange(-10, 20)
    hatt = random.randrange(-10, 20)
    num = num + 1

    if matt > 0:
        hhp = hhp - matt
        print("hero(HP:%d, attack:%d)" %(hhp, hatt), end='')
        if hatt > 0:
            print(" success <-> ", end='')
        else:
            print(" fail <-> ", end='')
    elif matt <= 0:
        print("hero(HP:%d, attack:%d)" %(hhp, hatt), end='')
        if hatt > 0:
            print(" success <-> ", end='')
        else:
            print(" fail <-> ", end='')

    if hatt > 0:
        mhp = mhp - hatt
        print("monster(HP%d, attack:%d)" %(mhp, matt), end='')
        if matt > 0:
            print(" success")
        else:
            print(" fail")
    elif hatt <= 0:
        print("monster(HP%d, attack:%d)" %(mhp, matt), end='')
        if matt > 0:
            print(" success")
        else:
            print(" fail")

print("----------------------------------------------------\n")
print("Total phase:", num)

if hhp <= 0:
    print("Monster Win!!!!")
elif mhp <= 0:
    print("Hero Win!!!!")

