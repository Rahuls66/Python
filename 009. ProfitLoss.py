costp = float(input("Enter the Cost Price for the Product: "))
sellp = float(input("Enter the Selling Price for the Product: "))

if sellp > costp:
    print("\nProduct was sold with Profit!")
elif costp > sellp:
    print("\nProduct sold with Loss!")
else:
    print("No Profit, No Loss!")

'''
Expected Output

Test Case I:
Enter the Cost Price for the Product: 12.22
Enter the Selling Price for the Product: 34.68

Product was sold with Profit!

Test Case II:
Enter the Cost Price for the Product: 54.97
Enter the Selling Price for the Product: 23.478

Product was sold with Profit!

Test Case III:
Enter the Cost Price for the Product: 55
Enter the Selling Price for the Product: 55
No Profit, No Loss!
'''
