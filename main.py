expense=[]

while True:
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total by Category")
    print("4. Exit")

    choice=input("Enter a choice: ")

    if choice=="1":
        Category=input("Enter a category: ")
        Price=float(input("Enter a price: "))
        Date=input("Enter a date (YYYY-MM-DD): ")

        new_expense = {
            "category": Category,
            "price": Price,
            "date": Date
        }

        expense.append(new_expense)
        print("Expense Added!")

    if choice=="2":
        for e in expense:
            print(e["category"], "-", e["price"], "-", e["date"])
        
    if choice=="3":
        totals={}
        for e in expense:
            cat=e["category"]
            p=e["price"]
            if cat in totals:
                totals[cat]+=p
            else:
                totals[cat]=p
        for cat, total in totals.items():
            print(cat, ":" , total)

    if choice=="4":
        print("\nTrack your expenses daily. Small savings build big wealth!")
        break





