import requests

catalogo = []

def buscar_filme_api(query):
    url = f"https://rest.imdbapi.dev/v2/search/titles?query={query}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados.get("results", [])
    else:
        print("❌ Erro ao buscar na API.")
        return []

def adicionar_filme():
    query = input("🎬 Digite o nome do filme que deseja buscar: ")
    resultados = buscar_filme_api(query)

    if not resultados:
        print("❌ Nenhum resultado encontrado.")
        return

    print("\n📽️ Resultados encontrados:")
    for i, filme in enumerate(resultados[:5], start=1):
        print(f"{i}. {filme.get('title')} ({filme.get('year')})")

    escolha = input("\nEscolha o número do filme que deseja adicionar (ou pressione Enter para cancelar): ")
    if not escolha.isdigit():
        print("🚫 Ação cancelada.")
        return

    index = int(escolha) - 1
    if 0 <= index < len(resultados[:5]):
        filme_escolhido = resultados[index]
        catalogo.append(filme_escolhido)
        print(f"✨ Filme '{filme_escolhido.get('title')}' adicionado ao seu catálogo!")
    else:
        print("🚫 Número inválido.")

def listar_filmes():
    if not catalogo:
        print("📂 Nenhum filme adicionado ainda.")
        return

    print("\n🎞️ Seu Catálogo de Filmes:")
    for i, filme in enumerate(catalogo, start=1):
        print(f"{i}. {filme.get('title')} ({filme.get('year')}) - IMDb ID: {filme.get('id')}")

def menu():
    while True:
        print("\n🎬 Menu do Catálogo")
        print("1. Adicionar filme pelo título")
        print("2. Listar filmes salvos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_filme()
        elif escolha == "2":
            listar_filmes()
        elif escolha == "3":
            print("🌙 Saindo... Até a próxima sessão!")
            break
        else:
            print("❗ Opção inválida.")

if __name__ == "__main__":
    menu()
