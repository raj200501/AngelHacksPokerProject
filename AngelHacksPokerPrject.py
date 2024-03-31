#You will be given five random cards to choose from. There are certain patterns that will help you win
#The rules will be printed out for the player to understand.
#The five random cards will be printed from a random.randint command and a dictionary.
#The objective of the game is to not be bankrupt and essentialy have more money than the other two players.
#The programcurrentlyprints thrules,andgives you your random cards, and in a loop so that there can be multiple rounds.
import time
import random
money = 3050
rmoney= 3050
jmoney= 3050
pot = 0
icup = 0
print('Welcome to POKER! Make sure you read the directions before you play because the rules are a little different.')
print('Rules:')
print('You will be given five random cards to choose from. There are certain patterns (shown later) that will help you win.')
print('If you think you cards are good, you can put on more money to the pot and the players will have to match it, increase it, or drop out.')
print('Dropping out means that you are out of this round, but the money you already put in is gone.')
print('Here are the flushes from highest to lowest:')
print('1. Five of the same cards (suits ARE included)')
print('2. Five of the same cards (suits NOT included)')
print('3. Five of the same suits (card value NOT included)')
print('4. High Card   The highest ranked card in your hand with an ace being the highest and two being the lowest')
print('If you ever want to show everyones cards and end the turn, you put in double the amount int the pot, and the person with the best deck wins the entire pot.')
print('Each play, you must put 10 dollars into the pot')
print('Do you want to play POKER!?!?!?!?!?  Type -yes- to continue')
x = input()
if x == 'yes':
    print('You will be playing against Josh and Ricardo.')
    print('You have $3050 to play with')
    while True:
        if icup==1:
            print('Are you ready for the next game?')
            x = input()
        f = 1
        opo = 1
        opop = 1
        print('Your cards are:')
        cards = {2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K',14:'A'}
        types = {1:'of diamonds',2:'of hearts',3:'of spades',4:'of clubs'}
        red = 'of diamonds' or 'of hearts'
        black = 'of spades' or 'of clubs'
        a = random.randint(2,14)
        b = random.randint(1,4)
        c = cards[a]
        d = types[b]
        print(c, d)
        a = random.randint(2,14)
        b = random.randint(1,4)
        e = cards[a]
        f = types[b]
        print(e, f)
        a = random.randint(2,14)
        b = random.randint(2,4)
        g = cards[a]
        h = types[b]
        print(g, h)
        a = random.randint(2,14)
        b = random.randint(2,4)
        i = cards[a]
        j = types[b]
        print(i, j)
        a = random.randint(2,14)
        b = random.randint(2,4)
        k = cards[a]
        l = types[b]
        print(k, l)
        a = random.randint(2,14)
        b = random.randint(1,4)
        m = cards[a]
        n = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        o = cards[a]
        p = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        q = cards[a]
        r = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        s = cards[a]
        t = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        u = cards[a]
        v = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        mm = cards[a]
        nn = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        oo = cards[a]
        pp = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        qq = cards[a]
        rr = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        ss = cards[a]
        tt = types[b]
        a = random.randint(2,14)
        b = random.randint(1,4)
        uu = cards[a]
        vv = types[b]
        money = money - 10
        rmoney = rmoney-10
        jmoney = jmoney-10
        icup = 1
        while True:
            pot = pot +30
            if f != 0:
                print('Your turn:')
                print('$',money)
                print('10','100','500','show','drop')
                print('The money you need to put in the pot is 10 or more')
                y = input()
                if y == '10':
                    money = money-10
                    pot = pot +10
                if y == '100':
                    money = money-100
                    pot = pot +100
                if y == '500':
                    money = money-500
                    pot = pot +500
                if money < 0:
                    print('You are bankrupt')
                    break
                if y == 'show':
                    money = money - 20
                    print('Are you ready? - yes-')
                    qpqpqp = input()
                    if qpqpqp == 'yes':
                        print("Josh's cards are...")
                        print(mm, nn)
                        print(oo, pp)
                        print(qq, rr)
                        print(ss, tt)
                        print(uu, vv)
                        print("Ricardo's cards are... say yes to continue")
                        qpqpqp = input()
                        if qpqpqp == 'yes':
                            print(m, n)
                            print(o, p)
                            print(q, r)
                            print(s, t)
                            print(u, v)
                            print('And your cards are... say yes to continue')
                            qpqpqp = input()
                        if qpqpqp == 'yes':
                            print("Your cards are...")
                            print(c, d)
                            print(e, f)
                            print(g, h)
                            print(i, j)
                            print(k, l)
                    if (c and e and g and i and k == c) and (d and f and h and j and l == d):
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if (m and o and q and s and u == m) and (n and p and r and t and v == n):
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if (mm and oo and qq and ss and uu == mm) and (nn and pp and rr and tt and vv == nn):
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    if c and e and g and i and k == c:
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if m and o and q and s and u == m:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if mm and oo and qq and ss and uu == mm:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    if d and f and h and j and l == d:
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if n and p and r and t and v == n:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if nn and pp and rr and tt and vv == nn:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    K = 'K'
                    Q = 'Q'
                    J = 'J'
                    A = 'A'
                    K = 13
                    Q = 12
                    J = 11
                    A = 14
                    youval = c+ e + g +i + k 
                    ricval = m+ o + q +s + u 
                    josval = mm+ oo + qq +ss + uu 
                    if youval > ricval and youval > josval:
                        print('You win!')
                        money = money +pot
                        pot = 0
                    if ricval > youval and ricval > josval:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                    if josval > youval and josval > ricval:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                    break
                if y == 'drop':
                    f= 1
                
            print('The pot is $',pot)
            
            print("Ricardo's turn")
            
            ppp = random.randint(1,5)
            if opo !=0:
                if ppp == 1:
                    print('Ricardo put in $10')
                    rmoney = rmoney-10
                    pot = pot +10
                if ppp == 2:
                    print('Ricardo put in $100')
                    rmoney = rmoney-100
                    pot = pot +100
                if ppp == 3:
                    print('Ricardo put in $500')
                    rmoney = rmoney-500
                    pot = pot +500
                if rmoney < 0:
                    print('Ricardo is bankrupt...')
                    break
                if ppp == 4:
                    rmoney = rmoney - 20
                    print('Ricardo wants to show')
                    print('Are you ready? - yes-')
                    qpqpqp = input()
                    if qpqpqp == 'yes':
                        print("Josh's cards are...")
                        print(mm, nn)
                        print(oo, pp)
                        print(qq, rr)
                        print(ss, tt)
                        print(uu, vv)
                        print("Ricardo's cards are... say yes to continue")
                        qpqpqp = input()
                        if qpqpqp == 'yes':
                            print("Ricardo's cards are...")
                            print(m, n)
                            print(o, p)
                            print(q, r)
                            print(s, t)
                            print(u, v)
                            print('And your cards are... say yes to continue')
                            qpqpqp = input()
                        if qpqpqp == 'yes':
                            print("Your cards are...")
                            print(c, d)
                            print(e, f)
                            print(g, h)
                            print(i, j)
                            print(k, l)
                    if (c and e and g and i and k == c) and (d and f and h and j and l == d):
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if (m and o and q and s and u == m) and (n and p and r and t and v == n):
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if (mm and oo and qq and ss and uu == mm) and (nn and pp and rr and tt and vv == nn):
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    if c and e and g and i and k == c:
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if m and o and q and s and u == m:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if mm and oo and qq and ss and uu == mm:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    if d and f and h and j and l == d:
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if n and p and r and t and v == n:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if nn and pp and rr and tt and vv == nn:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    K = 'K'
                    Q = 'Q'
                    J = 'J'
                    A = 'A'
                    K = 13
                    Q = 12
                    J = 11
                    A = 14
                    youval = c+ e + g +i + k 
                    ricval = m+ o + q +s + u 
                    josval = mm+ oo + qq +ss + uu 
                    if youval > ricval and youval > josval:
                        print('You win!')
                        money = money +pot
                        pot = 0
                    if ricval > youval and ricval > josval:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                    if josval > youval and josval > ricval:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                    break
                if ppp == 5:
                    opo= 0
                    print('Ricardo has dropped out')
                print('Ricardo has $',rmoney)
            print('The pot is $',pot)
            print("Josh's turn")
            ppp = random.randint(1,5)
            if opop !=0:
                if ppp == 1:
                    print('Josh put in $10')
                    jmoney = jmoney-10
                    pot = pot +10
                if ppp == 2:
                    print('Josh put in $100')
                    jmoney = jmoney-100
                    pot = pot +100
                if ppp == 3:
                    print('Josh put in $500')
                    jmoney = jmoney-500
                    pot = pot +500
                if jmoney < 0:
                    print('Josh is bankrupt...')
                    break
                if ppp == 4:
                    jmoney = jmoney - 20
                    print('Josh wants to show')
                    print('Are you ready? - yes-')
                    qpqpqp = input()
                    if qpqpqp == 'yes':
                        print("Josh's cards are...")
                        print(mm, nn)
                        print(oo, pp)
                        print(qq, rr)
                        print(ss, tt)
                        print(uu, vv)
                        print("Ricardo's cards are... say yes to continue")
                        qpqpqp = input()
                        if qpqpqp == 'yes':
                            print("Ricardo's cards are...")
                            print(m, n)
                            print(o, p)
                            print(q, r)
                            print(s, t)
                            print(u, v)
                            print('And your cards are... say yes to continue')
                            qpqpqp = input()
                        if qpqpqp == 'yes':
                            print("Your cards are...")
                            print(c, d)
                            print(e, f)
                            print(g, h)
                            print(i, j)
                            print(k, l)
                    if (c and e and g and i and k == c) and (d and f and h and j and l == d):
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if (m and o and q and s and u == m) and (n and p and r and t and v == n):
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if (mm and oo and qq and ss and uu == mm) and (nn and pp and rr and tt and vv == nn):
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    if c and e and g and i and k == c:
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if m and o and q and s and u == m:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if mm and oo and qq and ss and uu == mm:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    if d and f and h and j and l == d:
                        print('You win!')
                        money = money +pot
                        pot = 0
                        break
                    if n and p and r and t and v == n:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                        break
                    if nn and pp and rr and tt and vv == nn:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                        break
                    K = 'K'
                    Q = 'Q'
                    J = 'J'
                    A = 'A'
                    K = 13
                    Q = 12
                    J = 11
                    A = 14
                    youval = c+ e + g +i + k 
                    ricval = m+ o + q +s + u 
                    josval = mm+ oo + qq +ss + uu 
                    if youval > ricval and youval > josval:
                        print('You win!')
                        money = money +pot
                        pot = 0
                    if ricval > youval and ricval > josval:
                        print('Ricardo wins!')
                        rmoney = rmoney +pot
                        pot = 0
                    if josval > youval and josval > ricval:
                        print('Josh wins!')
                        jmoney = jmoney +pot
                        pot = 0
                    break
                if ppp == 5:
                    print('Josh has dropped out')
                    opop= 0
            print('Josh has $',jmoney)
            print( 'The pot is $',pot)


            
