name = input("Enter your name : ")
gender = input("Enter gender (M/F) : ")
age = int(input("Enter age : "))
product = input("Enter product : ")
grams = float(input("Enter product gram : "))
gold_price_per_gram = float(input("Current gold price (1 grm) : "))

total_gold_rate = grams * gold_price_per_gram

making_charge_per_gram = 845
total_making_charge = grams * making_charge_per_gram

total_amount = total_gold_rate + total_making_charge

discount_percent = 0

if gender.upper() == "M":
    if age > 65:
        if total_gold_rate > 200000 and total_gold_rate <= 300000:
            discount_percent = 20
        elif total_gold_rate > 300000 and total_gold_rate <= 500000:
            discount_percent = 30
        elif total_gold_rate > 500000:
            discount_percent = 35
    else:  
        if total_gold_rate > 200000 and total_gold_rate <= 300000:
            discount_percent = 10
        elif total_gold_rate > 300000 and total_gold_rate <= 500000:
            discount_percent = 20
        elif total_gold_rate > 500000:
            discount_percent = 25
elif gender.upper() == "F":
    if age > 65:
        if total_gold_rate > 200000 and total_gold_rate <= 300000:
            discount_percent = 25
        elif total_gold_rate > 300000 and total_gold_rate <= 500000:
            discount_percent = 35
        elif total_gold_rate > 500000:
            discount_percent = 40
    else: 
        if total_gold_rate > 200000 and total_gold_rate <= 300000:
            discount_percent = 15
        elif total_gold_rate > 300000 and total_gold_rate <= 500000:
            discount_percent = 25
        elif total_gold_rate > 500000:
            discount_percent = 30

discount_amount = (total_gold_rate * discount_percent) / 100

net_amount = (total_gold_rate - discount_amount) + total_making_charge

print("\n-------------------------------------")
print("TOTAL GOLD RATE : ", total_gold_rate)
print("Making charges (1 gram)  : ", making_charge_per_gram)
print("Total Making Charges : ", total_making_charge)
print("---------------------------------------")
print("TOTAL AMOUNT : ", total_amount)
print("\nDISCOUNT : ", discount_percent, "(AUTOMATIC)")
print("Discount Amount (on gold only) : ", discount_amount)
print("-----------------------------------------")
print("Total Net Amount : ", net_amount)