string = 'acabaabacakkmmddeewwqqrerttffloooooaaooooog'
#string = 'yandex'
#string = 'abac'
min_sub = string
flag = 0
ln = len(string)
ln_min = ln
pol =set()
for i in range(ln):
    #for j in range(i + 1, ln):
    for j in range(i + 1, i + ln_min):
        sub_string = string[i:j + 1]
        ln_sub = len(sub_string)
        print(sub_string)
        if sub_string == sub_string[::-1]  and ln_sub >= 2 and sub_string not in pol:
            pol.add(sub_string)
            flag = 1
            if ln_sub <= ln_min:
                ln_min = ln_sub
            break
                #pol.append(sub_string)
        #if sub_string == sub_string[::-1] and sub_string <= min_sub and len(sub_string) <= len(min_sub):
        #    min_sub = sub_string
        #    flag = 1
#pol = ['ant', 'bear', 'cat', 'dog', 'man']

pol = list(pol)
print(pol)
pol.sort()
pol.sort(key=len)
print(pol[0] if flag else -1)

#print('aac' < 'aaca')