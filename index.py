import random
import sys

from nltk.chat.util import Chat, reflections

listaJogos = {
    "The Legend of Zelda: Breath of the Wild": ["Ação-aventura", "Mundo aberto", "Fantasia"],
    "Red Dead Redemption 2": ["Ação-aventura", "Mundo aberto", "Velho Oeste"],
    "The Witcher 3: Wild Hunt": ["RPG", "Mundo aberto", "Fantasia"],
    "God of War": ["Ação-aventura", "Mundo aberto", "Mitologia"],
    "Minecraft": ["Sandbox", "Construção", "Aventura"],
    "Grand Theft Auto V": ["Ação-aventura", "Mundo aberto", "Crime"],
    "Dark Souls III": ["RPG", "Ação", "Fantasia"],
    "Horizon Zero Dawn": ["Ação-aventura", "Mundo aberto", "Ficção científica"],
    "Cyberpunk 2077": ["RPG", "Mundo aberto", "Ficção científica"],
    "Assassin's Creed Valhalla": ["Ação-aventura", "Mundo aberto", "Histórico"],
    "Among Us": ["Multijogador", "Social", "Mistério"],
    "Valorant": ["FPS", "Multijogador", "Competitivo"],
    "League of Legends": ["MOBA", "Multijogador", "Competitivo"],
    "Fortnite": ["Battle Royale", "Multijogador", "Construção"],
    "Call of Duty: Warzone": ["Battle Royale", "FPS", "Multijogador"],
    "Apex Legends": ["Battle Royale", "FPS", "Multijogador"],
    "Overwatch": ["FPS", "Multijogador", "Competitivo"],
    "Super Mario Odyssey": ["Plataforma", "Aventura", "Fantasia"],
    "Animal Crossing: New Horizons": ["Simulação", "Mundo aberto", "Social"],
}

def recomendar_jogo_por_genero(genero):
    print(f"Recomendando jogo do gênero: {genero}")
    jogos_recomendados = []
    for jogo, generos in listaJogos.items():
        if genero.lower() in [g.lower() for g in generos]:
            jogos_recomendados.append(jogo)
    if jogos_recomendados:
        return random.choice(jogos_recomendados)
    else:
        return False

def recomendar_jogo():
    randInt = random.randint(0, len(listaJogos) - 1)
    jogo = list(listaJogos.keys())[randInt]
    return jogo

pares = [
    (r"oi|olá|bom dia|boa tarde|boa noite|opa", [
        "Olá! Como posso ajudar?",
        "Oi tudo bem?",
    ]),
    (r"qual é o seu nome?", [
        "Meu nome é GameBot."
    ]),
    (r"qual é a sua função? | o que você faz?", [
        "Eu sou um chatbot que ajuda a escolher jogos da sua preferência.",
        "Posso recomendar jogos com base nos seus gostos e interesses."
    ]),
    (r"meu nome é (.*). baseado em meu nome, me indique um jogo", [
        recomendar_jogo()+". Você gostaria de uma recomendação personalizada com base em seus gostos?",
    ]),
    (r"sim, me recomende um jogo de (.*)", [
        "__GENERO__%1",
    ]),
    (r"me recomende um jogo de (.*)", [
        "__GENERO__%1",
    ]),
    (r"tchau|adeus|até mais", [
        "Tchau! Foi bom conversar com você.", 
        "Adeus! Tenha um ótimo dia!"
    ]),
    (r"(.*)", [
        "Desculpe, não entendi.", 
        "Tendi nada kkk"
    ]),
]

reflections = {
    "eu": "você",
    "meu": "seu",
    "meus": "seus",
    "minha": "sua",
    "minhas": "suas",
    "me": "você",
    "você": "eu",
    "seu": "meu",
    "sua": "minha",
    "fui": "foi",
    "estou": "está",
}

chatbot = Chat(pares, reflections)

def iniciar_chat():
    print("Início da conversa")
    while True:
        entrada = input("Você: ")

        if entrada.lower() in ["tchau", "adeus", "até mais"]:
            print("ChatBot: Tchau! Foi bom conversar com você.")
            break
        resposta = chatbot.respond(entrada)

        if resposta and resposta.startswith("__GENERO__"):
            genero = resposta.replace("__GENERO__", "", 1).strip()
            jogo = recomendar_jogo_por_genero(genero)
            if jogo:
                resposta = f"Eu recomendo o jogo '{jogo}'."
            else:
                resposta = "Não tenho nenhum jogo com esse gênero"

        print("ChatBot:", resposta)

iniciar_chat()