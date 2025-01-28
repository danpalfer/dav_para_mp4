import tkinter as tk
from tkinter import filedialog, messagebox
import vlc
import time
import threading
import os

def converter_dav_para_mp4(arquivo_entrada, arquivo_saida):
    player = vlc.Instance()
    media = player.media_new(arquivo_entrada)
    media.add_option(f"sout=#file{{dst={arquivo_saida}}}")
    media.add_option("no-sout-all")
    media.add_option("sout-keep")
    media_player = player.media_player_new()
    media_player.set_media(media)

    print(f"Convertendo {arquivo_entrada} para {arquivo_saida}...")
    media_player.play()
    time.sleep(5)  # Dê um tempo para o VLC iniciar

    while media_player.is_playing():
        time.sleep(1)

    print("Conversão concluída.")
    media_player.stop()


def selecionar_arquivo_entrada():
    arquivo_entrada = filedialog.askopenfilename(
        title="Selecione o arquivo .DAV",
        filetypes=[("Arquivos DAV", "*.dav"), ("Todos os Arquivos", "*.*")]
    )
    if arquivo_entrada:
        entrada_arquivo_entry.delete(0, tk.END)
        entrada_arquivo_entry.insert(0, arquivo_entrada)


def selecionar_arquivo_saida():
    arquivo_saida = filedialog.asksaveasfilename(
        title="Salvar como",
        defaultextension=".mp4",
        filetypes=[("Arquivos MP4", "*.mp4"), ("Todos os Arquivos", "*.*")]
    )
    if arquivo_saida:
        saida_arquivo_entry.delete(0, tk.END)
        saida_arquivo_entry.insert(0, arquivo_saida)


def iniciar_conversao():
    arquivo_entrada = entrada_arquivo_entry.get().strip()
    arquivo_saida = saida_arquivo_entry.get().strip()

    if not arquivo_entrada or not os.path.exists(arquivo_entrada):
        messagebox.showerror("Erro", "Selecione um arquivo .DAV válido.")
        return

    if not arquivo_saida:
        messagebox.showerror("Erro", "Selecione um local válido para salvar o arquivo.")
        return

    # Desativar o botão de conversão e mudar o texto
    converter_botao.config(state=tk.DISABLED, text="Aguarde, convertendo arquivo...", bg="yellow")

    def executar_conversao():
        try:
            converter_dav_para_mp4(arquivo_entrada, arquivo_saida)
            messagebox.showinfo("Sucesso", f"Conversão concluída!\nSalvo em: {arquivo_saida}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a conversão:\n{e}")
        finally:
            # Reativar o botão e restaurar o texto
            converter_botao.config(state=tk.NORMAL, text="Converter", bg="#007BFF", fg="white")

    # Executar a conversão em uma thread separada
    threading.Thread(target=executar_conversao).start()


# Criar a interface gráfica
root = tk.Tk()
root.title("Conversor DAV para MP4")

# Seção de arquivo de entrada
entrada_arquivo_label = tk.Label(root, text="Selecione o arquivo de entrada (.DAV):")
entrada_arquivo_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entrada_arquivo_entry = tk.Entry(root, width=50)
entrada_arquivo_entry.grid(row=0, column=1, padx=10, pady=5)

entrada_arquivo_botao = tk.Button(root, text="Procurar...", command=selecionar_arquivo_entrada)
entrada_arquivo_botao.grid(row=0, column=2, padx=10, pady=5)

# Seção de arquivo de saída
saida_arquivo_label = tk.Label(root, text="Selecione o local para salvar (.MP4):")
saida_arquivo_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

saida_arquivo_entry = tk.Entry(root, width=50)
saida_arquivo_entry.grid(row=1, column=1, padx=10, pady=5)

saida_arquivo_botao = tk.Button(root, text="Procurar...", command=selecionar_arquivo_saida)
saida_arquivo_botao.grid(row=1, column=2, padx=10, pady=5)

# Botão de conversão
converter_botao = tk.Button(root, text="Converter", command=iniciar_conversao, bg="#007BFF", fg="white")
converter_botao.grid(row=2, column=0, columnspan=3, pady=20)

# Executar a interface gráfica
root.mainloop()
