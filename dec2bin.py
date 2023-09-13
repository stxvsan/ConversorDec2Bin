def dec2bin(numero_decimal, numero_bits):
  numero_binario = bin(numero_decimal)
  numero_binario = numero_binario[2:len(numero_binario)]

  while len(numero_binario) < numero_bits:
  numero_binario = "0" + numero_binario
  return numero_binario





if __name__ == "__main__":
  numero_binario = int (input("Escribe el numero en decimal que quieres convertir:  "))
  numero_bits = int (input("Cuantos bits tendra el numero binario:  "))
  numero_binario = dec2bin(numero_decimal, numero_bits)
  print("El numero " + str(numero_decimal) + " es " + numero_binario + " en binario con " + str(numero_bits) + " bits.")
