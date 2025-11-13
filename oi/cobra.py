import turtle, time, random                     # Importa bibliotecas

delay, pontos, maior_ponto = 0.1, 0, 0          # Variáveis iniciais

wn = turtle.Screen()                            # Cria janela
wn.title("Jogo Da Cobra")                       # Título
wn.bgcolor("black")                             # Fundo
wn.setup(1920, 1080)                              # Tamanho
wn.tracer(0)                                    # Atualização manual

head = turtle.Turtle()                          # Cabeça da cobra              
head.shape("square")
head.color("gray")                   
head.penup()                                    # Evita riscos
head.direction = "stop"                         # Começa parada

food = turtle.Turtle()                          # Cria comida
food.shape("circle")                            # Forma
food.color("red")                                # Cor
food.penup()                                    # Sem linha
food.goto(0, 100)                                # Posição inicial

segments = []                                    # Lista do corpo

pen = turtle.Turtle()                            # Placar
pen.hideturtle()                                 # Oculta ícone
pen.penup()                                      # Sem risco
pen.color("white")                               # Cor do texto
pen.goto(0, 450)                                 # Posição
pen.write("Pontos: 0  Maior Pontuação: 0", align="center", font=("Courier", 24))  # Texto inicial

def move():                                      # Movimenta cabeça
    x, y = head.xcor(), head.ycor()              # Pega posição
    if head.direction == "up": head.sety(y+20)   # Sobe
    if head.direction == "down": head.sety(y-20) # Desce
    if head.direction == "left": head.setx(x-20) # Esquerda
    if head.direction == "right": head.setx(x+20)# Direita

def go_up():    head.direction = "up"    if head.direction != "down" else "down"   # Evita inverter
def go_down():  head.direction = "down"  if head.direction != "up"   else "up"
def go_left():  head.direction = "left"  if head.direction != "right"else "right"
def go_right(): head.direction = "right" if head.direction != "left" else "left"

wn.listen()                                     # Escuta teclado
wn.onkeypress(go_up, "w")                       # Movimento
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

def update_score():                              # Atualiza placar
    pen.clear()                                  # Apaga
    pen.write(f"Pontos: {pontos}  Maior Pontuação: {maior_ponto}",
              align="center", font=("Courier", 24))  # Reescreve

def reset_game():                                # Reinicia jogo
    global pontos, delay                          # Variáveis globais
    time.sleep(1)                                 # Pausa
    head.goto(0, 0)                               # Volta ao centro
    head.direction = "stop"                       # Para
    for seg in segments: seg.goto(1000, 1000)     # Some com corpo
    segments.clear()                              # Limpa lista
    pontos, delay = 0, 0.1                        # Reseta valores
    update_score()                                # Atualiza texto

while True:                                       # Loop do jogo
    wn.update()                                   # Atualiza tela

    if abs(head.xcor()) > 960 or abs(head.ycor()) > 960:  # Bateu na borda?
        reset_game()                              # Reinicia

    if head.distance(food) < 20:                  
        food.goto(random.randint(-960, 960), random.randint(-560, 560))  # Nova posição
        seg = turtle.Turtle()                     # Novo segmento
        seg.shape("circle")                       # Corpo
        seg.color("white")                        # Branco
        seg.penup()                               # Sem risco
        segments.append(seg)                      # Adiciona corpo
        delay = max(0.01, delay - 0.001)          # Aumenta velocidade
        pontos += 10                               # Soma pontos
        maior_ponto = max(maior_ponto, pontos)     # Atualiza recorde
        update_score()                             # Atualiza tela

    for i in range(len(segments)-1, 0, -1):       # Move corpo
        segments[i].goto(segments[i-1].pos())     # Segmento segue anterior
    if segments: segments[0].goto(head.pos())     # Primeiro segue a cabeça

    move()                                        # Move cabeça

    if any(seg.distance(head) < 20 for seg in segments):  # Bateu no corpo?
        reset_game()                              # Reinicia

    time.sleep(delay)                              # Delay

wn.mainloop()                                      # Mantém janela aberta
