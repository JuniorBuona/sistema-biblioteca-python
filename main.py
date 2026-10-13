import json
import os

ARQUIVO = "livros.json"

def carregar_livros():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_livros(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)

def adicionar_livro(livros):
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    livros.append({"titulo": titulo, "autor": autor, "ano": ano})
    salvar_livros(livros)
    print("Livro adicionado!")

def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

def remover_livro(livros):
    listar_livros(livros)
    idx = int(input("Número para remover: ")) - 1
    livros.pop(idx)
    salvar_livros(livros)
    print("Removido!")

def main():
    livros = carregar_livros()
    while True:
        print("\n=== Sistema Biblioteca ===")
        print("1. Adicionar")
        print("2. Listar")
        print("3. Remover")
        print("4. Sair")
        op = input("Opção: ")
        if op == "1": adicionar_livro(livros)
        elif op == "2": listar_livros(livros)
        elif op == "3": remover_livro(livros)
        elif op == "4": break

if __name__ == "__main__":
    main()
