n = str(input('Digite seu nome completo: ')).strip()

nome_list = n.split()

print('Seu primeiro nome é {} \n Seu segundo nome é {}'.format(nome_list[0] , nome_list[len(nome_list)-1]))