
'''

Preparation [Done]

1 Set all actions on table 'actions'
    'SELECT DISTINCT action FROM all_students_users_log_course266'

2 Set all modules on table 'modules'
    'SELECT DISTINCT module FROM all_students_users_log_course266'

Main routine

1 Get all students from log (unique)

2 Get a student A

2.1 Get all the events from student A

2.2 Group the events by day

2.3 Get an event group E_A

2.4 Set a sequence for group E_A

2.5 Set the events of E_A on the table event

3 Go back step 2 with student A+1

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
    cur_new.execute("""INSERT INTO actions(label) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM actions WHERE label=%s)""", (row[0], row[0]))

conn_new.commit()
print "Actions were inserted.\n"

#Set all modules to table modules
cur_old.execute("""SELECT DISTINCT module FROM all_students_users_log_course266""")
module_rows = cur_old.fetchall()


for row in module_rows:
    cur_new.execute("""INSERT INTO modules(label) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM modules WHERE label=%s)""", (row[0], row[0]))
conn_new.commit()
print "Modules were inserted.\n"

print " ========= Preparation done ========== "
print " ========= Starting Routine ========== "

#Get all students from log
print "Step 1 - Getting all students..."
cur_old.execute("""SELECT DISTINCT userid FROM all_students_users_log_course266 ORDER BY userid""")
all_students = cur_old.fetchall()
print str(len(all_students))+" students were found."

print "Building sequences..."
s = 1
for student in all_students:
    print "\nStep 2: Student - "+str(student[0])+" - Order: "+str(s)+"/"+str(len(all_students))"."

    print "Step 2.1 - Getting events from student "+str(student[0])+"..."
    cur_old.execute("""SELECT * FROM all_students_users_log_course266 WHERE userid=%s ORDER BY time DESC""", (student[0],))
    this_student_events = cur_old.fetchall()
    print str(student[0])+" has "+str(len(this_student_events))+" log events."

    print "Step 2.2 - Grouping "+str(student[0])+" events by day cicles..."
    #Each cicle will be a sequence row...
    
