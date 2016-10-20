#Fase de pré-processamento


Como os dados selecionados constituíam uma única tabela de registro de ações, o método
de pré-processamento escolhido foi a aplicação das regras de normalização de banco de dados
(William Kent, 1981). A aplicação das regras de normalização é capaz de reduzir problemas
de redundância de dados e inconsistências, propondo uma nova estrutura de armazenamento dos
dados. Essas regras forma aplicadas na tabela `a_selected_log` que possui os mesmos campos
descritos para a tabela `mdlacademico_log` na fase anterior. Seguindo o critério de manter
a natureza sequencial dos dados a estrutura proposta na normalização está representada
no seguinte diagrama entidade-relacional:

![DER](http://i.imgur.com/hO6vsEO.png)
Figura 2 - Diagrama ER das tabelas originadas após a normalização da tabela students_log_266 (2016). Fonte: Autoria própia.


A normalização dos dados seguindo essa abstração, permitiu definir as sequências como os conjuntos de eventos
executados por um usuário no ciclo de um dia. E os eventos como sendo um conjunto de ação e módulo acessado.

As informações dos campos action e module foram transferidas para tabelas de referência separadas.
No Moodle, o registro das ações e módulos eram gerados na aplicação, não existindo nenhuma referência
as instâncias das possíveis ações e módulos do sistema. As solução para normalização desses dados foi
selecionar todas as ações únicas e os módulos únicos existentes na tabela de log e definir as tabelas
modules e actions. Esse procedimento permitiu a referência as ações e módulos sem a redundância de dados
textuais.

Outro procedimento da normalização foi a definição das instâncias das sequências de ações dos usuários e dos
eventos dessas sequências. Cada instância de da tabela `sequences` representa o ciclo de um dia de atividades de um usuário
relativo a um curso. Nesta tabela são registrados os usuários (student) que executaram a sequência de eventos,
o começo da sequência como sendo o tempo do primeiro evento da sequência (sequence_start), o fim da sequência
como sendo o tempo do último evento da sequência (sequence_end) e a duração da sequência, sendo esta a subtração
do campo sequence_end pelo campo sequence_start. E por último o curso em que o usuário estudante executou a atividade.
A instâncias de log foram agrupadas por estudantes, em seguinda por cursos para cada estudantes e em seguinda em dias
de acordo com o campo `time`. A decisão de registrar as sequências em ciclos de eventos em um dia foi tomada por
possibilitar o registro dos dias em que um usuário foi ocioso no sistema. Em seguida foram definidas as instâncias de
eventos, que possuem uma referência a tabela sequences.

Uma instância de evento é composta por um atributo identificador, a referência do módulo executado pelo usuário e ação
executada sobre este módulo. Caso a sequência correspondesse a um dia ocioso do aluno, um evento era gerados para aquele
dia; começando as 00:00 e terminando as 23:59 e com os campos module e action como nulos. Preenchendo os dias ociosos entre
o começo e o fim da interação do usuário com o sistema.

Todos os procedimentos desta fase foram implementados na linguagem python, usando a biblioteca psycopg
para o acesso e manipulação do dados dados no SGBD PostgreSQL.
