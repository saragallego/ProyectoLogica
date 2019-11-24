class Tree():
    def __init__(self,label,iz,der):
        self.label = label
        self.left = iz
        self.right = der

def string2Tree(A):
    conectivos = ["Y","O",">"]
    stack = []
    for c in A:
    	if c in letras:
    		stack.append(Tree(c,None,None))
    	elif c == "-":
    		formaux = Tree(c, None, stack[-1])
    		del stack[-1]
    		stack.append(formaux)
    	elif c in conectivos:
    		formaux = Tree(c, stack[-1], stack[-2])
    		del stack[-1]
    		del stack[-1]
    		stack.append(formaux)
    return stack[-1]

def Inorder(arbol):
	conectivosBinarios = ["Y","O",">"]
	if arbol.label in letras:
		return arbol.label
	elif arbol.label == "-":
		return arbol.label+Inorder(arbol.right)
	elif arbol.label in conectivosBinarios:
		return "("+Inorder(arbol.left)+arbol.label+Inorder(arbol.right)+")"
	else:
		print("Oops, rotulo incorrecto")

def hay_clausula_unit(lista):
	for n in lista:
		#print(n)
		if len(n) == 1:
			return True
	return False


def complemento(n):
	x = n#[0]
	if x[0] == '-':
		return x[1]
	else:
		return '-' + x


def unit_propagate(S, I):
	#print("Haciendo unit propagate")
	#print(S, I)
	c_vacio = []
	aux = hay_clausula_unit(S)
	#print(aux)
	while(c_vacio not in S and aux):
		for n in S:
			if len(n) == 1:
				l = n[0]
		S = [y for y in S if l not in y]
		for w in S:
			if complemento(l) in w:
				w.remove(complemento(l))
		if l[0] == '-':
			I[l[1]] = 0
		else:
			I[l] = 1
		aux = hay_clausula_unit(S)
	return S, I


def DPLL(S, I):
	S, I = unit_propagate(S, I)
	c_vacio = []
	if c_vacio in S:
		return "Insatisfacible", {}
	elif len(S) == 0:
		return "Satisfacible", I
	l = ""
	for n in S:
		for x in n:
			if x not in I.keys():
				l = x
	lBarra = complemento(l)
	if l == "":
		print("Oh oh, problemas...")
		return None
	Sp = deepcopy(S)
	Sp = [n for n in Sp if l not in n]
	for m in Sp:
		if lBarra in m:
			m.remove(lBarra)
	Ip = deepcopy(I)
	if l[0] == '-':
		Ip[l[1]] = 0
	else:
		Ip[l] = 1

	S1, I1 = DPLL(Sp, Ip)
	if S1 == "Satisfacible":
		return S1, I1
	else:
		Spp = deepcopy(S)
		for a in Spp:
			if complemento(l) in a:
				Spp.remove(a)
		for b in Spp:
			if l in b:
				b.remove(l)
		Ipp = deepcopy(I)
		if l[0] == '-':
			Ipp[l[1]] = 0
		else:
			Ipp[l] = 1
		return DPLL(Spp, Ipp)


def enFNC(A):
    #assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    #print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 500000)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    L =[]
    Pila = []
    i = -1
    s = A[0]
    #atomo = letrasProposicionalesA + letrasProposicionalesB
    while len(A) > 0:
        if s in (letrasProposicionalesA or letrasProposicionalesB) and Pila[-1] == '-' and len(Pila) > 0:#modificacion.
            i += 1
            atomo = letrasProposicionalesB[i]
            Pila = Pila[:-1]
            Pila.append(atomo)
            L.append(atomo+'='+'-'+s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            w = Pila[-1]
            o = Pila[-2]
            v = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo + "=" + "(" + v + o + w + ")")
            s = atomo
        else:
            Pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    B = ''
    if i < 0:
        atomo = Pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for X in L:
        Y = enFNC(X)
        B += "Y" + Y
    B = atomo + B
    return B
    return "OK"

def Clausula(C):
    L = []
    while len(C) > 0:
        s = C[0]
        if s == "O":
            C = C[1:]
        elif s == "-":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L
    return "OK"

def formaClausal(A):
    L = []
    i = 0
    while len(A) > 0:
        if i >= len(A):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == "Y":
                L.append(Clausula(A[:i]))
                A = A[i + 1:]
                i = 0
            else:
                i += 1
    return L
    return "OK"
