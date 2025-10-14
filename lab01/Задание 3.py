Цена=float(input("Цена продукта:"))
Скидка=float(input("Скидка:"))
НДС=float(input("НДС:"))
X= Цена - (Цена*Скидка/100)
Y= X* НДС/100
total=X+Y
print(f"Цена после скидки: {X}")
print(f"НДС: {Y}")
print(f"Итого к оплате: {total:.2f}")