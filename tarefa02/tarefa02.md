# Tarefa: ODBC e ORM

Este documento apresenta uma visão técnica sobre as tecnologias de integração de banco de dados utilizadas no desenvolvimento de software, com foco na linguagem **Python**.

## 1. Scripts e Programas Criados

* [Script de Criação do Banco de Dados](./scripts/database_setup.sql)
* [Programa Principal (Back-end)](./src/main.py)
* [Definição de Modelos (ORM)](./src/models.py)

---

## 2. ODBC (Open Database Connectivity) em Python

O **ODBC** é um padrão de interface de programação de aplicações (API) para acessar sistemas de gerenciamento de banco de dados (SGBD). Ele foi projetado para ser independente de linguagens de programação e de sistemas operacionais.

Na linguagem **Python**, a utilização de ODBC permite que a aplicação se conecte a diversos bancos de dados (como PostgreSQL, SQL Server ou MySQL) de forma uniforme, desde que o driver correspondente esteja instalado. A biblioteca mais comum para essa finalidade é a `pyodbc`.

**Principais características:**
* **Abstração de Driver:** O desenvolvedor interage com uma interface comum, enquanto o driver cuida das especificidades do SGBD.
* **Desempenho:** Por ser uma interface de nível mais baixo, oferece excelente performance para operações em lote.
* **Compatibilidade:** Essencial para integrar sistemas Legados ou ambientes onde múltiplos SGBDs coexistem.

---

## 3. ORM (Object-Relational Mapping) em Python

O **ORM** é uma técnica que permite mapear objetos de uma linguagem de programação (como Python) para tabelas de um banco de dados relacional. Isso permite que o desenvolvedor manipule os dados utilizando a sintaxe da linguagem em vez de escrever SQL puro diretamente.

**Vantagens do ORM:**
* **Produtividade:** Reduz a quantidade de código repetitivo (*boilerplate*).
* **Segurança:** Protege naturalmente contra ataques de SQL Injection.
* **Manutenibilidade:** As alterações no esquema do banco são refletidas diretamente nas classes/modelos.

---

## 4. Framework Utilizado: Django ORM

O framework escolhido para a implementação desta tarefa foi o **Django ORM**. Por ser um framework *batteries-included*, o Django oferece uma camada de abstração poderosa e integrada para o PostgreSQL.

**Por que o Django ORM?**
O Django ORM facilita a criação de consultas complexas através de métodos como `.filter()`, `.exclude()` e `.annotate()`. Além disso, o sistema de **Migrations** automatiza a evolução do banco de dados, garantindo que a estrutura das tabelas esteja sempre em sincronia com o código Python.
