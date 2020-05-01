import math
print('What do you want to calculate? type "n" for count of months, type "a" for annuity monthly payment, type "p" for credit principal: ')
# y = 'n'
y = input()
if y == 'n':
    print('Enter credit principal: ')
    # principal = 700000
    principal = int(input())
    print('Enter monthly payment: ')
    # annuity = 26000
    annuity = int(input())
    print('Enter credit interest: ')
    # yearly_interest = 9.1
    yearly_interest = float(input())
    i = (yearly_interest / 12) / 100
    x = (annuity / (annuity - i * principal))
    z = 1 + i
    n_payments = math.log(x, z)
    a = (n_payments) / 12
    b = math.floor(a) # years
    c = a - b
    d = c * 12
    e = math.ceil(d) # months
    if a >= 1:
        if e == 0:
            print('You need ' + str(e) + ' months to repay this credit!')
        elif e == 12:
            f = b + 1
            print('You need ' + str(f) + ' years to repay this credit!')
        else:
            print('You need ' + str(b) + ' years and ' + str(e) + ' months to repay this credit!')

    else:
        print('You need ' + str(e) + ' months to repay this credit!')

if y == 'a':
    print('Enter credit principal: ')
    # principal = 1000000
    principal = int(input())
    print('Enter count of periods: ')
    # n = 60
    n = int(input())
    print('Enter credit interest: ')
    # yearly_interest = 10
    yearly_interest = float(input())
    i = (yearly_interest / 12) / 100
    x = ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
    z = (principal * x)
    f = round(z)
    if f < z:
        e = f + 1
        print('Your annuity payment = ' + str(e) + '!')
    else:
        print('Your annuity payment = ' + str(z) + '!')

if y == 'p':
    print('Enter monthly payment: ')
    # annuity = 8721.8
    annuity = float(input())
    print('Enter count of periods: ')
    # n = 120
    n = int(input())
    print('Enter credit interest: ')
    # yearly_interest = 5.6
    yearly_interest = float(input())
    i = (yearly_interest / 12) / 100
    x = ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
    z = annuity / x
    a = round(z)
    print('Your credit principal = ' + str(a) + '!')
