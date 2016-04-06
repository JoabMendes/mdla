
'''

Preparation

1 Set all actions on table 'actions'
    'SELECT DISTINCT action FROM all_students_users_log_course266'

2 Set all modules on table 'modules'
    'SELECT DISTINCT module FROM all_students_users_log_course266'

Main routine

1 Get all students from log (unique)

2 Get a student A

3 Get all the events from student A

4 Group the events by day

5 Get an event group E_A

6 Set a sequence for group E_A

7 Set the events of E_A on the table event

'''

#Libraries
import psycopg2


#Preparation

print " ======= Starting Preparation ======= "

#Connect with mdlacdemico
try:
    conn_old = psycopg2.connect("dbname='mdlacademico' user='postgres' host='localhost' password='admin123'")
except:
    print "I am unable to connect to the database"

if conn_old.status:
    print "Connected with mdlacademico"

#Connect with mdla sequential
try:
    conn_new = psycopg2.connect("dbname='mdla_sequential' user='postgres' host='localhost' password='admin123'")
except:
    print "I am unable to connect to the database"

if conn_new.status:
    print "Connected with mdla_sequential"

#Cursor objects
cur_old = conn_old.cursor()
cur_new = conn_new.cursor()

#Set all actions to table actions
cur_old.execute("""SELECT DISTINCT action FROM all_students_users_log_course266""")
action_rows = cur_old.fetchall()

for row in action_rows:
    cur_new.execute("""INSERT INTO  actions(label) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM actions WHERE label = %s)""", (row[0], row[0]))
print "Actions were inserted.\n"

#Set all modules to table modules
cur_old.execute("""SELECT DISTINCT module FROM all_students_users_log_course266""")
module_rows = cur_old.fetchall()

for row in module_rows:
    cur_new.execute("""INSERT INTO  modules(label) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM modules WHERE label = %s)""", (row[0], row[0]))
print "Modules were inserted.\n"

print " ========= Preparation done ========== "
