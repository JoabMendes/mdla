#Fase de seleção dos dados


Nessa fase foram selecionados os dados a serem analisados. Esses dados são a instâncias
de registro de ações executadas no sistema, armazenados na tabela `mdlacademico_log`.
Os dados dessa tabela são armazenados de forma sequêncial ordenados pelo momento (Data, dia, hora e minuto)
em que as ações forma executadas pelos usuários.

Os principais campos da tabela `mdlacademico_log` são:

- **log_id:** atributo identificador da instância de log.
- **time:** momento em que foi registrado a instância de log. (Data, Dia, hora e minuto)
- **userid:** identificador do usuário que executou a ação.
- **course:** identificador da disciplina/turma onde a ação foi executada.
- **action:** descrição textual da ação executada pelo usuário.
- **module:** descrição textual do módulo onde a ação foi executada.

A tabela possui outros 4 campos (ip, cmid,url,info) que foram desconsiderados por não terem
relevância no estudo do comportamento dos usuários.

A escolha das turmas se deu pela sua participação no uso do sistema, após descobrir a turma
mais ativa no sistema, ou seja, a turma que possui mais intâncias de ações executadas pelos estudantes.
Foi definido um número que representa a média de uso do sistema. Esse número foi definido como sendo a
metade do valor total de instâncias de log da turma com o maior uso do sistema.

A média de uso do sistema pelos estudantes é de exatamente `44955` interações. Com isso, as turmas
que possuem o número de interações maior ou igual a esse valor foram escolhidas.
Os scripts SQL de seleção estão no anexo `00_select_courses.sql`. Onde a contagem das atividades de cada
turma foram armazenadas na tabela `a_courses_activity`, a seleção das turmas com o uso médio na tabela
`a_selected_courses` e o log das turmas selecionadas em `a_selected_log`.

Ao todo, `42` turmas forma selecionadas, fornecendo um número de `2826630` intâncias
de log a serem mineradas.
