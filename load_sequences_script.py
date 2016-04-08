
# Preparation [Done]
#1 Set all actions on table 'actions'
#    'SELECT DISTINCT action FROM all_students_users_log_course266'
#2 Set all modules on table 'modules'
#    'SELECT DISTINCT module FROM all_students_users_log_course266'

#========== Main routine ==============

#1 Get all students from log (unique) [Done]

#2 Get a student A [Done]

#2.1 Get all the events from student A [Done]

#2.2 Group the events by day [Done]

#2.2.1 Set a sequence for group E_A

#2.2.2 Get an event group E_A

#2.2.3 Set the events of E_A on the table event


#Libraries
import psycopg2
from datetime import date
import time


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
std = 0 #Students counter
sqc = 0 #Sequences counter
for student in all_students:
    std+=1
    print "\nStep 2: Student - "+str(student[0])+" - Order: "+str(std)+"/"+str(len(all_students))+"."

    #2.1 Get this student events
    print "Step 2.1 - Getting events from student "+str(student[0])+"..."
    cur_old.execute("""SELECT * FROM all_students_users_log_course266 WHERE userid=%s ORDER BY time""", (student[0],))
    this_student_events = cur_old.fetchall()
    print str(student[0])+" has "+str(len(this_student_events))+" log events."

    #2.2 Group the events of this student by days
    print "Step 2.2 - Grouping "+str(student[0])+" events by day cicles (sequences)..."
    #Each cicle will be a sequence row...
    sequences_dic = {}
    for event in this_student_events:
        sequences_dic.setdefault(date.fromtimestamp(event[1]).toordinal(), []).append(event)
    #Builds an array of sequences properly grouped
    sequences_a = [sequences_dic.get(sequence, []) for sequence in range(min(sequences_dic), max(sequences_dic)+1)]
    print str(student[0])+" has "+str(len(sequences_a))+" event sequences."
    print sequences_a
    break

    #2.2.1 Building sequences individualy
    '''
        sequence = [  (3939624L, 1368137089L, 4013L, 266L, 'course', 'view', 5L),
            (3939610L, 1368137062L, 4013L, 266L, 'forum', 'view forum', 5L), ... ]
    '''
    for sequence in sequences:
        sqc+=1
        if len(sequence):
            sequence_start = sequence[0][1]
            sequence_end = sequence[-1][1]
        #cur_new.execute("INSERT INTO sequences")
