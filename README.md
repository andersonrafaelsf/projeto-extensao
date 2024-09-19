# Sistema de Agendamento para Massoterapeuta 

## Descrição
Este sistema foi desenvolvido para facilitar o gerenciamento de clientes e agendamentos para uma massoterapeuta autônoma. Ele permite o cadastro de clientes, o agendamento de horários e a visualização dos compromissos futuros.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Banco de Dados:** SQLite
- **Bibliotecas:** sqlite3, datetime

## Modelo do Banco de Dados
O banco de dados utilizado é o SQLite e possui uma única tabela para armazenar os agendamentos:

### Tabela: `agendamentos`
| Coluna        | Tipo      | Descrição                                 |
|---------------|-----------|-------------------------------------------|
| `id`          | INTEGER   | Chave primária autoincrementada            |
| `nome`        | TEXT      | Nome do cliente                           |
| `telefone`    | TEXT      | Telefone de contato do cliente             |
| `data_hora`   | TEXT      | Data e hora do agendamento                 |
| `servico`     | TEXT      | Descrição do serviço agendado              |

## Funcionalidades
- Cadastro de clientes (nome, telefone).
- Agendamento de horários.
- Visualização dos agendamentos futuros.

## Como Usar
1. Clone este repositório para sua máquina:
   ```bash
   git clone https://github.com/seu-usuario/sistema-agendamento.git
