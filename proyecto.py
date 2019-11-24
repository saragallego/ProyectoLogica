import libreria.py
from copy import deepcopy


def letrasProposicionales(disco, posicion, torre, ronda):
    letras = []
    primera_ronda = True
    for r in ronda:
        if primera_ronda:
            for d in disco:
                letras.append(d + posicion[disco.index(d)] + torre[0] + r)
                primera_ronda = False
        else:
            for t in torre:
                for p in posicion:
                    if int(r)%2 == 0:
                        letras.append(disco[0] + p + t + r)
                    else:
                        letras.append(disco[1] + p + t + r)
    return letras

def regla_movimiento(letras, ronda):
    inicial = True
    regla = ""
    for i in range(2,len(ronda)+1):
        aux1 = [x for x in letras if int(x[3]) == i]
        for p in aux1:
            regla_ronda = p
            aux2 = [x + "-" for x in aux1 if x != p]
            for q in aux2:
                regla_ronda = q + regla_ronda + "Y"
            if inicial:
                regla = regla_ronda
                inicial = False
            else:
                regla = regla_ronda + regla + "O"
    return regla

def regla_cantidad_posicion(letras, posicion, torre, ronda):
    inicial = True
    regla = ""
    for i in range(1,len(ronda)):
        aux1disco1 = [x for x in letras if int(x[3]) == i]
        aux1disco2 = [x for x in letras if int(x[3]) == i + 1]
        for j in range(len(torre)):
            aux2disco1 = [x for x in aux1disco1 if torre.index(x[2]) == j]
            aux2disco2 = [x for x in aux1disco2 if torre.index(x[2]) == j]
            for p in aux2disco1:
                regla_posicion = p
                aux3 = [x + "-" for x in aux2disco2 if x[1] == p[1]]
                for q in aux3:
                    regla_posicion = q + regla_posicion + ">"
                if inicial:
                    regla = regla_posicion
                    inicial = False
                else:
                    regla = regla_posicion + regla + "Y"
    return regla

def regla_tamaño(letras, disco, torre):
    inicial = True
    regla = ""
    for i in range(2, len(ronda)):
        aux1disco1 = [x for x in letras if int(x[3]) == i]
        aux1disco2 = [x for x in letras if int(x[3]) == i + 1]
        for j in range(len(torre)):
            aux2disco1 = [x for x in aux1disco1 if torre.index(x[2]) == j]
            aux2disco2 = [x for x in aux1disco2 if torre.index(x[2]) == j]
            for p in aux2disco1:
                regla_posicion = p
                negaciones = ""
                primera = True
                aux3 = [x + "-" for x in aux2disco2 if (disco.index(p[0]) < disco.index(x[0]))]
                for q in aux3:
                    if primera:
                        negaciones = q
                        primera = False
                    else:
                        negaciones = q + negaciones + "Y"
                    regla_posicion = negaciones + regla_posicion + ">"
                    if inicial:
                        regla = regla_posicion
                        inicial = False
                    else:
                        regla = regla_posicion + regla + "Y"
    return regla

def regla_tamano(letras, disco, torre):
  inicial = True
  regla = ""
  for i in range(2, len(ronda)):
      aux1disco1 = [x for x in letras if int(x[3]) == i]
      aux1disco2 = [x for x in letras if int(x[3]) == i + 1]
      for j in range(len(torre)):
          aux2disco1 = [x for x in aux1disco1 if torre.index(x[2]) == j]
          aux2disco2 = [x for x in aux1disco2 if torre.index(x[2]) == j]
          for p in aux2disco1:
              regla_posicion = p
              negaciones = ""
              primera = True
              aux3 = [x + "-" for x in aux2disco2 if (disco.index(p[0]) < disco.index(x[0])) and int(p[1]) > int(x[1])]
              if len(aux3) > 0:
                  for q in aux3:
                      if primera:
                          negaciones = q
                          primera = False
                      else:
                          negaciones = q + negaciones + "Y"
                  regla_posicion = negaciones + regla_posicion + ">"
                  if inicial:
                      regla = regla_posicion
                      inicial = False
                  else:
                      regla = regla_posicion + regla + "Y"
  return regla

