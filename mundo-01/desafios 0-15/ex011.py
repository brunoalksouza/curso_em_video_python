print ('quais as diensoes da suas parede?')
largura = float(input('digite a largura:'))
altura = float(input('digite a altura:'))
area = largura*altura

print ('sua parede tem {}x{} e sua area é de {}m²'.format(largura, altura, (area)))
print('voce vai precisar de {}l de tinta'.format((area)/2))
