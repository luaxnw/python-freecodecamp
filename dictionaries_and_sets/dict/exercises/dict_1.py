#Exercício 10 - Cadastro de Pessoa

#Crie um dicionário contendo

#{ "nome": "...", "idade": ..., "cidade": "...", "profissao": "..." }

#Mostre todas as informações.

my_dict = {'nome':'luan',
                'idade': 20,
                'cidade': 'chapecó',
                'profissão': 'programador'}

for key, item in my_dict.items():
    print(key, ":", item)