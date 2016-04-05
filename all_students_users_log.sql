SELECT m_log.id as log_id, m_log.time, m_log.userid, m_log.course, m_log.module, m_log.action, m_role_a.roleid
INTO all_students_users_log_course266
FROM mdlacademico_log m_log
INNER JOIN mdlacademico_role_assignments m_role_a on m_role_a.userid = m_log.userid
-- INNER JOIN mdlacademico_user u on u.id = m_log.userid
WHERE
m_log.course = 266 and -- Turma 88 = Mesma que o trabalho de Thaísa
m_role_a.roleid = 5 and  -- Role = 5 Estudante
m_role_a.contextid in (SELECT id from mdlacademico_context context where context.instanceid = m_log.course)
ORDER BY m_log.userid, m_log.time



-- SELECT DA TURMA COM O MAIOR NUMERO DE ESTUDANTES
SELECT count(DISTINCT(ra.userid)) as estudantes, c.instanceid as courseid, course.fullname, course.shortname, course.showgrades
INTO all_courses_students_count
FROM mdlacademico_role_assignments ra
INNER JOIN mdlacademico_context c on  c.id = ra.contextid
INNER JOIN mdlacademico_course course on course.id = c.instanceid
WHERE ra.roleid=5 and c.contextlevel=50
GROUP BY ra.contextid,c.id,c.instanceid, course.id
ORDER BY estudantes DESC


-- Novas açoes
SELECT DISTINCT action FROM all_students_users_log_course266
WHERE action not in (SELECT DISTINCT action FROM all_students_users_log_course88)



esdrascaleb@gmail.com
