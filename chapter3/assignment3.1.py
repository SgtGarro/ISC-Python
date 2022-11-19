hrs = input("Enter Hours:")
taxRate = input("Enter PerHour:")
h = float(hrs)
tax = float(taxRate)
h_2 = 0
if(h > 40):
  h_2 = h - 40
  h = h - h_2

total = h * tax + h_2 * (tax * 1.5)
print(total)