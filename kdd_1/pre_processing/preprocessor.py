
# Preparation [Done]
#1 Set all actions on table 'actions'
#    'SELECT DISTINCT action FROM a_selected_log'
#2 Set all modules on table 'modules'
#    'SELECT DISTINCT module FROM a_selected_log'

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
from datetime import date, datetime, timedelta
import time


#Helper functions

def getNextDay(last_day):
    last_day = datetime.utcfromtimestamp(last_day)
    tomorrow = last_day + timedelta(days=1)
    tomorrow_start = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 0, 0)
    tomorrow_end = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 23, 59, 0, 0)
    return [int(tomorrow_start.strftime("%s")), int(tomorrow_end.strftime("%s"))]

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
cur_old.execute("""SELECT DISTINCT action FROM a_selected_log""")
action_rows = cur_old.fetchall()

for row in action_rows:
    cur_new.execute("""INSERT INTO actions(label) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM actions WHERE label=%s)""", (row[0], row[0]))

conn_new.commit()
print "Actions were inserted.\n"

#Set all modules to table modules
cur_old.execute("""SELECT DISTINCT module FROM a_selected_log""")
module_rows = cur_old.fetchall()


for row in module_rows:
    cur_new.execute("""INSERT INTO modules(label) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM modules WHERE label=%s)""", (row[0], row[0]))
conn_new.commit()
print "Modules were inserted.\n"

print " ========= Preparation done ========== "
print " ========= Starting Routine ========== "

#Get all students from log
print "Step 1 - Getting all students..."
cur_old.execute("""SELECT DISTINCT userid FROM a_selected_log ORDER BY userid""")
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
    cur_old.execute("""SELECT * FROM a_selected_log WHERE userid=%s ORDER BY time""", [student[0]])
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

    #2.2.1 Building sequences individualy
    last_sequence = None
    for sequence in sequences_a:
        sqc+=1
        sequence_id = None
        sequence_start = None
        sequence_end = None
        duration = None
        if len(sequence):
            #No idle sequence
            sequence_start = sequence[0][1]
            sequence_end = sequence[-1][1]
            duration = sequence_end - sequence_start if sequence_end - sequence_start else 1
            last_sequence = sequence

        else:
            #idle squence
            #Get the next day of the last sequence
            this_day = getNextDay(last_sequence[0][1])
            sequence_start = this_day[0] #Default: this day at 00:00
            sequence_end = this_day[1] #Default: this day at 23:59
            #To avoid the last sequence to be empty
            last_sequence = [["start", sequence_start], ["end", sequence_end], "idle" ]
            duration = 86400 #Seconds of a day

        cur_new.execute("""INSERT INTO sequences(student, sequence_start, sequence_end, duration) VALUES (%s, %s, %s, %s) RETURNING sequence_id""", (student[0], sequence_start, sequence_end, duration))

        #The id of the sequence inserted
        sequence_id = cur_new.fetchone()[0]

        #Insert all events of this sequence
        if len(sequence):
            for event in sequence:
                    course = event[3]
                #2.2.2 Get an event group E_A
                    #Get this action id
                    action_label = event[5]
                    cur_new.execute("""SELECT action_id FROM actions WHERE label=%s""", [action_label])
                    action_id = cur_new.fetchone()[0]
                    #Get this module id
                    module_label = event[4]
                    cur_new.execute("""SELECT module_id FROM modules WHERE label=%s""", [module_label])
                    module_id = cur_new.fetchone()[0]
                    cur_new.execute("""INSERT INTO event(sequence_id, action_id, module_id, course) VALUES (%s, %s, %s, %s)""", (sequence_id, action_id, module_id, course))
        else:
            cur_new.execute("""INSERT INTO event(sequence_id) VALUES (%s)""", [sequence_id])

        #2.2.3 Set the events of E_A on the table event
        conn_new.commit()
    print "Sequences were inserted.\n"
