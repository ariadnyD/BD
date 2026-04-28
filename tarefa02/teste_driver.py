import sqlite3

# O SQLite no Django fica na raiz com este nome
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# a. Inserir atividade (Projeto ID 1)
cursor.execute("INSERT INTO app_atividade (descricao, projeto_id, data_inicio, data_fim) VALUES (?, ?, ?, ?)", 
               ('Nova Atividade Driver', 1, '2024-01-01', '2024-01-10'))

# b. Atualizar líder (Projeto ID 1, Funcionario ID 2)
cursor.execute("UPDATE app_projeto SET responsavel_id = ? WHERE id = ?", (2, 1))

# c. Listar projetos e atividades
cursor.execute("""
    SELECT p.nome, a.descricao FROM app_projeto p 
    LEFT JOIN app_atividade a ON p.id = a.projeto_id
""")
for row in cursor.fetchall():
    print(f"Projeto: {row[0]} | Atividade: {row[1]}")

conn.commit()
conn.close()