def computepay(h, r):
  total = 0
  if(h > 40):
    total = 40 * r + (h - 40) * (r * 1.5)
  else: 
    total = h * r
  return total

hrs = input("Enter Hours:")
tax = input("Enter Tax: ")
p = computepay(float(hrs), float(tax))
print("Pay", p)