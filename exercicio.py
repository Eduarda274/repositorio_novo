def calcular_imc(peso, altura):
    """Calcula o IMC e retorna a categoria correspondente."""
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = 'Abaixo do peso'
    elif 18.5 <= imc < 24.9:
        categoria = 'Peso normal'
    elif 25 <= imc < 29.9:
        categoria = 'Sobrepeso'
    else:
        categoria = 'Obesidade'
    
    return imc, categoria

def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return
        
        imc, categoria = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Categoria: {categoria}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
