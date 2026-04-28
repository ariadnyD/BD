import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_atividades.settings')
django.setup()

from app.models import Funcionario, Departamento, Projeto

# Criando funcionários
f1 = Funcionario.objects.create(nome="Ana", sexo="F", dt_nasc="1988-05-07", salario=2500.00)
f2 = Funcionario.objects.create(nome="Taciano", sexo="M", dt_nasc="1980-01-25", salario=2500.00)

# Criando um departamento
depto = Departamento.objects.create(nome="Dep. Computação", sigla="DCT", descricao="Departamento de TI")

# Criando o Projeto ID 1
Projeto.objects.create(
    nome="APF", 
    descricao="Analisador de Ponto de Função", 
    depto=depto, 
    responsavel=f1, 
    data_inicio="2018-02-26", 
    data_fim="2019-06-30"
)

print("Dados iniciais criados com sucesso! O Projeto ID 1 já existe.")