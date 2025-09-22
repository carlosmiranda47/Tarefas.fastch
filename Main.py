pessoas = [["wellyton", 70, 1.75, 35],["joão", 90, 1.60, 40], ["maria", 90,  1.60, 40]]

def classificar_imc(imc):
	if imc < 18.5:
		return "baixo peso(grau 1)"
	elif 18.5 <= imc < 25:
		return "peso adequado"
	elif 25 <= imc < 30:
	    return "sobre peso"
	elif 30 <= imc < 35:
	    return "obesidade (grau 1)"
	elif 35 <= imc < 40:
	    return "obesidade (grau 2)"
	else:
	    return "obesidade (grau 3)"
	    

for pessoas in pessoas:
	nome, peso, altura, idade = pessoas
	imc = peso / (altura ** 2)
	descricao = classificar_imc(imc)
	print(f"{nome} - {idade} anos - {descricao}")
