# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def main():
	try:
		a = float(input('Digite o primeiro número: '))
		b = float(input('Digite o segundo número: '))
	except ValueError:
		print('Entrada inválida')
		return

	s = a + b
	d = a - b
	p = a * b
	print(f'{a} + {b} = {s}')
	print(f'{a} - {b} = {d}')
	print(f'{a} * {b} = {p}')
	if b != 0:
		print(f'{a} / {b} = {a / b}')
	else:
		print('Divisão por zero não permitida')


if __name__ == '__main__':
	main()