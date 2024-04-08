f = "a b+b_ c+a c_"
liste = f.split("+")
element = []
for i in liste:
	s = i.split(" ")
	for j in s:
		if j not in element:
			element.append(j)

liste_bin = []
for i in range(8):
	j = bin(i)[2:]
	if len(j) == 1:
		j = "00"+j
	elif len(j) == 2:
		j = "0"+j
	liste_bin.append(j)
element.sort(key=lambda x:len(x))
liste_total = []
for i in element:
	liste_total.append(i)
for i in liste:
	liste_total.append(i)
liste_total.append('f')
l_final = []
for i in range(8):
	d = {}
	premier_indice = liste_bin[i]
	tmp = []
	for j in range(8):
		if j in [0,1,2]:
			d[liste_total[j]] = int(premier_indice[j])
		elif j in [3,4]:
			if liste_total[j] == "b_":
				d[liste_total[j]] = 1 if d['b'] == 0 else 0
			elif liste_total[j] == "c_":
				d[liste_total[j]] = 1 if d['c'] == 0 else 0
		else:
			p , m = liste_total[j].split(" ")
			d[liste_total[j]] = d[p]&d[m]
			tmp.append(d[p]&d[m])
		if len(tmp) == 3:
			d['f']=tmp[0]|tmp[1]|tmp[2]
			tmp = []
			l_final.append(d)

print("\t".join(liste_total))
print("-"*70)
for i in l_final:
	c = []
	for j in range(len(i)):
		c.append(str(i[liste_total[j]]))
	print("\t".join(c))

ass = []
for i in l_final:
	a = i['a']
	b = i['b']
	c = i['c']
	chaine = ""
	if a == 0:
		chaine += "a_"
	else:
		chaine += "a"
	if b == 0:
		chaine += "b_"
	else:
		chaine += "b"
	if c == 0:
		chaine += "c_"
	else:
		chaine += "c"
	ass.append(chaine)
res = []
res2= []
index = 0
for i in l_final:
	resultat = i['f']
	if resultat == 1:
		res.append(ass[index])
	else:
		res2.append(ass[index])
	index+=1
index = 0
for i in res2:
	i = i.replace("a_","x").replace("b_","y").replace("c_","z").replace("a","1").replace("b","2").replace("c","3")
	i = f"({i})"
	res2[index] = "+".join(i).replace("(+","(").replace("+)",")").replace("x","a").replace("y","b").replace("z","c").replace("1","a_").replace("2","b_").replace("3","c_")
	index+=1

print("premiere forme canonique : ")
print(" + ".join(res))

print("seconde forme canonique : ")
print(" ".join(res2))
