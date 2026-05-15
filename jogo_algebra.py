import random
import tkinter as tk
from textblob import TextBlob

class JogoCalculoAlgebrico:
    def __init__(self, root):
        # Inicializa a janela principal do aplicativo
        self.root = root
        self.root.title("Jogo de Cálculo Algébrico")
        
        # Define as dimensões da tela e impede que o usuário redimensione a janela
        self.root.geometry("450x650")
        self.root.resizable(False, False)
        
        # Define a cor de fundo predominante (um tom claro de cinza azulado)
        self.root.configure(bg="#f4f6f9")

        # Variáveis globais para armazenar o estado da partida atual
        self.pontuacao = 0
        self.problema = ""
        self.resposta_correta = 0

        # Definição de estilos de fonte para padronizar o design
        fonte_titulo = ("Helvetica", 16, "bold")
        fonte_normal = ("Helvetica", 14)
        fonte_destaque = ("Helvetica", 28, "bold")

        # Criação do placar que fica no topo da tela, fora do quadro principal
        self.label_placar = tk.Label(root, text=f"Pontuação: {self.pontuacao}", font=fonte_normal, bg="#f4f6f9", fg="#2980b9")
        self.label_placar.pack(pady=(15, 0))

        # Quadro principal que funciona como um cartão central branco
        self.frame_principal = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
        self.frame_principal.pack(pady=15, padx=25, fill="both", expand=True)

        # Rótulo de instrução para o jogador
        self.label_problema = tk.Label(self.frame_principal, text="Resolva a equação:", font=fonte_titulo, bg="#ffffff", fg="#34495e")
        self.label_problema.pack(pady=(20, 10))

        # Rótulo em tamanho grande onde a equação matemática será exibida
        self.problema_texto = tk.Label(self.frame_principal, text="", font=fonte_destaque, bg="#ecf0f1", fg="#2c3e50", width=8)
        self.problema_texto.pack(pady=10)

        # Campo de entrada de texto onde o usuário vai digitar o número da resposta
        self.entry_resposta = tk.Entry(self.frame_principal, font=("Helvetica", 16), justify="center", bd=1, relief="solid", bg="#fdfdfd")
        self.entry_resposta.pack(pady=15, ipady=5)
        
        # Vincula a tecla Enter do teclado para executar a função de verificação automaticamente
        self.entry_resposta.bind("<Return>", lambda event: self.verificar_resposta())

        # Botão verde para confirmar a resposta matemática
        self.botao_verificar = tk.Button(self.frame_principal, text="Verificar Resposta", command=self.verificar_resposta, font=fonte_normal, bg="#27ae60", fg="white", activebackground="#2ecc71", activeforeground="white", relief="flat", cursor="hand2")
        self.botao_verificar.pack(pady=10, ipadx=15, ipady=5)

        # Espaço reservado para avisar se o jogador acertou ou errou
        self.label_feedback = tk.Label(self.frame_principal, text="", font=("Helvetica", 12, "bold"), bg="#ffffff")
        self.label_feedback.pack(pady=5)

        # Criação de um subquadro oculto dedicado apenas à coleta do sentimento
        self.frame_sentimento = tk.Frame(self.frame_principal, bg="#ffffff")
        
        # Pergunta exibida após a resolução do problema
        self.label_pergunta = tk.Label(self.frame_sentimento, text="Como você se sentiu com essa questão?", font=("Helvetica", 11), bg="#ffffff", fg="#34495e")
        self.label_pergunta.pack(pady=(10, 5))
        
        # Campo onde o jogador digita como se sentiu
        self.entry_sentimento = tk.Entry(self.frame_sentimento, font=("Helvetica", 12), justify="center", bd=1, relief="solid", bg="#fdfdfd", width=25)
        self.entry_sentimento.pack(ipady=3)
        self.entry_sentimento.bind("<Return>", lambda event: self.processar_sentimento())

        # Botão para enviar a frase de sentimento para análise
        self.botao_enviar_sentimento = tk.Button(self.frame_sentimento, text="Enviar Feedback", command=self.processar_sentimento, font=("Helvetica", 10, "bold"), bg="#f39c12", fg="white", activebackground="#e67e22", activeforeground="white", relief="flat", cursor="hand2")
        self.botao_enviar_sentimento.pack(pady=10, ipadx=10)

        # Rótulo para exibir a mensagem motivacional gerada pela análise de texto
        self.label_reforco = tk.Label(self.frame_principal, text="", font=("Helvetica", 12, "italic"), bg="#ffffff", fg="#7f8c8d", wraplength=350, justify="center")
        self.label_reforco.pack(pady=10)

        # Botão azul na parte inferior para iniciar uma nova rodada do zero
        self.botao_novo_problema = tk.Button(root, text="Gerar Novo Problema", command=self.novo_problema, font=fonte_normal, bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", relief="flat", cursor="hand2")
        self.botao_novo_problema.pack(side="bottom", pady=20, ipadx=20, ipady=5)

        # Chama a função pela primeira vez para garantir que o jogo já inicie com um problema pronto
        self.novo_problema() 

    def gerar_problema(self):
        # Sorteia aleatoriamente se a conta será de mais ou de menos
        operador = random.choice(['+', '-'])
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        
        # Regra simples para evitar números negativos em contas de subtração
        if operador == '-' and a < b:
            a, b = b, a
            
        # Formata a equação em formato de texto
        problema = f"{a} {operador} {b}"
        
        # A função eval resolve a string matemática de forma automática
        resposta_correta = eval(problema)
        return problema, resposta_correta

    def analisar_sentimento(self, texto):
        try:
            # Tenta usar a biblioteca TextBlob para traduzir o texto para inglês
            blob = TextBlob(texto)
            blob_traduzido = blob.translate(from_lang='pt', to='en')
            
            # Avalia se a frase é positiva ou negativa usando o motor nativo em inglês
            sentimento = blob_traduzido.sentiment.polarity
        except Exception:
            # Caso não haja internet ou a API falhe, usa um sistema de palavras de emergência
            palavras_positivas = ['bem', 'ótimo', 'bom', 'fácil', 'legal', 'feliz', 'tranquilo']
            palavras_negativas = ['mal', 'ruim', 'difícil', 'triste', 'frustrado', 'chato', 'complicado']
            
            # Converte tudo para minúsculo para facilitar a busca
            texto_min = texto.lower()
            
            if any(p in texto_min for p in palavras_positivas):
                return 'positivo'
            elif any(p in texto_min for p in palavras_negativas):
                return 'negativo'
            else:
                return 'neutro'
                
        # Se a tradução funcionou, retorna positivo para valores maiores que zero
        return 'positivo' if sentimento > 0 else 'negativo'

    def reforco_positivo(self, sentimento):
        # Retorna uma frase escolhida aleatoriamente com base na avaliação do humor do jogador
        if sentimento == 'positivo':
            return random.choice([
                "Ótimo trabalho! Continue assim!",
                "Você está indo muito bem, continue se esforçando!",
                "Excelente! Matemática é seu forte!",
            ])
        elif sentimento == 'neutro':
            return "Tudo bem, o importante é continuar praticando!"
        else:
            return random.choice([
                "Não desista! Você consegue!",
                "Vamos tentar novamente, você vai melhorar!",
                "A prática leva à perfeição, continue tentando!",
            ])

    def atualizar_placar(self):
        # Atualiza o texto visual do placar com a pontuação atual
        self.label_placar.config(text=f"Pontuação: {self.pontuacao}")

    def novo_problema(self):
        # Aciona a criação matemática e atualiza a tela
        self.problema, self.resposta_correta = self.gerar_problema()
        self.problema_texto.config(text=self.problema)
        
        # Destrava a caixa de resposta, apaga o conteúdo antigo e coloca o foco lá
        self.entry_resposta.config(state="normal")
        self.entry_resposta.delete(0, tk.END)
        self.entry_resposta.focus()
        
        # Limpa as mensagens de feedback da rodada anterior
        self.label_feedback.config(text="")
        self.label_reforco.config(text="")
        
        # Esconde completamente a seção de análise de sentimentos até a próxima resposta
        self.frame_sentimento.pack_forget()
        self.entry_sentimento.delete(0, tk.END)

    def verificar_resposta(self):
        try:
            # Tenta converter o texto digitado em um número inteiro
            resposta = int(self.entry_resposta.get())
            
            # Lógica de acerto e erro
            if resposta == self.resposta_correta:
                self.label_feedback.config(text="Correto!", fg="#27ae60")
                self.pontuacao += 1
                self.atualizar_placar()
            else:
                self.label_feedback.config(text=f"Incorreto! A resposta certa era {self.resposta_correta}.", fg="#e74c3c")
            
            # Bloqueia a edição do campo de resposta para evitar alterações
            self.entry_resposta.config(state="disabled")
            
            # Torna visível o painel de feedback emocional
            self.frame_sentimento.pack(pady=10)
            self.entry_sentimento.focus()

        except ValueError:
            # Avisa o usuário caso ele digite letras ou caracteres especiais
            self.label_feedback.config(text="Por favor, insira um número válido.", fg="#e67e22")

    def processar_sentimento(self):
        # Pega o texto de sentimento e remove os espaços em branco das pontas
        texto = self.entry_sentimento.get()
        
        # Só processa se o campo não estiver completamente vazio
        if texto.strip() != "":
            # Executa a análise e exibe a mensagem de incentivo na tela
            sentimento = self.analisar_sentimento(texto)
            mensagem_reforco = self.reforco_positivo(sentimento)
            self.label_reforco.config(text=mensagem_reforco)
            
            # Remove o painel de texto de sentimento novamente para manter a interface limpa
            self.frame_sentimento.pack_forget()

# Ponto de entrada do programa
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoCalculoAlgebrico(root)
    root.mainloop()