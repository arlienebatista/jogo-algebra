# Jogo de Cálculo Algébrico 🔢

## Sobre o Projeto

O Jogo de Cálculo Algébrico é uma aplicação interativa desenvolvida em Python com foco em educação e engajamento. O objetivo principal é auxiliar no treinamento de operações matemáticas básicas de forma lúdica e visualmente agradável. 

Além de gerar equações aleatórias para o usuário resolver, o sistema conta com um diferencial: a avaliação emocional contínua. Ao final de cada rodada, o jogador compartilha como se sentiu ao resolver a questão e recebe um feedback motivacional personalizado gerado através de Processamento de Linguagem Natural (NLP).

## Funcionalidades Principais

* **Geração Dinâmica:** Criação automática de problemas algébricos de adição e subtração.
* **Interface Gráfica:** Design limpo, focado e amigável construído com a biblioteca Tkinter nativa.
* **Placar em Tempo Real:** Acompanhamento da pontuação do jogador a cada acerto.
* **Análise de Sentimentos:** Integração com a biblioteca TextBlob para interpretar o feedback emocional do usuário após cada rodada.
* **Mensagens Adaptativas:** Sistema de respostas motivacionais que variam de acordo com a polaridade do texto digitado (positivo, negativo ou neutro).

## Tecnologias Utilizadas

* **Python 3.x:** Linguagem principal de desenvolvimento.
* **Tkinter:** Criação da Interface Gráfica de Usuário (GUI).
* **TextBlob:** Biblioteca para análise léxica e extração do sentimento do texto.

## Como Executar o Projeto

### Pré-requisitos

Certifique que o Python esteja devidamente instalado no seu sistema. Além disso, as bibliotecas externas necessárias estão listadas no arquivo `requirements.txt`.

### Passo a Passo

1. Clone este repositório para o seu ambiente local usando o comando:
   `git clone https://github.com/seu-usuario/nome-do-repositorio.git`
2. Navegue até a pasta raiz do projeto através do seu terminal.
3. Instale as dependências requeridas executando:
   `pip install -r requirements.txt`
4. Inicie o jogo executando o script principal (substitua pelo nome correto do seu arquivo):
   `python jogo_calculo.py`

## Licença

Este projeto é de código aberto e está disponível para que a comunidade possa utilizá-lo, modificá-lo e sugerir novas implementações.
