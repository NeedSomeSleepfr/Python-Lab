# Python-Lab
## Лаб 1
### Задание 1

```
Name= input("ваше имя:" )
Year= int(input("ваш возраст:"))
print(f"Привет {Name}!, через год тебе будет {Year+1}")
```
<![alt text](01.1.png)>

### Задание 2

```
n1=float(input("Номер 1 ="))
n2=float(input("Номер 2 ="))
sum=n1+n2
res=n1-n2
print(f"Cложение={sum:.1f}, вычитание={res:.1f}")
```

### Задание 3

```
Цена=float(input("Цена продукта:"))
Скидка=float(input("Скидка:"))
НДС=float(input("НДС:"))
X= Цена - (Цена*Скидка/100)
Y= X* НДС/100
total=X+Y
print(f"Цена после скидки: {X}")
print(f"НДС: {Y}")
print(f"Итого к оплате: {total:.2f}")
```

### Задание 4

```
Минуты=int(input("Минуты: "))
Часы=Min//60
остаток=Min%60
print(f"{Часы}:{остаток:02d}")
```

### Задание 5

```
Name=input("Введите ФИО: ")
inic=Name[0].upper()+"."
for i in range(len(Name)):
    if Name[i] == " " and i +1 < len(Name):
        inic = inic + Name [i + 1]. upper () + "."
lage= len (Name.replace(" ",""))
print (f"ФИО:{Name}")
print (f"Инициалы: {inic}")
print (f"Длина: {lage}")
```
