print('-=' * 20)
print('ANALISTA DE TURMAS'.center(40))
print('-='* 20)
alunos = []
dados_temp = []
while True:

    dados_temp.append(str(input('Nome: ')))
    dados_temp.append(float(input('1ª nota: ')))
    dados_temp.append(float(input('2ª nota: ')))
    alunos.append(dados_temp[:])
    dados_temp.clear()

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break

print('-=' * 20)
print('MÉDIA DOS ALUNOS'.center(40))
print('-=' * 20)
print(f'{'Nome: ':<20} {'Média: ':<8}')
print('--' * 20)
for cada_aluno in alunos:
    media = (cada_aluno[1] + cada_aluno[2]) / 2
    print(f'{cada_aluno[0]:<20} {media:<7.1f}')
maior_media = 0
melhor_aluno = ''
print('-=' * 20)
for indice, cada_aluno in enumerate(alunos):
    media = (cada_aluno[1] + cada_aluno[2]) / 2
    if indice == 0:
        maior_media = media
        melhor_aluno = cada_aluno[0]
    else:
        if media > maior_media:
            maior_media = media
            melhor_aluno = cada_aluno[0]
print(f'Ao todo, foram cadastrados {len(alunos)} alunos')
print(f'O aluno que teve o maior rendimento foi [{melhor_aluno}] que teve [{maior_media:.1f}]')

