import pickle
with open('database.pkl', 'rb') as f:
    acc = pickle.load(f)
while True:
    print()
    print('1.deposit', '2.withdraw', '3.check balance', '4.exit', sep='\n')
    n = int(input('select any option: '))
    if n == 1:
        ac = int(input('account number: '))
        if ac in acc:
            amt = int(input('amount: '))
            acc[ac] = acc[ac] + amt
            print('current balance:', acc.get(ac))
            with open('database.pkl', 'wb') as f:
                pickle.dump(acc, f)
        else:
            print('Invalid account number!')
    elif n == 2:
        ac = int(input('account number: '))
        if ac in acc:
            amt = int(input('amount: '))
            if amt < acc.get(ac):
                acc[ac] = acc[ac] - amt
                with open('database.pkl', 'wb') as f:
                    pickle.dump(acc, f)
            else:
                print('Low balance!')
            print('current balance:', acc.get(ac))
        else:
            print('Invalid account number!')
    elif n == 3:
        ac = int(input('account number: '))
        if ac in acc:
            print('balance:', acc.get(ac))
        else:
            print('Invalid account number!')
    elif n == 4:
        break
    else:
        print()
        print('Invalid option!')