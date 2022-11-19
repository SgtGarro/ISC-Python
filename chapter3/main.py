x = 6
if x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')

if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')

x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

x = -1
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')

# astr = 'Hello Bob'
# istr = int(astr)
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)