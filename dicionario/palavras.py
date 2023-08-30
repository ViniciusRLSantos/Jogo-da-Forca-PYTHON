# Pacotes/Bibliotecas
import random

# Lista de palavras categorizadas para um jogo de forca
palavra = {
    "Animais": [
        "Gato",
        "Cachorro",
        "Elefante",
        "Leão",
        "Girafa",
        "Borboleta",
        "Tubarão",
        "Pinguim",
        "Coala",
        "Macaco"
    ],
    "Frutas": [
        "Maçã",
        "Banana",
        "Laranja",
        "Morango",
        "Uva",
        "Abacaxi",
        "Pêra",
        "Kiwi",
        "Manga"
    ],
    "Países": [
        "Brasil",
        "Estados Unidos",
        "França",
        "Japão",
        "Rússia",
        "Canadá",
        "China",
        "Índia",
        "Itália",
        "México"
    ],
    "Profissões": [
        "Médico",
        "Professor",
        "Engenheiro",
        "Advogado",
        "Chef",
        "Artista",
        "Bombeiro",
        "Policial",
        "Jornalista",
        "Dentista"
    ],
    "Alimentos": [
        "Pizza",
        "Hambúrguer",
        "Massa",
        "Sushi",
        "Salada",
        "Chocolate",
        "Sorvete",
        "Batata",
        "Frango",
        "Arroz"
    ],
    "Termos Científicos": [
        "Eletromagnetismo",
        "Mitocôndria",
        "Fotossíntese",
        "Ácido Desoxirribonucleico",
        "Entropia",
        "Equilíbrio Químico",
        "Circunferência",
        "Hipotenusa",
        "Isótopo",
        "Nebulosa"
    ],
    "Vocabulário Arcaico": [
        "Arcaísmo",
        "Pellizcar",
        "Obsoleto",
        "Soerguer",
        "Rústico",
        "Exíguo",
        "Desusado",
        "Míngua",
        "Ufano",
        "Peregrino"
    ],
    "Palavras Estrangeiras": [
        "Schadenfreude",
        "Saudade",
        "Déjà vu",
        "Komorebi",
        "Fernweh",
        "Tsundoku",
        "Mamihlapinatapai",
        "Hygge",
        "Kummerspeck",
        "Waldeinsamkeit"
    ],
    "Personagens Históricos": [
        "Galileu Galilei",
        "Hipátia de Alexandria",
        "Wu Zetian",
        "Diógenes",
        "Hypatius de Roma",
        "Sócrates",
        "Álvaro de Campos",
        "Murasaki Shikibu",
        "Maimônides",
        "Marcus Aurelius"
    ]
}

# Função que irei utilizar para retornar uma categoria e uma palavra daquela categoria em forma de tupla
def escolher_palavra():
    global palavra
    
    categoria = random.choice(list(palavra.keys()))
    palavra_escolhida = random.choice(palavra[categoria])
    
    return categoria, palavra_escolhida

