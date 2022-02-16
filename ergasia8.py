import random

whiteRook = 'White Rook' #aspros pirgos
blackBishop = 'Black Bishop' #mauros aksiwmatikos

'''ftiaxnw sunartisi gia na mhn kanw 3 fores to idio pragma'''
def chessTable(width, height, chessTable):
  setting = 0 #an o pinakas einai 7x7 h 8x8 to setting=0

  if width == 7 and height == 8: #an o pinakas einai 7x8 kanw to setting=1
    setting = 1

  '''dimiourgw th lista skaki vazontas height listes me width stoixeia mesa se autes ta opoia einai kena'''
  chess = [] #to skaki
  for y in range(height):
    chess.append([])
    for x in range(width):
      chess[y].append('   ')

  '''ta vazw -1 giati to randint den einai opws to range pou bazeis px 8 kai pairnei apo 0 ews 7,
     pairnei kai to 8 (an px width=8 kai height=8). Efoson loipon dinw suntetagmenes prepei na eimai
     entos tou index tou chess, 0-7 dhladh'''
  #se ola kanei random pick enan arithmo
  whiteX = random.randint(0,width-1) #to x tou asprou pirgou
  whiteY = random.randint(0,height-1) #to y tou pirgou
  blackX = random.randint(0,width-1) #to x tou maurou aksiwmatikou
  blackY = random.randint(0,height-1) #to y tou aksiwmatikou

  #bazw ta pionia stis random suntetagmenes mesa sto chess
  chess[whiteY][whiteX] = whiteRook
  chess[blackY][blackX] = blackBishop

  playersTurn = whiteRook #poianou paikti einai h seira
  whiteWins = 0 #nikes pirgou
  blackWins = 0 #nikes aksiwmatikou

  for i in range(100):
    playerWon = True #an kanpoios kerdisei stamataei o giros kai pame sto epomeno game

    #gia kathe game vazw random suntetagmenes
    whiteX = random.randint(0,width-1)
    whiteY = random.randint(0,height-1)
    blackX = random.randint(0,width-1)
    blackY = random.randint(0,height-1)

    #bazw ta pionia sto chess
    chess[whiteY][whiteX] = whiteRook
    chess[blackY][blackX] = blackBishop

    while playerWon: #oso den exei kerdisei akoma kanenas paiktis ton giro
      if (playersTurn == whiteRook): #seira asprou
        playersTurn = blackBishop #allazw th seira
        for position in range(width): #xrhsimopoiw to width gia na mhn bgw out of range ston pinaka 7x8
          '''
          sxetika me thn parakatw if:
          elegxw na o aksiwmatikos brisketai sto range pou kineitai o pirgos
          prospa8isa na to kanw leitourgiko gia olous tous pinakes epomenws:
          o pirgos paei panw katw deksia aristera ara:
          1. tsekarw ton aksona x (afhnw to y idio)
          2. tsekarw ton aksona y (afhnw to x idio). Alla epeidh ston pinaka 7x8 to y einai parapanw apo to x
          to setting ginetai 1(stin arxh ths sunarthshs) kai prosti8etai sto position pou einai apo 0-6 gia
          na mporesw na tsekarw to epipleon koutaki pou mou menei. An o pinakas den einai 7x8 tote to setting=0
          kai den allazei kati
          3. epeidh pros8etw to setting=1 gia pinaka 7x8 to y den koitaei to 0 arxika, opote ebala allon enan elegxo
          me y=0 gia na tsekaretai kai auto
          '''
          if chess[whiteY][position] == chess[blackY][position] or chess[position+setting][whiteX] == chess[position+setting][blackX] or chess[0][whiteX] == chess[0][blackX]:
            whiteWins += 1 #kerdizei to aspro
            playerWon = False #teleiwse o giros
            break #teleiwnei o giros
      else: #seira maurou
        playersTurn = whiteRook #allazw th seira
        for position in range(width): #xrhsimopoiw to width gia na mhn bgw out of range ston pinaka 7x8
          '''
          sxetika me thn parakatw if:
          elegxw na o pirgos brisketai sto range pou kineitai o aksiwmatikos
          o aksiwmatikos paei loksa ara:
          1. tsekarw gia loksa pros ta mprosta (to x kai y tha exoun thn idia timh)
          2. tsekarw gia loksa pros ta pisw afairontas apo thn telikh timh (width) to position pou auksanetai
          kai bazw kai -1 gia na mhn bgw ektos tou pinaka afou to range(width) ftanei apo 0 ews width-1
          '''
          if chess[position][position] == chess[whiteY][whiteX] or chess[width-position-1][width-position-1] == chess[whiteY][whiteX]:
            blackWins += 1  #kerdizei to mauro
            playerWon = False #teleiwse o giros
            break #teleiwnei o giros

  #emfanizw ta apotelesmata
  print('For', chessTable, 'chess:')
  print(whiteRook, 'won', whiteWins, 'times!')
  print(blackBishop, 'won', blackWins, 'times!')

#kalw ti sunarthsh me ta dedomena tou kathe pinaka
chessTable(8, 8, '8x8')
print(' ')
chessTable(7, 7, '7x7')
print(' ')
chessTable(7, 8, '7x8')