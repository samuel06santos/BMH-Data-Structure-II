# Discentes:
# Fantiny Santos dos Santos 202211140005
# Ilana Thaise Da Silva Pereira 202211140038
# João Samuel Dias Santos 202211140033
# Kevin Washington Azevedo da Cruz 202211140006
# Kim Lima de Lima 202211140014

from BMH import BMH
from generatorText import gerador_lorem

### A função `BMH` retorna uma lista de inteiros (caso tenha mais de um caso do padrão no texto) que correspondem aos índices no texto onde o padrão foi encontrado.
### A função `gerador_lorem` retorna um texto com `n`(parametro) caracteres

texto = None

while True:
  opcao = input("""\nEscolha uma opção:
0 - Sair
1 - Gerar texto
2 - Procurar padrao no texto
> """)

  try:
    opcao = int(opcao)
  except:
    print("Opção inválida, escolha novamente!")
    continue

  if opcao == 0:
    break
    
  #Abre menu de geracao de texto
  elif opcao == 1:
    while True:
      opcao1 = input("""\nEscolha uma opção:
0 - Não gerar o texto
1 - 500 caracteres 
2 - 1.000 caracteres
3 - 1.500 caracteres
4 - 2.000 caracteres
5 - 3.000 caracteres
> """)
      try:
        opcao1 = int(opcao1)
      except:
        print("Opção inválida, escolha novamente!")
        continue

      if opcao1 == 0:
        break

      #Gera texto de 500 caracteres
      elif opcao1 == 1:
        texto: str = gerador_lorem(500)
        print(f"Texto gerado: {texto}")
        break
        
      #Gera texto de 1000 caracteres
      elif opcao1 == 2:
        texto: str = gerador_lorem(1000)
        print(f"Texto gerado: {texto}")
        break
        
      #Gera texto de 1500 caracteres
      elif opcao1 == 3:
        texto: str = gerador_lorem(1500)
        print(f"Texto gerado: {texto}")
        break

      #Gera texto de 2000 caracteres
      elif opcao1 == 4:
        texto: str = gerador_lorem(2000)
        print(f"Texto gerado: {texto}")
        break
      
      #Gera texto de 3000 caracteres
      elif opcao1 == 5:
        texto: str = gerador_lorem(3000)
        print(f"Texto gerado: {texto}")
        break
        
  #Busca e mostra padrao no texto
  elif opcao == 2:
    if (texto == None):
      print("Você precisa gerar um texto primeiro!")
      continue
    else:
      texto_temp = texto
      pintar = lambda string: f"\033[102m{string}\033[0m"
      padrao: str = input("Padrão para ser buscado no texto:\n> ")
      resultado = BMH(texto_temp, padrao)
      for e, i in enumerate(resultado):
        i += 10 * e  # faz a correção do tamanho da string (funcao `pintar` altera)
        texto_temp = texto_temp[:i] + pintar(
          texto_temp[i:i + len(padrao)]) + texto_temp[i + len(padrao):]
      print(texto_temp, end="\n\n")

      if resultado:
        print(f"O padrão ´{padrao}´ foi encontrado nos índices: {', '.join(map(str, resultado[:-1]))} e {resultado[-1]}.")
      else:
        print(f"O padrão ´{padrao}´ não foi encontrado no texto!!")
