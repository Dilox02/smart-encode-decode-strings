from math import prod


# Implementazione di un metodo di codifica/decodifica di stringhe basato su numeri primi
# Sfrutta il Teorema Cinese del Resto per mantenere l'informazione della posizione
# dei singoli caratteri in una sequenza, evitando così di usare un sistema posizionale 
# base 256 con valori che esplodono molto rapidamente
#
# Principio di funzionamento:
# 1. Usa numeri primi come pesi per garantire l'unicità della codifica
# 2. Ogni valore viene "pesato" in base alla sua posizione originale

# Vantaggi:
# - Preserva perfettamente l'ordine dei valori originali
# - Permette di rappresentare una sequenza come un singolo numero intero
# - Utilizza proprietà matematiche dei numeri primi per garantire l'invertibilità

def encode(values, weights):
    """Codifica una lista di valori usando pesi distinti."""
    return sum(v * prod(weights[:i]) for i, v in enumerate(values))

def decode(S, weights):
    """Decodifica il valore S in base ai pesi."""
    values = []
    for i, w in enumerate(weights):
        modulo = prod(weights[:i])
        values.append((S // modulo) % w)
    return values


def string_to_ascii_array(s):
    """Converte una stringa in un array dei suoi valori ASCII."""
    return [ord(char) for char in s]

def ascii_array_to_string(ascii_array):
    """Ricostruisce una stringa a partire da un array di valori ASCII."""
    return ''.join(chr(code) for code in ascii_array)

# Esempio 1
values = string_to_ascii_array("ciaomondo")


primi=[257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433]

weights=primi[:len(values)]
encoded = encode(values, weights)
decoded = decode(encoded, weights)



print(f"Valori originali: {values}")
print(f"Numero codificato: {encoded}")
print(f"Valori decodificati: {decoded}")

# Esempio 2

# for i in range(10,100):
#     decoded = decode(i, weights)
#     print(decoded)
#     print(ascii_array_to_string(decoded))