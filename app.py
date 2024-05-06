import webbrowser
import pyautogui as py
from time import sleep

def deslogar():
    py.click(1305,614,duration=2)
    py.click(1874,108,duration=2)
    py.click(1761,352,duration=2)

while True:
    #Navegar ate o sit https://www.instagram.com
    webbrowser.open('https://www.instagram.com')
    sleep(1)

    #Entrar com meu usuario
    py.click(1539,362,duration=1)
    sleep(1)
    py.typewrite('usuario')
    sleep(1)

    #Entrar com a minha senha
    py.click(1546,398,duration=1)
    sleep(1)
    py.typewrite('senha')
    sleep(1)

    #Clicar em login
    py.click(1567,445,duration=1)
    sleep(10)

    #Clicar em "Not now" para não salvar navegador
    py.click(1590,603, duration=1)
    sleep(10)

    #Fechar janela de "salvar senha"
    py.click(1662,88, duration=1)
    sleep(1)

    #Pesquisar pela pagina
    py.click(1526,105, duration=1)
    sleep(1)
    py.typewrite('nike')
    sleep(1)

    #Entrar na página
    py.move(0,50,duration=1)
    sleep(1)
    py.click()
    sleep(10)

    #Clicar na postagem mais recente
    py.click(1398,595,duration=1)
    sleep(10)

    #Verificar se ja curti ou não a postagem
    coracao = py.locateCenterOnScreen('coracao_curtida.png')
    sleep(1)

    #Se ja tiver curtido, não fazer nada e aguardar 24h
    if coracao is not None:
        sleep(86400) #Aguardar 24 horas
        
    #Se não tiver curtido, curtir a foto
    elif coracao == None:
        deslogar()
        sleep(86400)
        #Se ja tiver curtido, comentar tambem na postagem
        py.click(1505,749,duration=1)
        sleep(3)
        py.click(1568,834,duration=1)
        sleep(1)
        py.typewrite('comentario')
        sleep(1)
        py.click(1715,832,duration=1)
        
        #Sai da conta
        deslogar()
        #Pausar por 24h
        sleep(86400)