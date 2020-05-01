import math
import sys
import argparse

args = sys.argv

if len(sys.argv) != 5:
    print('Incorrect parameters')
    exit()

if 'interest' not in sys.argv[4]:
    print('Incorrect parameters')
    exit()

type = (sys.argv[1]).replace('--type=', '')
principal = (sys.argv[2]).replace('--principal=', '')
# payment = (sys.argv[2]).replace('--payment=', '')
periods = (sys.argv[3]).replace('--periods=', '')
# payment = (sys.argv[3]).replace('--payment=', '')
interest = (sys.argv[4]).replace('--interest=', '')
i = (float(interest) / 12) / 100
m = 1

if type == 'annuity':
    # if 'interest' not in sys.argv[4]:
    #     principal = (sys.argv[2]).replace('--principal=', '')
    #     payment = (sys.argv[3]).replace('--payment=', '')
    #     periods = (sys.argv[4]).replace('--periods=', '')
    #     x = (int(payment) * int(periods)) - int(principal)
    #     y = (x / int(principal)) / (int(periods) / 12)
    #     z = round(y, 1)
    #     print('Your interest rate = ' + str(z) + '!')
    #     print('Overpayment = ' + str(x).replace('.0', ''))
    #     exit()

    if 'payment' in sys.argv[2]:
        payment = (sys.argv[2]).replace('--payment=', '')
        periods = (sys.argv[3]).replace('--periods=', '')
        x = ((i * ((1 + i) ** int(periods))) / (((1 + i) ** int(periods)) - 1))
        z = int(payment) / x
        a = math.floor(z)
        print('Your credit principal = ' + str(a).replace('.0', '') + '!')
        print('Overpayment = ' + str((int(payment) * int(periods)) - a).replace('.0', ''))
        exit()
    if 'principal' in sys.argv[2] and 'payment' in sys.argv[3]:
        principal = (sys.argv[2]).replace('--principal=', '')
        payment = (sys.argv[3]).replace('--payment=', '')
        x = (int(payment) / (int(payment) - i * int(principal)))
        z = 1 + i
        n_payments = math.log(x, z)
        a = (n_payments) / 12
        b = math.floor(a)  # years
        c = a - b
        d = c * 12
        e = math.ceil(d)  # months
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
        print('Overpayment = ' + str((int(payment) * round(n_payments)) - int(principal)).replace('.0', ''))
        exit()
    if 'principal' in sys.argv[2]:
        x = ((i * ((1 + i) ** int(periods))) / (((1 + i) ** int(periods)) - 1))
        z = (int(principal) * x)
        f = round(z)  # calculates annuity and rounds answer
        if f < z:
            e = f + 1
            print('Your annuity payment = ' + str(e).replace('.0', '') + '!')
        print('Overpayment = ' + str((e * int(periods)) - int(principal)).replace('.0', ''))
        exit()
        if f >= z:
            print('Your annuity payment = ' + str(z).replace('.0', '') + '!')
        print('Overpayment = ' + str((z * int(periods)) - int(principal)).replace('.0', ''))
        exit()

if type == 'diff':
    total = []
    diff = ((int(principal) / (int(periods))) + (i * (int(principal) - ((int(principal) * (m - 1)) / (int(periods))))))
    f = round(diff)
    e = round(f + 1)
    while m <= int(periods):
        m += 1
        if f < diff:
            e = round(f + 1)
            month = m - 1
            print('Month ' + str(month) + ': paid out ' + str(e).replace('.0', ''))
            total.append(e)
            diff = ((int(principal) / (int(periods))) + (
                        i * (int(principal) - ((int(principal) * (m - 1)) / (int(periods))))))
            f = round(diff)
            e = round(f + 1)
        else:
            f = round(diff)
            e = round(f + 1)
            month = m - 1
            print('Month ' + str(month) + ': paid out ' + str(f).replace('.0', ''))
            total.append(f)
            diff = ((int(principal) / (int(periods))) + (
                        i * (int(principal) - ((int(principal) * (m - 1)) / (int(periods))))))
            f = round(diff)
            e = round(f + 1)
    print('\nOverpayment = ' + str((sum(total)) - int(principal)).replace('.0', ''))
