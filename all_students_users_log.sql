SELECT m_log.id AS log_id,
       m_log.time,
       m_log.userid,
       m_log.course,
       m_log.module,
       m_log.action,
       m_role_a.roleid INTO all_students_users_log_course266
FROM mdlacademico_log m_log
INNER JOIN mdlacademico_role_assignments m_role_a ON m_role_a.userid = m_log.userid -- INNER JOIN mdlacademico_user u on u.id = m_log.userid

WHERE m_log.course = 266
    AND -- Turma com o mais númeor de estudantes
m_role_a.roleid = 5
    AND -- Role = 5 Estudante
m_role_a.contextid IN
        (SELECT id
         FROM mdlacademico_context context
         WHERE context.instanceid = m_log.course)
ORDER BY m_log.userid,
         m_log.time -- SELECT DA TURMA COM O MAIOR NUMERO DE ESTUDANTES

SELECT count(DISTINCT(ra.userid)) AS estudantes,
       c.instanceid AS courseid,
       course.fullname,
       course.shortname,
       course.showgrades INTO all_courses_students_count
FROM mdlacademico_role_assignments ra
INNER JOIN mdlacademico_context c ON c.id = ra.contextid
INNER JOIN mdlacademico_course course ON course.id = c.instanceid
WHERE ra.roleid=5
    AND c.contextlevel=50
GROUP BY ra.contextid,
         c.id,
         c.instanceid,
         course.id
ORDER BY estudantes DESC -- Novas açoes

SELECT DISTINCT action
FROM all_students_users_log_course266
WHERE action NOT IN
        (SELECT DISTINCT action
         FROM all_students_users_log_course88)

-- esdrascaleb@gmail.com
