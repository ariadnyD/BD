from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    dt_nasc = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    depto = models.ForeignKey('Departamento', on_delete=models.SET_NULL, null=True, related_name='membros')

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=250)
    gerente = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, related_name='gerencia_depto')

class Projeto(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=250)
    responsavel = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    depto = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()

class Atividade(models.Model):
    descricao = models.CharField(max_length=250)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='atividades')
    data_inicio = models.DateField()
    data_fim = models.DateField()

# Create your models here.
