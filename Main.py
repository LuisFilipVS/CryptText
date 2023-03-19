from PyQt5 import QtCore, QtGui, QtWidgets
import Interface

def Tabela(): #Metodo que cria a tabela de Vigenere
    lista = []
    j = 0
    while (j < 26): 
        cont = 0
        i = 65 + j #Uso numeração com base no codigo UNICODE

        linha = []
        while cont < 26:
            if (i > 90):
                i = 65
            linha.append(chr(i))
            cont += 1
            i += 1
        lista.append(linha)
        j += 1
    return lista

def getCodigo(frase, chave): #Metodo que adiciona uma caractere de criptografia para cada caractere da frase
    i = 0
    j = 0
    keyComplete = ""
    while i < len(frase):
        if j >= len(chave):
            j = 0
        keyComplete += chave[j]
        j += 1
        i += 1
    return keyComplete

def tiraEspaço(frase): #Metodo auxiliar que trata os espaços entre as palavras (Neste caso, os espaços nao são criptografados)
    resultado = []
    localEspaços = []
    cont = 0
    i = 0
    while i < len(frase):
        if frase[i] == " ":
            frase = frase[:i] + "" + frase[i + 1:]
            localEspaços.append(i + cont)
            i -= 2
            cont += 1
        i += 1
    resultado.append(frase)
    resultado.append(localEspaços)

    return resultado

def colocaEspaço(frase, arrayPosição): #Metodo auxiliar que trata os espaços entre as palavras (Neste caso, os espaços nao são criptografados)
    while arrayPosição != []:
        frase = frase[:arrayPosição[0]] + " " + frase[arrayPosição[0]:]
        arrayPosição.pop(0)

    return frase

def decriptografar(criptografia, chave): #Metodo que realiza a decodificação da frase
    tabelaVigenere = Tabela()

    string = tiraEspaço(criptografia)

    keyComplete = getCodigo(string[0], chave)
    fraseDecriptografada = ""

    i = 0
    while i < len(keyComplete):
        j = 0
        while j < len(tabelaVigenere):
            if tabelaVigenere[ord(keyComplete[i]) - 65][j] == string[0][i]:
                fraseDecriptografada += str(chr(j + 65))
                break
            else:
                j += 1
        i += 1

    fraseDefinitiva = colocaEspaço(fraseDecriptografada, string[1])

    return fraseDefinitiva

def criptografaTexto(texto, chave): #Metodo que realiza a codificação da frase
    tabelaVigenere = Tabela()

    string = tiraEspaço(texto)

    keyComplete = getCodigo(string[0], chave)

    fraseCriptografada = ""

    i = 0
    while i < len(keyComplete):
        fraseCriptografada += str(tabelaVigenere[ord(keyComplete[i]) -
                                                 65][ord(string[0][i]) - 65])
        i += 1

    fraseCriptografada = colocaEspaço(fraseCriptografada, string[1])

    return fraseCriptografada

def main(): #Metodo principal que aciona a interface e realiza todas as operações e chamadas de funções
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Interface.Ui_Dialog()
    ui.setupUi(Dialog)

    ui.label_Answer.hide()

    def executaCriptografia():
        frase = ui.lineEdit_Text.text().upper()
        chave = ui.lineEdit_Key.text().upper()

        ui.label_Answer.show()
        ui.label_Answer.setText(str(criptografaTexto(frase,chave)))    

        pass

    def executaDecriptografia():
        frase = ui.lineEdit_Text.text().upper()
        chave = ui.lineEdit_Key.text().upper()

        ui.label_Answer.show()
        ui.label_Answer.setText(str(decriptografar(frase,chave)))    

        pass

    #Atribuição de Eventos

    ui.pushButton_Cript.clicked.connect(lambda: executaCriptografia())

    ui.pushButton_Decript.clicked.connect(lambda: executaDecriptografia())

    Dialog.show()
    sys.exit(app.exec_())

    pass

main()