def Frequency_analytic(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i,0)+1
    for key, value in sorted(dic.items()):
        if str.islower(key):
            print(key, value)
    for key, value in sorted(dic.items()):
            if str.isupper(key):
                print(key, value)

if __name__ == "__main__":
    msg = input("input your message : ")
    Frequency_analytic(msg)
