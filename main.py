# Imports
import random
from unidecode import unidecode
from dicionario import palavras


# Iniciar variáveis
categoria = "Sei lá" # Categoria da palavra que foi escolhida
palavra_escolhida = "Também não sei" # A palavra_escolhida é a palavra escondida (uau)
palavra_secreta = "Aí que não sei mesmo" # A palavra que será revelada aos poucos

valendo = 0 # Quanto dinheiro vale a adivinhacao
dinheiro = 0 # VALENDO DINHEIRO DE VERDADE (REAL)
erros = 0 # Será o índice do nosso homem da forca
homem_da_forca = [ # Vai desenhar o boneco da forca utilizando a variável 'erros' como índice
    "\n\n\n",
    " O \n\n", 
    " O \n | \n",
    " O \n-| \n",
    " O \n-|- \n",
    " O \n-|- \n/",
    " O \n-|- \n/ \\"
]
letras_ditas = [] # Irá armazenar todas as letras que já foram ditas


# Procura letras e espaços de uma string e substitui por * e - respectivamente e retorna a nova string
def esconder_palavra(palavra: str):
    for i in range(len(palavra)):
        if palavra[i].isspace():
            palavra = palavra.replace(palavra[i], "-")
        elif palavra[i] != "*":
            palavra = palavra.replace(palavra[i], "*")
    return palavra

# Escolhe uma categoria aleatória e uma palavra aleatória da categoria escolhida
def iniciar_forca():
    global categoria
    global palavra_escolhida
    global palavra_secreta
    global erros
    
    # Escolher uma categoria e uma palavra
    (categoria, palavra_escolhida) = palavras.escolher_palavra()
    palavra_secreta = esconder_palavra(palavra_escolhida)
    
    jogo() # Inicia a 

# Verifica se a letra digitada está na palavra e se já foi utilizada
def verificar_adivinhacao(letra: str):
    global palavra_escolhida
    global palavra_secreta
    global erros
    global letras_ditas
    global valendo
    global dinheiro
    
    palavra = unidecode(palavra_escolhida).upper() # É a mesma palavra escolhida, mas sem acentos e deixando tudo maiúsculo
    letra = unidecode(letra) # Tiramos o acento da letra inserida, caso tenha
    letra = letra[0].upper() # Pegamos somente a primeira letra da string para caso o usuário tenha inserido mais de uma letra.
    
    # Caso a letra não esteja na palavra e nem nas letras ditas
    if letra not in palavra and letra not in letras_ditas:
        erros += 1 # aumentamos a variável de erros em 1
        letras_ditas.append(letra) # inserimos a letra na lista de letras ditas
    elif letra in letras_ditas: # Caso esteja na lista de letras ditas
        print("\n")
        print("-"*50)
        print("ESTA LETRA JÁ FOI USADA")
        print("-"*50)
    else: # caso a letra exista na palavra e não está nas letras ditas
        letras_ditas.append(letra) # inserimos a letra na lista de letras ditas
        dinheiro += valendo * palavra.count(letra) # Paga o valor de cada letra acertada
        # Inicia uma repetição que insere a letra no local correto da palavra secreta
        for i in range(0, len(palavra)):
            if letra == palavra[i]:
                # Substituimos os '*' com a letra correta no local correto
                palavra_secreta = palavra_secreta[:i]+palavra_escolhida[i]+palavra_secreta[i+1:]
    jogo() # Voltamos para a forca
    

# Jogo principal
def jogo():
    global valendo
    global dinheiro
    global palavra_escolhida
    
    # Basicamente a roleta do 
    valendo = int(random.randrange(1, 10)) * 100
    
    # Faz com que o jogador perca
    if erros >= len(homem_da_forca)-1:
        print("="*50)
        print("===================VOCÊ PERDEU===================")
        print("="*50)
        print(homem_da_forca[erros])
        print("Ele morreu... e você ainda saiu pobre. Vish...")
        print(f"A palavra correta era: {palavra_escolhida}")
        return
    
    # Faz com que o jogador vença
    if palavra_secreta.count("*") <= 0:
        print("="*50)
        print("===================VOCÊ VENCEU===================")
        print("="*50)
        print(f"E ainda levou R${dinheiro},00 para casa!")
        return
    
    print("="*50)
    print("=v=====")
    print(homem_da_forca[erros])
    print(f"{palavra_secreta}")
    print(f"Categoria: {categoria.upper()}")
    print("\nLetras ditas:\n" + "-".join(letras_ditas))
    print(f"VALENDO R${valendo},00  CADA LETRA CORRETA!")
    print(f"\nVocê tem: R${dinheiro},00")
    suposicao = input("Fale uma letra: ")
    print("="*50)
    verificar_adivinhacao(suposicao)   

# Executar somente esse script
if __name__ == "__main__":
    iniciar_forca()