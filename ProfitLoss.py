costp = float(input("Enter the Cost Price for the Product: "))
sellp = float(input("Enter the Selling Price for the Product: "))

if sellp > costp:
    print("\nProduct was sold with Profit!")
elif costp > sellp:
    print("\nProduct sold with Loss!")
else:
    print("No Profit, No Loss!")
