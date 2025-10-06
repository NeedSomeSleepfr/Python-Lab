Стоимость=float(input())
Скидка=float(input())
НДС=float(input())
X=Стоимость - (Стоимость*Скидка/100)
Y= X* НДС/100
total=X+Y
print(f"Цена после скидки: ")
print(f"НДС: ")
print(f"Итого к оплате: {total:.2f}")