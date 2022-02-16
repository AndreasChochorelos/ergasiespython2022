from collections import Counter

myList1 = [] #lista me tis lekseis
twoLetters = [] #lista me ta 2 prwta grammata olwn ton leksewn
threeLetters=[] #lista me ta 3 prwta grammata olwn ton leksewn

#tha xreiastei na allaksete to path
with open('C:\\Users\\aapos\\Desktop\\PYTHON\\ergasia5\\two_cities_ascii.txt', 'r') as file: #diavazw to file
    for line in file: #gia kathe grammh
        for word in line.split(): #kane split tin kathe leksh
            if word.isalpha(): #an einai mono grammata
                myList1.append(word.lower()) #bale th sti lista

# a
'''xrhsimopoioume tin class Counter h opoia pairnei th lista kai mas gurizei to poses fores
uparxei to kathe stoixeio mesa se auth'''
words = Counter(myList1)
'''xrhsimopoioume thn most_common gia na broume ta n (edw n=10) stoixeia pou uparxoun perissoteres
   fores sth words pou exei ta stoixeia pou mas epestrepse h Counter'''
most_common = words.most_common(10)
print('The 10 most common words are:', most_common)

# b 
for i in range(len(myList1)): #pernaw apo oles tis lekseis ths listas
    if len(myList1[i]) > 1: #an h leksh exei toulaxiston 2 grammata
        twoLetters.append(myList1[i][0:2]) #tote ta 2 prwta grammata bale ta sth lista twoLetters

#kai kanw to idio pragma me prin xrhsimopoiwntas thn twoLetter list pou exei ta 2 prwta grammata kathe lekshs
letters2 = Counter(twoLetters)
most_common_two_letters = letters2.most_common(3)
print('The 3 most commmon 2-letter combinations are:', most_common_two_letters)

# c
#kanw to idio akribws pragma me to #b
for i in range(len(myList1)):
    if len(myList1[i]) > 2:
        threeLetters.append(myList1[i][0:3])

letters3 = Counter(threeLetters)
most_common_three_letters = letters3.most_common(3)
print('The 3 most commmon 3-letter combinations are:', most_common_three_letters)
