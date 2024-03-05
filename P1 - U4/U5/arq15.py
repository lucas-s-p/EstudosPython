falhas = []
while True:
  faltas = input()
  
  if faltas == '.F.F.F.F.F': break
  armazenamento = []

  contador = 0
  for falta in faltas:
    if falta == "F":
      contador += 1
    elif falta == '.' and contador !=0:
      armazenamento.append(contador)
      contador = 0
  
  if contador != 0:
    armazenamento.append(contador)
    falhas.append(armazenamento)

for falha in falhas:
  acumulador = ''
  contador_ = 0
  for i_falha in range(len(falha)):
    contador_ += falha[i_falha]
    if i_falha != len(falha)-1:
      acumulador += f"{falha[i_falha]} + "
    else:
      acumulador += f"{falha[i_falha]}"
  if contador_ > 0:
    print(f"{contador_} falha(s): {acumulador}")
  else:
    print(print(f"{contador_} falha(s)"))
