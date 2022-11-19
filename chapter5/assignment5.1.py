largest = -1
smallest = 9999
while True:
  num = input("Enter a number: ")
  if num == "done":
    break
  try:
    num = int(num)
    if (num > largest): 
      largest = num
    if (num < smallest): 
      smallest = num
  except:
    print("Invalid input")
  
print("Maximum is", largest)
print("Minimum is", smallest)