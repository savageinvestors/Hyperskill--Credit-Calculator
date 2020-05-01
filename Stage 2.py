print('Enter the credit principal: ')
x = int(input())
print('What do you want to calculate? type "m" for count of months, type "p" for monthly payment: ')
y = input()
if y == 'm':
    print('Enter monthly payment: ')
    z = int(input())
    months = (round(x / z))
    if months > 1:
        print('It takes ' + str(months) +' months to repay the credit')
    else:
        print('It takes ' + str(months) + ' month to repay the credit')
if y == 'p':
    print('Enter count of months: ')
    a = int(input())
    payment = (x / a)
    round_payment = (round(x / a))
    new_payment = (round(x / a) + 1)
    # print(payment)
    # print(round_payment)
    # print(new_payment)
    if round_payment < payment:
        if new_payment * a > x:
            last_month = x - (a - 1) * new_payment
            print('Your monthly payment = ' + str(new_payment) + ' with last month payment = ' + str(last_month))
        else:
            print('Your monthly payment = ' + str(new_payment))
    else:
        if round_payment * a > x:
            last_month = x - (a - 1) * round_payment
            print('Your monthly payment = ' + str(round_payment) + ' with last month payment = ' + str(last_month))
        else:
            print('Your monthly payment = ' + str(round_payment))
