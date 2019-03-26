num_lines = sum(1 for line in open('liste_francais.txt', 'r', encoding = "ISO-8859-15"))
f = open('liste_francais.txt', 'r', encoding = "ISO-8859-15")
lines = f.readlines()

wrd = input('> ')
wrd = wrd.lower()
w = 0
i = 0

if wrd + '\n' not in lines and wrd not in lines:
	print('Mot non reconnu !')
	exit()

while w == 0:
	if lines[i] == wrd + '\n' or lines[i] == wrd:
		w = 1
	i = i + 1

print('Lignes : ', end='')
print(i)
print('Etapes : ', end='')
print(i)