
'''

Preparation

1 Set all actions on table 'actions'
    'SELECT DISTINCT action FROM all_students_users_log_course266'

2 Set all modules on table 'modules'
    'SELECT DISTINCT action FROM all_students_users_log_course266'

Main routine

1 Get all students from log (unique)

2 Get a student A

3 Get all the events from student A

4 Group the events by day

5 Get an event group E_A

6 Set a sequence for group E_A

7 Set the events of E_A on the table event

'''

#Preparation
import psycopg2

try:
    conn_old = psycopg2.connect("dbname='mdlacademico' user='postgres' host='localhost' password='admin123'")
except:
    print "I am unable to connect to the database"

if conn_old.status:
    print "Connected with mdlacademico"

try:
    conn_new = psycopg2.connect("dbname='mdla_sequential' user='postgres' host='localhost' password='admin123'")
except:
    print "I am unable to connect to the database"

if conn_new.status:
    print "Connected with mdla_sequential"
