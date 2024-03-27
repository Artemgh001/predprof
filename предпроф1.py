s=open('game1.csv',encoding='UTF-8').readlines()#открываем и читаем файл
a=[]
for i in range(1,len(s)):
    st=s[i].split('$')
    if '55' in st[2]: # ищем значения, где присутствует ошибка с 55
        print('У персонажа',st[1],', в игре',st[0],', нашлась ошибка с кодом',st[2],'. Дата фиксации',str(st[3])[:-1],'.')
        st[2]='Done' # меняем ошибку на другое значение
        st[3]='0000-00-00\n'
    a.append(st)
import csv
with open('game_new.csv','w',newline='') as file: # охраняем новый список в новый файл
    write=csv.writer(file)
    write.writerows(a)




