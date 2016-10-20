# Fase de seleção dos dados

Esta fase é responsável pela seleção dos dados a serem usados na mineração e foi executada e duas etapas: estudo
do banco de dados e a seleção dos informações a serem mineradas.

## Etapa 1: Estudo do banco de dados

Estudando o banco de dados do Moodle é possível identificar que o registro das ações dos usuários
são armazenados conforme eles interagem com o sistema. Uma tabela de log (`mdlacademico_log`) faz o
armazenamento dessas ações. Salvando o id do usuário,o timestamp da ação, o contexto da ação, o curso,
a ação executada e o módulo acessado.

Os principais campos da tabela `mdlacademico_log` são:

- **log_id:** atributo identificador da instância de log.
- **time:** momento em que foi registrado a instância de log. (Data, Dia, hora e minuto)
- **userid:** identificador do usuário que executou a ação.
- **course:** identificador da disciplina/turma onde a ação foi executada.
- **action:** descrição textual da ação executada pelo usuário.
- **module:** descrição textual do módulo onde a ação foi executada.

A tabela possui outros 4 campos (ip, cmid,url,info) que foram desconsiderados por não terem
relevância no estudo do comportamento dos usuários.

Com a compreensão desses dados foi possível definir um critério de seleção de dados. Sendo
este a seleção das turmas de educação a distância que possuíssem uma participação relativa no sistema.
Este critério permite que várias turmas possam ser estudadas fornecendo a possibilidade de uma
variedade maior de comportamentos, além de permitir uma coleta de dados bastante densa. Permitindo uma maior
precisão em um processo de descoberta de conhecimento em banco dados.

# Etapa 2: Selecionando os dados

A escolha das turmas se deu pela sua participação no uso do sistema, após descobrir a turma
mais ativa no sistema, ou seja, a turma que possui mais intâncias de ações executadas pelos estudantes.
Foi definido um número que representa a média de uso do sistema. Esse número foi definido como sendo a
metade do valor total de instâncias de log da turma com o maior uso do sistema.

A média de uso do sistema pelos estudantes é de exatamente `44.955` interações. Com isso, as turmas
que possuem o número de interações maior ou igual a esse valor foram escolhidas.
Os scripts SQL de seleção estão no anexo `00_select_courses.sql`. Onde a contagem das atividades de cada
turma foram armazenadas na tabela `a_courses_activity`, a seleção das turmas com o uso médio na tabela
`a_selected_courses` e o log das turmas selecionadas em `a_selected_log`.

Ao todo, `42` turmas forma selecionadas, fornecendo um número de `2.826.630` intâncias
de log a serem mineradas.
