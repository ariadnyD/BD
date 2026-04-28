import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_atividades.settings')
django.setup()

from app.models import Projeto, Atividade, Funcionario

# a. Inserir atividade
proj = Projeto.objects.get(id=1)
Atividade.objects.create(descricao="Nova Atividade ORM", projeto=proj, data_inicio="2024-01-01", data_fim="2024-01-10")

# b. Atualizar líder
proj.responsavel = Funcionario.objects.get(id=2)
proj.save()

# c. Listar
for p in Projeto.objects.all():
    print(f"Projeto: {p.nome}")
    for a in p.atividades.all():
        print(f"  - {a.descricao}")