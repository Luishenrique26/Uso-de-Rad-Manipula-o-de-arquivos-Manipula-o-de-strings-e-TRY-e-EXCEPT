# cria um arquivo de exemplo e escreve um conteúdo nele.
with open("Lh.txt", "w", encoding ="utf-8") as f:
 f.write("exemplo de uso dos métodos seek() e tell () em python.")

 # Abre o arquivo para leitura e demonstra o uso de seek() e tell ()
 with open("Lh.txt", "r", encoding="utf-8") as f:
  # Posição inicial do cursor
  print("posição inicial do cursor:" ,f.tell())

  # le os primeiros 10 caracteres
  conteudo = f.read(10)
  print("conteúdo lido:", conteudo)
  print("posição do cursor após ler 10 caracteres:", f.tell())

  # volta para o início do arquivo.
  f.seek (0,0) # whence=0 início do arquivo

  print("posição do cursor após seek(0,0):", f.tell())