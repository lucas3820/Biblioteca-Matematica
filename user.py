import matematica as m

numero = int(input("Informe um número: "))
resposta = m.fatorial(numero)
print(resposta)
if m.primo(numero):
    print("É primo")
else:
    print("Não é primo")
print("par" if m.par(numero) else "impar")