def regla_final(letras, disco, ronda):
    inicial = True
    regla = ""
    aux1 = [x for x in letras if x[2] == "c"]
    aux2 = [x for x in aux1 if (int(x[3]) + disco.index(x[0])) == len(ronda)]
    correctas = [x for x in aux2 if (disco.index(x[0]) + 1) == int(x[1])]
    incorrectas = [x + "-" for x in aux2 if x not in correctas]
    for p in correctas:
        if inicial:
            regla = p
            inicial = False
        else:
            regla = p + regla + "Y"
    for q in incorrectas:
        regla = q + regla + "Y"
    return regla


disco = ["a", "b"]
posicion = [str(i) for i in range(1, len(disco)+1)]
torre = ["a", "b", "c"]
ronda = ["1", "2", "3", "4"]

letrask = letrasProposicionales(disco, posicion, torre, ronda)
regla_movimiento(letrask, ronda)
regla_cantidad_posicion(letrask, posicion, torre, ronda)
regla_tamano(letrask, disco, torre)



letrasprop ={"a1a1" : 'a', "b2a1" : 'b', "a1a2" : 'c' ,"a2a2" : 'd',"a1b2" : 'e',"a2b2" : 'f' ,"a1c2" : 'g', "a2c2" : 'h', "b1a3" : 'i', "b2a3" : 'j', "b1b3" : 'k' ,"b2b3" : 'l',"b1c3" : 'm',"b2c3" : 'n',"a1a4" : 'o',"a2a4" : 'p',"a1b4" : 'q',"a2b4" : 'r',"a1c4" : 's',"a2c4" : 't'}


#regla = "n>m>l>k>j>i>n-m-YYh>n-m-Yi>n-m-Yh>n-m-Yg>l-k-Yf>l-k-Ye>j-i-Yd>j-i-Yc>YYYYYYYYYYY"
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']

#REGLAS
a = regla_final(letrask, disco, ronda)
b = regla_tamano(letrask, disco, torre)
c = regla_movimiento(letrask, ronda)
d = regla_cantidad_posicion(letrask, posicion, torre, ronda)

#print (a)
#print (b)
#print (c)
#print (d)

# REESCRIBIENDO REGLAS
# REGLAS a

def convert(a):
	conectivos = ["Y", "O", ">"]
	f = ""
	i = 0

	while len(a) > 0:
		if a[i] in conectivos:
			f += a[i]
			a = a[1:]
		elif a[i] + a[i+1]+ a[i+2]+ a[i+3]  in letrasprop:
			 e = letrasprop[a[i] + a[i+1]+ a[i+2]+ a[i+3]]
			 if a[i+4] == "-":
			 	e = e + "-"
			 	if len(a) > 5:
			 		a = a[5:]
			 else:
			 	if len(a) > 4:
			 		a = a[4:]
			 f += e
	return f

ac = convert(a)
bc = convert(b)
cc = convert(c)
dc = convert(d)

#print(ac)
#print(bc)
#print(cc)
#print(dc)

final = ac + bc + cc + dc + "YYY"

print()
print("################################")
print()

print(final)


print()
print("################################")
print()

h = string2Tree(final)
h1 = Inorder(h)
h2 = Tseitin1(h1, letras)
h3 = formaClausal(h2)
dpll = DPLL(h3, {})
print(dpll)
print()

def diccionario(dic): #retorna un diccionario con los valores de las 64 letras proposicionales.
    d = {}
    for n in dic.keys():
        if n in letras:
            d[n] = dic[n]
    return d

print(dpll[1])

print(diccionario(dpll[1]))
