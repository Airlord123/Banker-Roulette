import random
print('Hello and welcome to the bankers roulette, please enter any 5 freinds names')
freind1 = input('\nfreind 1: ')
freind2 = input('\nfreind 2: ')
freind3 = input('\nfreind 3: ')
freind4 = input('\nfreind 4: ')
freind5 = input('\nfreind 5: ')
freinds = [freind1, freind2, freind3, freind4, freind5]
Roulette_looser = freinds[random.randint(0,4)] 

print(Roulette_looser +', pays the total bill' )
