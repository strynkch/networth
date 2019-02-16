import sqlite3

def ass_lib():
    global carloan
    global mort
    bone = input('How much money do you have in your checking account? : ')
    btwo = input('What about your savings account? : ')
    invone = input('Do you have any investments? (stocks, bonds, CD..etc)(y/n): ')
    if invone.lower() == 'y':
            invone = input('How much are your investment(s) worth?: ')
    if invone.lower() == 'n':
       invone = '0'
    car = input('Do you own a car? (y/n): ')
    if car.lower == 'n':
        car = '0'
        carloan = '0'
    if car.lower() == 'y':
        a = input('How many cars do you own?: ')
        if a == '0':
            car = '0'
        if a == '1':
            car = input('How much is your car worth?: ')
        if a >= '2':
            car = input('How much is the sum total of your cars.')
        if a >= '1':
            carloan = input('How much do you owe towards a car loan?: ')
        if car.lower == 'y':
            carloan = input('How much do you owe towards a car loan?: ')
    home = input('Do you own a home?(y/n): ')
    if home == 'n':
        home = '0'
        mort = '0'
    if home.lower() == 'y':
        x = input('How many homes do you own? ')
        if x == '0':
            home = '0'
        if x == '1':
            home = input('What is the Market Value of your home?: ')
        if x >= '2':
            home = input('What is the total market value of the sum of each home?: ')
        if x >= '1':
            mort = input('Enter the amount you owe on your mortgage: ')
        if home == 'y':
            mort = input('Enter amount you owe on mortgage: ')
    personalprop = input('Do you have Personal Property? Such as Jewelery, Art, Furniture, Electronics. Etc (y/n): ')
    if personalprop.lower() == 'y':
        personalprop = input('What is the sum of all Personal Property?: ')
    if personalprop.lower() == 'n':
        personalprop = '0'
    insur = input('Do you have any insurance policies? (y/n): ')
    if insur.lower() == 'n':
        insur = '0'
    if insur.lower() == 'y':
       y = input('How many policies do you have?: ')
       if y >= '2':
            insur = input('What is the total value of all insurance policies?: ')
       if y == '1':
            insur = input('How much is your policy worth?: ')
       if y == '0':
           insur = '0'
    aset = input('Value of any other assets: ')
    stu = input('Value of any student loans: ')
    credit = input('Do you have any credit cards? (y/n) :')
    if credit.lower() == 'n':
            credit = '0'
    if credit.lower() == 'y':
        b = input('How many credit cards do you own?: ')
        if b == '0':
            credit = 0
        if b == '1':
            credit = input('How much do you owe on your credit card?: ')
        if b >= '2':
            credit = input('How much do you owe on your credit cards?: ')
    debt_one = input('Any other form of current debt: ')
    result_one = float(bone) + float(btwo) + float(invone) + float(car) + float(home) + float(personalprop) + float(aset) + float(insur)
    result_two = float(stu) + float(credit) + float(debt_one) + float(mort) + float(carloan)
    print(result_one - result_two)








