from sys import*

token = []
symbols = {}
loop = []

def open_file(filename):
	data = open(filename,"r").read()
	data+= "<EOF>"
	return data

def lex(filecontent):
		#ExpressionHolders
		tok = ""
		string = ""
		expr = ""
		var = ""
		#bools
		varstarted = 0
		state = 0
		Isexpr = 0
		filecontent = list(filecontent)
		for char in filecontent:
			tok += char
			if tok == " ":
				if state == 0:
					tok = ""
				elif state == 1:
					tok = " "
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
			elif tok == "\t":
				if state == 0:
					tok = ""
				elif state == 1:
					tok = "\t"
				if var != "":
					token.append("VAR:"+var)
					var = ""
			elif tok == "\n" or tok == "<EOF>":
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				elif expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				elif var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				tok = ""
			elif tok == "<" and state == 0:
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				token.append("CON:LST")
				tok = ""
			elif tok == ">" and state == 0:
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				token.append("CON:GRT")
				tok = ""
			elif tok == "!=" and state == 0:
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				token.append("CON:NTE")
				tok = ""
			elif tok == "=" and state == 0:
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				if token[-1] == "EQL:":
					token[-1] = "CON:DQL"
				elif token[-1] == "CON:GRT":
					token[-1] = "CON:GRE"
				elif token[-1] == "CON:LST":
					token[-1] = "CON:LSE"
				else:
					token.append("EQL:")
				tok = ""
			elif tok == "#" and state == 0:
				varstarted = 1
				var += tok
				tok = ""
			elif varstarted == 1:
				if tok == "<" or tok == ">":
					if var != "":
						token.append("VAR:"+var)
						var = ""
						varstarted = 0
				var += tok
				tok = ""
			elif tok == "expose" or tok == "EXPOSE":
				token.append("DIS:")
				tok = ""
			elif tok == "wonder" or tok == "WONDER":
				token.append("IIF:")
				tok = ""
			elif tok == "loop" or tok == "LOOP":
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				token.append("LOP:")
				tok = ""
			elif tok == "to" or tok == "TO":
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				token.append("TIL:")
				tok = ""
			elif tok == "endloop" or tok == "ENDLOOP":
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				token.append("ELP:")
				tok = ""
			elif tok == "next" or tok == "NEXT":
				if expr != "" and Isexpr == 0:
					token.append("NUM:" + expr)
					expr = ""
				if expr != "" and Isexpr == 1:
					token.append("EXP:" + expr)
					expr = ""
					Isexpr = 0
				if var != "":
					token.append("VAR:"+var)
					var = ""
					varstarted = 0
				token.append("THN:")
				tok = ""
			elif tok == "ender" or tok == "ENDER":
				token.append("EIF:")
				tok = ""
			elif tok == "get" or tok == "GET":
				token.append("GET:")
				tok = ""
			elif state == 0 and (tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9"):
				expr += tok
				tok = ""
			elif state == 0 and (tok == "+" or tok == "-" or tok == "*" or tok == "/" or tok == "(" or tok == ")" or tok == "%"):
				Isexpr = 1
				expr += tok
				tok = ""
			elif tok == "\"" or tok == " \"":
				if	state == 0:
					state = 1
				elif state == 1:
					if tok=="\"":
						token.append("STR:"+string+"\"")
					else:
						token.append("STR:"+string+" \"")
					string = ""
					state = 0
					tok = ""
			elif state == 1:
				string += tok
				tok = ""
		print(token)
		#return ''
		return token

def doPRINT(toPrint):
	if toPrint[0:4] == "STR:":
		toPrint = toPrint[5:-1]
	elif toPrint[0:4] == "EXP:":
		toPrint = doEvaluate(toPrint[4:])
	elif toPrint[0:4] == "NUM:":
		toPrint = toPrint[4:]
	print(toPrint)
		
def doEvaluate(toEvaluate):
	return str(eval(toEvaluate))

def doAssign(VarName, VarValue):
	if VarValue[0:4] == "STR:":
		VarValue = VarValue[5:-1]
	elif VarValue[0:4] == "EXP:":
		VarValue = doEvaluate(VarValue[4:])
	elif VarValue[0:4] == "NUM:":
		VarValue = VarValue[4:]
	elif VarValue[0:4] == "VAR:":
		VarValue = getVARIABLE(VarValue)
	symbols[VarName[4:]] = VarValue
	
def doLoop(toks):
	i = 0
	index = 0
	stack = []
	while(i<len(toks)):
		if toks[i][0:4] == "ELP:":
			toks[i] = "ELP:"+stack.pop()
		elif toks[i][0:4] == "LOP:":
			toks[i] = "LOP:" + str(index)
			stack.append(str(index))
			index+=1
		i+=1
	return toks

def getInput(string, varName):
	string = string[1:-1]
	i = input(string)
	inp = ""
	i = list(i)
	IsNum = 0
	IsExp = 0
	for char in i:
		inp += char
		if inp=="0" or inp=="1" or inp=="2" or inp=="3" or inp=="4" or inp=="5" or inp=="6" or inp=="7" or inp=="8" or inp=="9":
			IsNum = 1
		if IsNum == 1:
			if char=="+" or char=="-" or char=="*" or char=="/" or char=="%" or char=="(" or char==")":
				IsExp = 1
	if IsNum ==1 and IsExp == 1:
		inp = doEvaluate(inp)
	symbols[varName] = inp
	
def getVARIABLE(VarName):
	VarName = VarName[4:]
	if VarName in symbols:
		return symbols[VarName]
	else:
		return "Undefined Variable :("
		exit()
	
def parse(toks):
	i = 0
	toks = doLoop(toks)
	while (i < len(toks)):
		if toks[i] == "CON:LST":
			i+=1
		elif toks[i][0:4] == "ELP:":
			tex = toks[i][4:]
			y = i
			x = loop.pop()
			x = int(x)
			x+=1
			while toks[i] != "LOP:"+tex:
				i-=1
			if x >= int(toks[i+3][4:]):
				i = y+1
			else:
				loop.append(x)
				i += 4
		elif toks[i] == "EIF:":
			i+=1
		elif toks[i] + " " + toks[i+1][0:4] == "DIS: STR:" or toks[i] + " " + toks[i+1][0:4] == "DIS: EXP:" or toks[i] + " " + toks[i+1][0:4] == "DIS: NUM:" or toks[i] + " " + toks[i+1][0:4] == "DIS: VAR:":
			if toks[i+1][0:4] == "STR:":
				doPRINT(toks[i+1])
			elif toks[i+1][0:4] == "EXP:":
				doPRINT(toks[i+1])
			elif toks[i+1][0:4] == "NUM:":
				doPRINT(toks[i+1])
			elif toks[i+1][0:4] == "VAR:":
				doPRINT(getVARIABLE(toks[i+1]))
			i+=2
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] == "VAR: EQL: STR:" or toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] == "VAR: EQL: NUM:" or toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] == "VAR: EQL: EXP:" or toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] == "VAR: EQL: VAR:":
			if toks[i+2][0:4] == "STR:":
				doAssign(toks[i], toks[i+2])
			elif toks[i+2][0:4] == "EXP:":
				doAssign(toks[i], toks[i+2])
			elif toks[i+2][0:4] == "NUM:":
				doAssign(toks[i], toks[i+2])
			elif toks[i+2][0:4] == "VAR:":
				doAssign(toks[i], toks[i+2])
			i+=3
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] == "GET: STR: VAR:":
			getInput(toks[i+1][4:],toks[i+2][4:])
			i+=3
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: NUM: CON: NUM: THN:":
			if (toks[i+1][4:] == toks[i+3][4:] and toks[i+2][4:] == "DQL"):
				i+=5
			elif (toks[i+1][4:] > toks[i+3][4:] and toks[i+2][4:] == "GRT"):
				i+=5
			elif (toks[i+1][4:] < toks[i+3][4:] and toks[i+2][4:] == "LST"):
				i+=5
			elif (toks[i+1][4:] >= toks[i+3][4:] and toks[i+2][4:] == "GRE"):
				i+=5
			elif (toks[i+1][4:] <= toks[i+3][4:] and toks[i+2][4:] == "LSE"):
				i+=5
			elif (toks[i+1][4:] != toks[i+3][4:] and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
			
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: NUM: CON: EXP: THN:":
			if (toks[i+1][4:] == doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (toks[i+1][4:] > doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (toks[i+1][4:] < doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (toks[i+1][4:] >= doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (toks[i+1][4:] <= doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (toks[i+1][4:] != doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: EXP: CON: NUM: THN:":
			if (doEvaluate(toks[i+1][4:]) == (toks[i+3][4:]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) > (toks[i+3][4:]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) < (toks[i+3][4:]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) >= (toks[i+3][4:]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) <= (toks[i+3][4:]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) != (toks[i+3][4:]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: EXP: CON: EXP: THN:":
			if (doEvaluate(toks[i+1][4:]) == doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) > doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) < doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) >= doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) <= doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) != doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: VAR: CON: EXP: THN:":
			if (getVARIABLE(toks[i+1]) == doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (getVARIABLE(toks[i+1]) > doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (getVARIABLE(toks[i+1]) < doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (getVARIABLE(toks[i+1]) >= doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) <= doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) != doEvaluate(toks[i+3][4:]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: VAR: CON: VAR: THN:":
			if (getVARIABLE(toks[i+1]) == getVARIABLE(toks[i+3]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (getVARIABLE(toks[i+1]) > getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (getVARIABLE(toks[i+1]) < getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (getVARIABLE(toks[i+1]) >= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) <= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) != getVARIABLE(toks[i+3]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: EXP: CON: VAR: THN:":
			if (doEvaluate(toks[i+1][4:]) == getVARIABLE(toks[i+3]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) > getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) < getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) >= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) <= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (doEvaluate(toks[i+1][4:]) != getVARIABLE(toks[i+3]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: NUM: CON: VAR: THN:":
			if ((toks[i+1][4:]) == getVARIABLE(toks[i+3]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif ((toks[i+1][4:]) > getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif ((toks[i+1][4:]) < getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LST"):
				i+=5
			elif ((toks[i+1][4:]) >= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif ((toks[i+1][4:]) <= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif ((toks[i+1][4:]) != getVARIABLE(toks[i+3]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: VAR: CON: NUM: THN:":					
			if (getVARIABLE(toks[i+1]) == (toks[i+3][4:]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (getVARIABLE(toks[i+1]) > (toks[i+3][4:]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (getVARIABLE(toks[i+1]) < (toks[i+3][4:]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (getVARIABLE(toks[i+1]) >= (toks[i+3][4:]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) <= (toks[i+3][4:]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) != (toks[i+3][4:]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
		
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: VAR: CON: STR: THN:":					
			if (getVARIABLE(toks[i+1]) == (toks[i+3][5:-1]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif (getVARIABLE(toks[i+1]) > (toks[i+3][5:-1]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif (getVARIABLE(toks[i+1]) < (toks[i+3][5:-1]) and toks[i+2][4:] == "LST"):
				i+=5
			elif (getVARIABLE(toks[i+1]) >= (toks[i+3][5:-1]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) <= (toks[i+3][5:-1]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif (getVARIABLE(toks[i+1]) != (toks[i+3][5:-1]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: STR: CON: STR: THN:":					
			if ((toks[i+1][5:-1]) == (toks[i+3][5:-1]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif ((toks[i+1][5:-1]) > (toks[i+3][5:-1]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif ((toks[i+1][5:-1]) < (toks[i+3][5:-1]) and toks[i+2][4:] == "LST"):
				i+=5
			elif ((toks[i+1][5:-1]) >= (toks[i+3][5:-1]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif ((toks[i+1][5:-1]) <= (toks[i+3][5:-1]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif ((toks[i+1][5:-1]) != (toks[i+3][5:-1]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
					
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] + " " + toks[i+4][0:4] == "IIF: STR: CON: VAR: THN:":					
			if ((toks[i+1][5:-1]) == getVARIABLE(toks[i+3]) and toks[i+2][4:] == "DQL"):
				i+=5
			elif ((toks[i+1][5:-1]) > getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRT"):
				i+=5
			elif ((toks[i+1][5:-1]) < getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LST"):
				i+=5
			elif ((toks[i+1][5:-1]) >= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "GRE"):
				i+=5
			elif ((toks[i+1][5:-1]) <= getVARIABLE(toks[i+3]) and toks[i+2][4:] == "LSE"):
				i+=5
			elif ((toks[i+1][5:-1]) != getVARIABLE(toks[i+3]) and toks[i+2][4:] == "NTE"):
				i+=5
			else:
				i+=5
				while toks[i] != "EIF:":
					i+=1
		
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] == "LOP: NUM: TIL: NUM:":
			loop.append(toks[i+1][4:])
			i+=4
		elif toks[i][0:4] + " " + toks[i+1][0:4] + " " + toks[i+2][0:4] + " " + toks[i+3][0:4] == "LOP: VAR: TIL: NUM:":
			loop.append(getVARIABLE(toks[i+1]))
			i+=4

def run():
	data = open_file(argv[1])
	toks = lex(data)
	parse(toks)

run()