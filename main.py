import json
import os

ARQUIVO = "livros.json"

def carregar_livros():
    """Carrega livros do JSON com tratamento de erro"""
    try:
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
    except json.JSONDecodeError:
        print("Erro: Arquivo JSON corrompido. Criando novo.")
    except Exception as e:
        print(f"Erro ao carregar: {e}")
    return []

def salvar_livros(livros):
    """Salva com tratamento de erro"""
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(livros, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def adicionar_livro(livros):
    try:
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        ano = input("Ano: ").strip()
        if not titulo or not autor:
            print("Erro: Título e autor são obrigatórios!")
            return
        livros.append({"titulo": titulo, "autor": autor, "ano": ano})
        salvar_livros(livros)
        print("✅ Livro adicionado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

def listar_livros(livros):
    if not livros:
        print("📚 Nenhum livro cadastrado.")
        return
    print(f"\n--- {len(livros)} livro(s) cadastrado(s) ---")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

def buscar_por_titulo(livros):
    """Funcionalidade extra"""
    try:
        termo = input("Buscar por título: ").lower().strip()
        encontrados = [l for l in livros if termo in l['titulo'].lower()]
        if encontrados:
            print(f"\n🔍 {len(encontrados)} encontrado(s):")
            for l in encontrados:
                print(f"- {l['titulo']} - {l['autor']}")
        else:
            print("Nenhum livro encontrado.")
    except Exception as e:
        print(f"Erro na busca: {e}")

def remover_livro(livros):
    listar_livros(livros)
    if not livros:
        return
    try:
        idx = int(input("Número do livro para remover: ")) - 1
        if 0 <= idx < len(livros):
            removido = livros.pop(idx)
            salvar_livros(livros)
            print(f"🗑️ Removido: {removido['titulo']}")
        else:
            print("Número inválido!")
    except ValueError:
        print("Erro: Digite um número válido!")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    livros = carregar_livros()
    while True:
        print("\n=== Sistema Biblioteca - Python - Marcelo Buonadio ===")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Buscar por título")
        print("4. Remover livro")
        print("5. Sair")
        try:
            op = input("Opção: ").strip()
            if op == "1": adicionar_livro(livros)
            elif op == "2": listar_livros(livros)
            elif op == "3": buscar_por_titulo(livros)
            elif op == "4": remover_livro(livros)
            elif op == "5":
                print("Saindo... 👋")
                break
            else: print("Opção inválida!")
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
