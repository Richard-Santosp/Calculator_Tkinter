valores = ''
# Função para exibir valores no campo
def exibir_valor(campo, item):
    global valores
    valores += item
    campo.set(valores)

# Função para apresentar o resultado
def resultado(campo):
    global valores
    try:
        resultado = eval(valores)
        campo.set(resultado)
        valores = str(resultado)
    except SyntaxError:
        campo.set("Erro de sintaxe")
        valores = ""

# Função o botão de limpar  o campo
def limpar_campo(campo):
    global valores
    valores = ''
    campo.set('')