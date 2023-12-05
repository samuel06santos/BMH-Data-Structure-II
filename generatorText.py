# pip install lorem_text
from lorem_text import lorem

def gerador_lorem(tamanhoCadeia):
  """
  A função recebe o número limite de caracteres. 
  O número de palavras foi arbitrario para conter palavras suficientes para atender os requisitos da atividade.
  """
  
  words = 1000
  return lorem.words(words)[:tamanhoCadeia]
