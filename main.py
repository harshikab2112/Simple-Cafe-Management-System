print("*" * 90)
print(" " * 28 + "WELCOME TO MY CAFE" + " " * 28)
print("*" * 90)

print(
    """
☕ Café Menu - 15 Items

🥤 Beverages
Cappuccino - ₹150
Cold Coffee - ₹130
Lemon Iced Tea - ₹100
Hot Chocolate - ₹140
Strawberry Milkshake - ₹160

🥪 Snacks & Light Bites
Grilled Veg Sandwich - ₹120
Cheese Garlic Bread - ₹110
French Fries - ₹90
Paneer Wrap - ₹150
Chicken Nuggets (6 pcs) - ₹160

🍝 Meals
White Sauce Pasta - ₹180
Veg Hakka Noodles - ₹160
Margherita Pizza (7") - ₹200

🍰 Desserts
Chocolate Brownie - ₹90
Vanilla Ice Cream (2 scoops) - ₹70
"""
)

# Cafe menu dictionary
menu = {
    "cappuccino": 150,
    "cold coffee": 130,
    "lemon iced tea": 100,
    "hot chocolate": 140,
    "strawberry milkshake": 160,
    "grilled veg sandwich": 120,
    "cheese garlic bread": 110,
    "french fries": 90,
    "paneer wrap": 150,
    "chicken nuggets": 160,
    "white sauce pasta": 180,
    "veg hakka noodles": 160,
    "margherita pizza": 200,
    "chocolate brownie": 90,
    "vanilla ice cream": 70,
}

order_total = 0
ordered_items = []

while True:
    item = input("Enter the name of the item you want to order: ").strip().lower()

    if item in menu:
        order_total += menu[item]
        ordered_items.append(item.title())
        print(f"✅ {item.title()} has been added to your order.")
    else:
        print("❌ Item not found in the menu. Please try again.")

    another = input("Do you want to order another item? (Yes/No): ").strip().lower()
    if another != "yes":
        break

# Display order summary
print("\n🧾 Order Summary:")
for i, item in enumerate(ordered_items, 1):
    print(f"{i}. {item} - ₹{menu[item.lower()]}")

print(f"\n💰 Total Amount (without tip): ₹{order_total}")

# Tip option
donate = input("\nWould you like to tip our café staff? (Yes/No): ").strip().lower()
tip = 0

if donate == "yes":
    try:
        tip = int(input("Enter tip amount (₹): "))
        order_total += tip
        if tip > 20:
            print("≽^•⩊•^≼\nThank you so much for your generous tip!")
        else:
            print("Thank you for your kindness!")
    except ValueError:
        print("Invalid amount entered. Tip skipped.")
else:
    print("No problem! We appreciate your visit 😊")

print(f"\n🧾 Final Bill Amount: ₹{order_total}")
print("🙏 Thank you for visiting My Cafe! Have a wonderful day!")
