def BMH(texto: str, padrao: str) -> list:
  n, m = len(texto), len(padrao)
  
  # A priori, cria um dicionário contendo os caracteres do conjunto do `padrao` como chaves, e todos os valores são setados para o tamanho do `padrao`
  tabela: dict = {caractere: m for caractere in set(padrao)}
  for i in range(m - 1):
    tabela[ padrao[i] ] = m - i - 1
  # print(tabela)
  
  resultado: list = []
  
  i = 0
  while i <= n - m:
    j = m - 1
    while j >= 0 and padrao[j] == texto[i + j]:
      j -= 1
  
    if j < 0:
      resultado.append(i)
      i += m
  
    else:
      # Pega o valor do caractere na tabela, se nao existir o valor é igual a `m`
      i += tabela.get(texto[i + (m - 1)], m)

  return resultado
