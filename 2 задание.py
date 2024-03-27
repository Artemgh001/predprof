s=open('game1.csv',encoding='UTF-8').readlines()
print('Введите имя вашего персонажа')
a = input()
k=0
z=0
while True:
    if a=='game':
        break
    for i in range(len(s)):
        st = s[i].split('$')
        if st[1]==a and k<=5:
            k+=1
            print('Персонаж',st[1], 'встречается в играх :',st[0])
        if k!=0:
            k=0
    a=input()
    for i in range(len(s)):
        st=s[i].split('$')
        if st[1]!=a:
            z+=1
        if z==len(s) and a!='game':
            print('Этого персонажа не существует')
            z=0