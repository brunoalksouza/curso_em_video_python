import random

alunos = ['aluno1', 'aluno2', 'aluno3', 'aluno4']

print('o aluno que vai apagar o quando vai ser o {} de um maximo de {} alunos'.format(
    random.choice(alunos), len(alunos)))
