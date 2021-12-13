#Lógica de Programação e Algoritmos exercicio 2
def convert_letter(letter):
   letter = letter.upper()
   if(letter == 'A'):
       return '@'
   if(letter == 'E'):
       return '&'
   if(letter == 'I'):
       return '!'
   if(letter == 'O'):
       return '#'
   if(letter == 'U'):
       return '*'
def main():
   nome = input("Digite seu nome: ")
   new_name = ''
   for i in nome:
       #print(i.upper())
       if(i.upper() == 'A' or i.upper() == 'E' or i.upper() == 'I' or i.upper() == 'O' or i.upper() == 'U'):
           new_name += convert_letter(i.upper())
       else:
           new_name += i.upper()
   print(new_name)
if __name__ == '__main__':
   main()