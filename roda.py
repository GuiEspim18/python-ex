import csv
import random

words = [
    "Suricato",
    "Mosquito",
    "Lombriga"
]

players = []

contentWords = []

with open("words.csv", "r") as file:
    read = csv.reader(file)
    num = 0
    for i in read:
        if len(i) > 0: 
            contentWords.append(dict(words= i, num= num))
            num += 1

sortWord = random.randint(1, 3)
sortedWord = contentWords[sortWord]
answer = []
panel = "\n"
roda = []
sortedItem = ""
letter = ""
wordIndex = 0

with open("opts.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")
    for i in lines:
        if i.strip():
            roda.append(i)
        

for i in range(8):
    answer.append("")

for i in range(len(answer)):
    panel += "_ "

print("Digite o nome de 3 jogadores:")
for i in range(3): 
    pname = input(f"Jogador {i+1}: ")
    players.append(dict(name= pname, pts=0)) 

match sortWord:
    case 1:
        print("\nMamífero")
    case 2:
        print("\nInseto")
    case 3:
        print("\nParasita")

print(panel)

sort = int(random.randint(1, len(players)) -1)
sorted = players[sort]
print(f"\nO jogador {sorted['name']} vai começar!")
print(f"\nDigite {sorted['name']} '0' para rodar a roda:")
spin = int(input())
if spin != 0:
    print(f"\nDigite {sorted['name']} '0' para rodar a roda:")
    spin = int(input())
else:
    sortItem = random.randint(1, len(roda)) - 1
    sortedItem = roda[sortItem]
if sortedItem != "Perde tudo" and sortedItem != "Passa a vez":
    print(f"\nCaiu {sortedItem}")
    letter = input("Escolha uma letra: ")
    qtds = 0
    wordIndex = 0
    for i in sortedWord['words']:
        if i.lower() == letter.lower():
            qtds += 1
        wordIndex += 1
    sorted['pts'] = int(sortedItem)*qtds
    if wordIndex != 0:
        answer[wordIndex-1] = letter.lower()
    else:
        answer[wordIndex-1] = letter.upper()
else:
    print(f"\nCaiu {sortedItem}")
    if sortedItem == "Perde tudo":
        sorted['pts'] = 0
pindex = 0
for i in players:
    if i == sorted:
        break
    pindex += 1
if pindex+1 == len(players):
    sorted = players[0]
else:
    sorted = players[pindex+1]

print(answer)
     
