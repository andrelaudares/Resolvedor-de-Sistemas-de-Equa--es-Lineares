'''
 Resolvedor de Sistemas de Equações Lineares
 
André Laudares Soares - 22001646
Guilherme Ferreira Jorge - 22007283
Raul Migliari - 22005575
'''

def carregaMatriz (nomeArq):
    arq     = open(nomeArq,"r")
    qtdLins = int (arq.readline())
    
    ret = []
    for lin in range(qtdLins):
        texto = arq.readline().split()
        
        linha = []
        for col in range(qtdLins+1):
            linha.append(float(texto[col])) 
            
        ret.append(linha)
        
    arq.close()
    return ret

def divisaoElementos(a,b):
    if a == 0 and b == 0:
        return 'indeterminado'
    elif b == 0:
        return 'infinito'
    else:
        return a/b

def divisaoLinhas(m,lin1,lin2):
    ret = []
    for col in range(len(m[lin1])-1):
        ret.append(divisaoElementos(m[lin1][col],m[lin2][col]))

    resultado = ret[0]
    igual = True

    for item in ret:
        if resultado != item:
            igual = False
            break

    if igual == True:
        print("<<<ERRO: Uma das linhas é originada de outra linha, tente outro sistema>>>")
        exit()

def permuta (m, perm, perms):
    if m==[]:
        perms.append(perm)
    else:
        for lin in range(len(m)):
            permuta(m[0:lin]+m[lin+1:len(m)],perm+[m[lin]],perms)

def permutacoes (m):
    perms=[]
    permuta(m,[],perms)
    return perms

def haZeroNaDiagonal(m):

    qtdDeZeros=0
    posicao=0
    
    while posicao<len(m):
        if m[posicao][posicao]==0:
            qtdDeZeros+=1
        posicao+=1

    return qtdDeZeros>0

def poeUmNaDiagonalPrincipalNaLinha (lin,m):

    divisor = m[lin][lin]

    for col in range(len(m)+1):
        m[lin][col] /= divisor

def multiplicaSubtraiLinha(col,m,lin):

    const = m[lin][col]

    for col1 in range(len(m[col])):
        m[lin][col1] -= (m[col][col1]*const)

matrizOriginal = carregaMatriz("sistema.txt")

matrizAll = permutacoes(matrizOriginal)

x = 0
while x < len(matrizAll):

    matriz = matrizAll[x]

    while haZeroNaDiagonal(matriz):
        x += 1
        if x == len(matrizAll):
            print("<<<ERRO: Na resolução aparece um zero na diagonal, tente outro sistema>>>")
            exit()
        matriz = matrizAll[x]

    linhas = len(matriz)
    
    for linha in range(linhas):
        for var1 in range(linhas):
            if linha != var1:
                divisaoLinhas(matriz,linha,var1)

    for linha in range(linhas):
        poeUmNaDiagonalPrincipalNaLinha(linha,matriz)

        for var1 in range(linhas):
            if linha != var1:
                multiplicaSubtraiLinha(linha,matriz,var1)
                while haZeroNaDiagonal(matriz):
                    x += 1
                    if x == len(matrizAll):
                        print("<<<ERRO: Na resolução aparece um zero na diagonal, tente outro sistema>>>")
                        exit()
                    matriz = matrizAll[x]
    break

for var2 in range(linhas):
    print(f'A variável {var2+1} é igual á: {matriz[var2][linhas]}')