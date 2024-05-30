d = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
order = []
total_cost = 0
while True:
    try:

        item = input("Item: ").strip().title()
        if item in d:
            order.append(d[item])
            total_cost = sum(order)
            print(f"Total: ${total_cost:.2f}", end="\n")
        else:
            pass

    except EOFError:
        print()
        break

