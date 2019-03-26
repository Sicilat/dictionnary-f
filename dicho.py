num_lines = sum(1 for line in open('liste_francais.txt', 'r', encoding = "ISO-8859-15"))
f = open('liste_francais.txt', 'r', encoding = "ISO-8859-15")
lines = f.readlines()

wrd.lower() = input('> ')
p = int(num_lines / 2)
min0 = 0
max0 = num_lines
w = 0
i = 0

if wrd + '\n' not in lines:
	print('Mot non reconnu !')
	exit()

while w == 0:
	i += 1
	if lines[p] == wrd + '\n':
		w = 1
	elif lines[p] > wrd + '\n':
		max0 = p
	else:
		min0 = p
	p = int((max0 - min0) / 2) + min0

p = p + 1
print('Lignes : ', end='')
print(p)
print('Etapes : ', end='')
print(i)