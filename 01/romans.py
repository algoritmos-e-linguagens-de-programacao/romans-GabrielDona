#definição que cria a lista de números com atribuição de simbolos a cada um deles
def printRoman(number):

    #Números que terão sua conexão com o simbolos
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]

    #Simbolos que serão convertidos no lugar dos números
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]

    #i = ordem em que se encontra os números, sendo o úmero com local 12 o mais alto e local 0 o mais baixo
    i = 12

    #cria um enquanto que faz a repetição da ação sempre que etiver nesse processo
    while number:

        #Operação de divisão do número inputado com número na ordem da lista, sendo a sequencia do mais alto para o mais baixo   
        div = number // num[i]
        #Pega a sobra da divisão e trasnforma no proximo numero a ser dividido, e faz com que volte a acontecer a corda, até acabar os número a serem divididos
        number %= num[i]
  
        #Enquanto que faz com que o simbolo do número dividido seja printado e assim passe para o proximo número a ser dividio e printado
        while div:
            #Printa o simbolo
            print(sym[i], end = "")
            #Pega o numero divido e diminui 1 dele
            div -= 1
        #Diminui em 1 na ordem de sequencia de divisão dos números
        #Resumindo, passa para o proximo número
        i -= 1
  
if __name__ == "__main__":
    number = 3954
    print("O número romano para o numeral inserido é:", end = " ")
    printRoman(number)
    
