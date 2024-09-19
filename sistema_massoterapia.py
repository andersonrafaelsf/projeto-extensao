import sqlite3

# Função para criar o banco de dados e a tabela, se não existirem
def inicializar_banco_dados():
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um novo agendamento
def adicionar_agendamento():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")
    data = input("Data do agendamento (YYYY-MM-DD): ")
    horario = input("Horário do agendamento (HH:MM): ")

    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO agendamentos (nome, telefone, data, horario)
        VALUES (?, ?, ?, ?)
    ''', (nome, telefone, data, horario))
    conn.commit()
    conn.close()

    print("Agendamento adicionado com sucesso!")

# Função para visualizar todos os agendamentos
def visualizar_agendamentos():
    conn = sqlite3.connect('agendamentos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM agendamentos')
    agendamentos = cursor.fetchall()
    conn.close()

    if agendamentos:
        for agendamento in agendamentos:
            print(f"ID: {agendamento[0]}, Nome: {agendamento[1]}, Telefone: {agendamento[2]}, Data: {agendamento[3]}, Horário: {agendamento[4]}")
    else:
        print("Nenhum agendamento encontrado.")

# Função principal para exibir o menu e lidar com as opções
def main():
    inicializar_banco_dados()

    while True:
        print("\nMenu:")
        print("1. Adicionar agendamento")
        print("2. Visualizar agendamentos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_agendamento()
        elif escolha == '2':
            visualizar_agendamentos()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
