--- LISTAR TURMAS E ATIVIDADES
---  activity |  courseid

SELECT count(mdlacademico_log.id) AS activity, mdlacademico_log.course
INTO a_courses_activity
FROM mdlacademico_log
INNER JOIN mdlacademico_role_assignments m_role_a ON m_role_a.userid = mdlacademico_log.userid
INNER JOIN mdlacademico_context context ON context.id = m_role_a.contextid
WHERE m_role_a.roleid = 5
    AND m_role_a.contextid IN
        (SELECT id
         FROM mdlacademico_context context
         WHERE context.instanceid = mdlacademico_log.course)
GROUP BY mdlacademico_log.course
ORDER BY activity DESC;


--- SELECIONAR TURMAS PELA MEDIA DE ATIVIDADE MINIMA
---- course_id | activity | course_fullname

SELECT course, activity, courses.fullname
INTO a_selected_courses
FROM a_courses_activity
INNER JOIN mdlacademico_course courses ON courses.id = a_courses_activity.course
WHERE activity >= 44955; --- Activity Average


--- SELECIONAR O LOG DOS ESTUDANTES DAS TURMAS SELECIONADAS

SELECT m_log.id AS log_id,
       m_log.time,
       m_log.userid,
       m_log.course,
       m_log.module,
       m_log.action,
       m_role_a.roleid
INTO a_selected_log
FROM mdlacademico_log m_log
INNER JOIN mdlacademico_role_assignments m_role_a ON m_role_a.userid = m_log.userid
WHERE m_log.course IN (SELECT course FROM a_selected_courses)
    AND -- Turma com o mais númeor de estudantes
m_role_a.roleid = 5
    AND -- Role = 5 Estudante
m_role_a.contextid IN
        (SELECT id
         FROM mdlacademico_context context
         WHERE context.instanceid = m_log.course)
ORDER BY m_log.userid,
         m_log.time;
