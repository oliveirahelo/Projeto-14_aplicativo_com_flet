import os
import flet as ft

def main(page: ft.Page):
    page.title = "💻 Sistema Multifunções Avançado"
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.scroll = "auto"

    # --- CAMPOS ---
    entrada = ft.TextField(label="Nome do arquivo/pasta", width=400)
    novo_nome = ft.TextField(label="Novo nome (para renomear ou mover)", width=400)
    novo_caminho = ft.TextField(label="Novo diretório (para mudar de pasta)", width=400)
    mensagem = ft.Text("", size=18, color="white")

    # --- FUNÇÕES ---
    def atualizar_mensagem(texto, cor="white"):
        mensagem.value = texto
        mensagem.color = cor
        page.update()

    def criar_pasta(e):
        nome = entrada.value.strip()
        if not nome:
            return atualizar_mensagem("Digite o nome da pasta.", "orange")
        try:
            os.mkdir(nome)
            atualizar_mensagem(f"📁 Pasta criada: {nome}", "lightgreen")
        except FileExistsError:
            atualizar_mensagem("Essa pasta já existe.", "yellow")
        except Exception as erro:
            atualizar_mensagem(f"Erro: {erro}", "red")

    def criar_arquivo(e):
        nome = entrada.value.strip()
        if not nome:
            return atualizar_mensagem("Digite o nome do arquivo.", "orange")
        try:
            open(nome, "w").close()
            atualizar_mensagem(f"📄 Arquivo criado: {nome}", "lightgreen")
        except Exception as erro:
            atualizar_mensagem(f"Erro: {erro}", "red")

    def listar(e):
        try:
            itens = os.listdir()
            if not itens:
                atualizar_mensagem("📂 Nenhum arquivo ou pasta encontrado.", "orange")
            else:
                atualizar_mensagem("📋 Itens no diretório atual:\n" + "\n".join(itens), "cyan")
        except Exception as erro:
            atualizar_mensagem(f"Erro: {erro}", "red")

    def mostrar_diretorio(e):
        dir_atual = os.getcwd()
        atualizar_mensagem(f"📁 Diretório atual:\n{dir_atual}", "cyan")

    def mudar_diretorio(e):
        caminho = novo_caminho.value.strip()
        if not caminho:
            return atualizar_mensagem("Digite o novo caminho.", "orange")
        try:
            os.chdir(caminho)
            atualizar_mensagem(f"📂 Mudou para: {os.getcwd()}", "lightgreen")
        except FileNotFoundError:
            atualizar_mensagem("Caminho não encontrado.", "yellow")
        except Exception as erro:
            atualizar_mensagem(f"Erro: {erro}", "red")

    def renomear(e):
        antigo = entrada.value.strip()
        novo = novo_nome.value.strip()
        if not antigo or not novo:
            return atualizar_mensagem("Preencha os dois campos.", "orange")
        try:
            os.rename(antigo, novo)
            atualizar_mensagem(f"✏️ '{antigo}' renomeado para '{novo}'", "lightgreen")
        except FileNotFoundError:
            atualizar_mensagem("Item não encontrado.", "yellow")
        except Exception as erro:
            atualizar_mensagem(f"Erro: {erro}", "red")

    def excluir(e):
        nome = entrada.value.strip()
        if not nome:
            return atualizar_mensagem("Digite o nome do item a excluir.", "orange")
        try:
            if os.path.isdir(nome):
                os.rmdir(nome)
                atualizar_mensagem(f"🗑️ Pasta excluída: {nome}", "lightgreen")
            else:
                os.remove(nome)
                atualizar_mensagem(f"🗑️ Arquivo excluído: {nome}", "lightgreen")
        except FileNotFoundError:
            atualizar_mensagem("Item não encontrado.", "yellow")
        except OSError:
            atualizar_mensagem("A pasta não está vazia.", "orange")
        except Exception as erro:
            atualizar_mensagem(f"Erro: {erro}", "red")

    def detalhes(e):
        nome = entrada.value.strip()
        if not nome:
            return atualizar_mensagem("Digite o nome do arquivo/pasta.", "orange")
        if not os.path.exists(nome):
            return atualizar_mensagem("Item não encontrado.", "yellow")
        try:
            tipo = "Pasta" if os.path.isdir(nome) else "Arquivo"
            tamanho = os.path.getsize(nome)
            caminho = os.path.abspath(nome)
            atualizar_mensagem(
                f"🔎 Detalhes:\nTipo: {tipo}\nTamanho: {tamanho} bytes\nCaminho: {caminho}",
                "lightblue",
            )
        except Exception as erro:
            atualizar_mensagem(f"Erro: {erro}", "red")

    def limpar(e):
        entrada.value = ""
        novo_nome.value = ""
        novo_caminho.value = ""
        atualizar_mensagem("Campos limpos.", "gray")
        page.update()

    def sair(e):
        atualizar_mensagem("👋 Encerrando o programa...", "orange")
        page.update()
        page.window.close()

    # --- BOTÕES ---
    botoes_linha1 = ft.Row([
        ft.ElevatedButton("📁 Criar Pasta", on_click=criar_pasta, bgcolor="purple", color="white"),
        ft.ElevatedButton("📄 Criar Arquivo", on_click=criar_arquivo, bgcolor="cyan", color="black"),
        ft.ElevatedButton("📋 Listar Itens", on_click=listar, bgcolor="teal", color="white"),
    ], alignment="center")

    botoes_linha2 = ft.Row([
        ft.ElevatedButton("📂 Mostrar Diretório", on_click=mostrar_diretorio, bgcolor="indigo", color="white"),
        ft.ElevatedButton("📍 Mudar Diretório", on_click=mudar_diretorio, bgcolor="blue", color="white"),
    ], alignment="center")

    botoes_linha3 = ft.Row([
        ft.ElevatedButton("✏️ Renomear", on_click=renomear, bgcolor="orange", color="black"),
        ft.ElevatedButton("🗑️ Excluir", on_click=excluir, bgcolor="red", color="white"),
        ft.ElevatedButton("🔎 Detalhes", on_click=detalhes, bgcolor="green", color="white"),
    ], alignment="center")

    botoes_linha4 = ft.Row([
        ft.ElevatedButton("🧹 Limpar", on_click=limpar, bgcolor="gray", color="white"),
        ft.ElevatedButton("🚪 Sair", on_click=sair, bgcolor="black", color="white"),
    ], alignment="center")

    # --- LAYOUT ---
    page.add(
        ft.Text("SISTEMA MULTIFUNÇÕES AVANÇADO", size=30, weight="bold", color="white"),
        entrada,
        novo_nome,
        novo_caminho,
        botoes_linha1,
        botoes_linha2,
        botoes_linha3,
        botoes_linha4,
        mensagem
    )

ft.app(target=main)