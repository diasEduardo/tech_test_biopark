# Desafio Tech - trainee Biopark 2021

### Objetivo
Desenvolver uma Aplicação para o agendamento de comunicações.

A aplicação deve permitir:
- Inserção de um novo agendamento
- Visualização dos agendamentos existentes
- Remoção de um agendamento


### Desenvolvimento
- Linguagem 
  - Python
- Banco de dados 
  - PostgreSQL
- Testes unitarios
  - \_\_
- Estrutura de comunicação
  - RESTful API

###### Suposições
1. Os dados de contato, tipo e status são gerenciados esternamente a essa funcionalidade.
2. A mensagem é salva como texto
3. Por questóes de simplicidade os numeros aceitos consideram apenas o padrão de celular no brasil

Com base nisso foi desenvolvido o esquema para o banco de dados, que pode sem encontrado na pasta 
[documentation](/documentation).
![database scheme](https://raw.githubusercontent.com/diasEduardo/tech_test_biopark/main/documentation/Database/db_scheme.png)


# Funcionamento

A aplicação se encontra hospedada em [ainda_nao_tem_site.com](/), ela conta com uma interface na forma de API assim como na forma de um site. Quanto ao site ele apresenta uma interface grafica simples para melhor demonstrar o uso da API.


### API

As **consultas** podem ser visualizadas através do verbo GET

	GET /api/agendamentos

caso se queria buscar por apenas uma consulta pode-se fazer a especificação

	GET /api/agendamentos/<id> 
<hr/>

Para **realizar agendamentos** deve-se passar todos os dados pertinentes, sendo eles
- type_id
  - numerico, id do tipo de dado 
- receiver_id
  - numerico, id do destinario
- date_time
  - timestamp, no formato 'YYYY-MM-DD HH:mm:ss'
- message
  - texto, mensagem a ser enviada

Utilizando o verbo POST

	POST /api/agendamentos?type_id=1&receiver_id=1&date_time=2020-12-21 11:00:00&message=mensagem

<hr/>

Para a **deleção** se utiliza o verbo DELETE 

	DELETE /api/agendamentos/<id>