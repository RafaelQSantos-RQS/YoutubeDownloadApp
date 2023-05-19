import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube

window = tk.Tk() # Criação da caixa de texto
window.title("Meu Youtube App") # Defininfo o titulo da janela

# Define o tamanho da janela em pixels
largura = 250
altura = 150

# Calcula a posição para centralizar a janela na tela
posicao_x = (window.winfo_screenwidth() - largura) // 2
posicao_y = (window.winfo_screenheight() - altura) // 2

# Define a posição e o tamanho da janela
window.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

# Define o número de colunas da janela como 2
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

def download():
    link = textbox.get()
    midia = droplist.get()

    # Verifica se todos os campos foram preenchidos corretamente
    if not link:
        messagebox.showerror("Erro", "O campo link deve ser preenchido corretamente.")
        return
    if not midia:
        messagebox.showerror("Erro", "O campo tipo de mídia deve ser preenchido corretamente.")
        return
    
    # Prossegue com o download
    try:
        yt = YouTube(link)
        if(midia == 'Vídeo'):
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path="Videos")
        else:
            ys = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            ys.download(output_path="Áudios")
    except Exception as e:
        messagebox.showerror("Erro",f"Ocorreu um erro:{str(e)}")

##### LINK #####
link_label = tk.Label(window, text="Insira o link") # Cria o rótulo (label) para o texto descritivo
link_label.grid(row=0,column=0,sticky="w") # Posicionando em cima da caixa de texto
textbox = tk.Entry(window) # Criação da caixa de texto
textbox.grid(row=0,column=1,sticky="we") # Posiciona a caixa de entrada de texto na janela

##### Midia #####
midia_label = tk.Label(window, text="Midia") # Cria o rótulo (label) para o texto descritivo
midia_label.grid(row=1,column=0,sticky="w") # Posicionando em cima da combobox
droplist = ttk.Combobox(window,values=["Vídeo","Áudio"],state="readonly")
droplist.grid(row=1,column=1,sticky="we")

download_button = tk.Button(window,text="Download",command=download)
download_button.grid(row=2,column=1,rowspan=1,columnspan=2,sticky="we")

window.mainloop()