alunos = {}

# cadastro de alunos:
alunos['aluno1'] = {
    "nome": 'João Gabriel Gonçalves Bertolin',
    "ra": '172619342',
    "email": 'joaogabrielbertolin2@gmail.com'
}

alunos['aluno2'] = {
    "nome": 'Aluno fictício',
    "ra": '123456789',
    "email": 'alunoficticio123456789@gmail.com'
}

# listar alunos cadastrados:
print("Alunos cadastrados: ",alunos)

# consultar informações de um aluno:
print("Informações do 1º aluno",alunos['aluno1'])

# excluir um aluno:
del alunos['aluno2']
print("aluno2 excluído")
print(alunos)

#link github: https://github.com/Joao-3/atividadeGitHub
