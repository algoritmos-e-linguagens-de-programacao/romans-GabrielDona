# Números que terão sua conexão com os símbolos
num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

# Símbolos que serão convertidos no lugar dos números
sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

def int_to_roman(number):
    i = 0
    roman_numeral = ""
    while number > 0:
        # Operação de divisão do número inputado com número na ordem da lista
        div = number // num[i]
        # Pega a sobra da divisão e transforma no próximo número a ser dividido
        number %= num[i]
        # Enquanto que faz com que o símbolo do número dividido seja adicionado ao resultado
        while div > 0:
            roman_numeral += sym[i]
            div -= 1
        # Passa para o próximo número
        i += 1
    return roman_numeral
sym_to_value = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
    "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
}

def roman_to_int(s):
    i = 0
    total = 0
    n = len(s)
    while i < n:
        # Verifica se o par de símbolos forma um numeral especial (por exemplo, "IV", "IX", etc.)
        if i + 1 < n and s[i:i+2] in sym_to_value:
            total += sym_to_value[s[i:i+2]]
            i += 2
        else:
            total += sym_to_value[s[i]]
            i += 1
    return total

if __name__ == "__main__":
    number = 1994
    s = "MCMXCIV"

    print("O número romano para o numeral inserido é:", int_to_roman(number))
    print("O número inteiro para o numeral romano inserido é:", roman_to_int(s))
