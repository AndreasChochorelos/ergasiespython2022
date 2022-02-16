import random

figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]


# 1
print('First stage of the game: ')

p1wins = 0 #nikes tou 1ou paikti
p2wins = 0 #nikes tou 2ou paikti
draws = 0 #isopalies

'''o kwdikas pou eixame'''
for games in range(100):
  cards = []
  for i in xarti:
    for j in color:
      cards.append([i,j])
        
  random.shuffle(cards)

  player1 = []
  sum1 = 0
  while sum1 < 16:
    sum1 = 0
    player1.append(cards.pop())

    for card in player1:
      if card[0] in figures:
        sum1 = sum1 + 10
      else:
        sum1 = sum1 + card[0]

  if sum1 > 21:
    print("Player 2 wins!")
    p2wins += 1
  elif sum1 == 21:
    print("Player 1 wins!") #an petuxei 21 tote kerdise, den uparxei nohma na sunexistei to paixnidi
    p1wins += 1
  else:
    player2=[]
    sum2 = 0

    while sum2 < 16:
      sum2 = 0
      player2.append(cards.pop())
      
      for card in player2:
        if card[0] in figures:
          sum2 = sum2 + 10
        else:
          sum2 = sum2 + card[0]

    if sum2 > 21:
      print("Player 1 wins!")
      p1wins += 1
    else:
      if sum2 == 21:
        print("Player 2 wins!") #an petuxei 21 tote kerdise, den uparxei nohma na sunexistei to paixnidi
        p2wins +=1
      elif sum1 > sum2:
        print("Player 1 wins!")
        p1wins += 1
      elif sum2 > sum1:
        print("Player 2 wins!")
        p2wins += 1
      else:
        print("It's a draw")
        draws += 1

print(' ')
print('Player 1 wins: ', p1wins, 'or', (p1wins/100)*100, '%')
print('Player 2 wins: ', p2wins, 'or', (p2wins/100)*100, '%')
print('Draws: ', draws, 'or', (draws/100)*100, '%')


# 2
print(' ')
print(' ')
print('Second stage of the game: ')

p1wins = 0
p2wins = 0
draws = 0

card1 = [10] + figures
'''bazoume se mia lista to 10 mazi me tis figoures gia na ginei argotera mia 
   random epilogi gia to fullo tou 1ou paikth'''

for games in range(100):
  cards = []
  for i in xarti:
    for j in color:
      cards.append([i,j])
        
  random.shuffle(cards)

  player1 = []
  sum1 = random.choice(card1) #random epilogi (pou eipa prin) anamesa se 10, J, Q kai K
  
  if sum1 in figures: #oi figoures exoun aksia 10 kai to sum prepei na einai integer gia th while sun8iki
    sum1 = 10
  '''
  sxetika me thn parapanw if:
  skeftika na balw kateu8eian to sum = 10 giati kai ta 4 fulla exoun aksia 10. Alla epeidi stin ekfwnisi lete
  "10 h figoura" eipa na pros8esw auto to bhma gia sigouria
  '''

  cards.remove(cards[-1])
  '''
  gia to cards.remove(cards[-1]):
  me ton tropo pou to exw kanei (xrisimopoiw to sum) einai san oi paiktes na exoun trabhksei hdh to 1o fullo afou, 
  to 1o tou fullo tou 1ou paikth tha einai 10 h figoures kai tou 2ou tha einai kati apo 2 ews kai 9
  '''

  while sum1 < 16:
    sum1 = 10 
    '''ksekinaw to sum me 10 afou auth thn aksia 8a exei to 1o fullo.
       kai ta 4 fulla exoun aksia 10 opote den ksanaekana tin if edw'''
    player1.append(cards.pop())

    for card in player1:
      if card[0] in figures:
        sum1 = sum1 + 10
      else:
        sum1 = sum1 + card[0]
      
  if sum1 > 21:
    print("Player 2 wins!")
    p2wins += 1
  elif sum1 == 21:
    print("Player 1 wins!")
    p1wins += 1
  else:
    player2=[]
    sum2 = random.randint(2,9) #random ari8mos apo to 2 mexri kai to 9

    cards.remove(cards[-1]) #idia eksigisi me panw

    while sum2 < 16:
      sum2 = random.randint(2,9)
      player2.append(cards.pop())
      
      for card in player2:
        if card[0] in figures:
          sum2 = sum2 + 10
        else:
          sum2 = sum2 + card[0]

    if sum2 > 21:
      print("Player 1 wins!")
      p1wins += 1
    else:
      if sum2 == 21:
        print("Player 2 wins!")
        p2wins += 1
      elif sum1 > sum2:
        print("Player 1 wins!")
        p1wins += 1
      elif sum2 > sum1:
        print("Player 2 wins!")
        p2wins += 1
      else:
        print("It's a draw")
        draws += 1

print(' ')
print('Player 1 wins: ', p1wins, 'or', (p1wins/100)*100, '%')
print('Player 2 wins: ', p2wins, 'or', (p2wins/100)*100, '%')
print('Draws: ', draws, 'or', (draws/100)*100, '%')