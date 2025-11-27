#1
hashes = ("abc123", "ffd222", "9af010", "ffd222", "x0x0x0")
b = hashes.count("ffd222")
print("Количество вхождений:", b)

#2
users = ("guest", "moderator", "admin", "root")
b=users.index("admin") 
print("Индекс admin:",b)

#3
key_params = ("AES", 256, "CBC")
algorithm, key_size, mode=key_params
print("Algorithm: ", algorithm)
print ("Key size:",key_size)
print ("Mode:",mode)

#4
log = ("login", "download", "upload", "logout")
b=log[3]
print (b)

#5
ips = ("192.168.0.1", "10.0.0.2", "172.16.0.3")
b=input("Введите IP адрес :")
if b in ips:
    print ("Найдено")
else:
    print ("Нет в списке")      
    
#6
name=input("Введите имя:")    
role=input ("Введите роль:")
status=input ("Введите статус:")
packed=(name,role, status )
print(packed)

#7
access = ("read", "write", "execute")
new=(input("Введите новое значение для 2-го элемента:"))
new_tuple=(access[0],new,access[2])
print (new_tuple)

#8
attempts = ("success", "fail", "fail", "success", "fail", "fail")
a=attempts.count("success")
b=attempts.count("fail")
print("Количество успешных попыток входа:",a)
print ("Количество неудачных попыток входа:",b)

#9
admins = ("root", "admin")
users = ("alex", "bob")
c=admins+users
print (c)

#10
logs = ("login", "upload", "download", "logout")
start, *middle, end = logs
print("Start:", start)
print("Middle:", tuple(middle))
print("End:", end)