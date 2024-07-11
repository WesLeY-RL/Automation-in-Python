
# passo -1 Entrar no sistema criado
# passo  -2 fazer login 
# passo -3 importar a base de dados
# passo  - 4 cadastrar um produto 
# passo - 5 repetir o passo 4  até terminar todos os produtos

# instalar o pyautogui -- uma biblioteca de automação 



import pyautogui

# definindo tempo de execução para cada ação
pyautogui.PAUSE = 1 

#passo 1

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.doubleClick(x=423, y=317)
pyautogui.doubleClick(x=423, y=61)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#passo 2

pyautogui.doubleClick(x=536, y=372)
pyautogui.write("nsbijdsbfsdbuh")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("enter")

import pandas as pd

df = pd.read_csv("")

print(df)
# passo 4

for linha in df.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = df.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(df.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = df.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(df.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
