
'''
Transform sequential data to csv for SPAM algorithm input

ID ... ACTION MODULE -1 ... -2

'''


# Libraries
import psycopg2


# Connect with mdla sequential
try:
    conn_new = psycopg2.connect(
        "dbname='mdla_sequential' user='postgres' host='localhost' password='admin123'")
except:
    print "I am unable to connect to the database"

if conn_new.status:
    print "Connected with mdla_sequential"


cur_new = conn_new.cursor()

f = open('dictionary.json', 'w+')

# Get students
cur_new.execute("""SELECT DISTINCT student FROM sequences""")
students = cur_new.fetchall()

stdsc = len(students)
c = 1
dictionary = {}
for std in students:
    std_sqc_str = str(std[0])+" "
    # Get sequences of this student
    cur_new.execute(
        """SELECT sequence_id FROM sequences WHERE student=%s""", [std[0]])
    sequences = cur_new.fetchall()
    for sqc in sequences:
        # Get the events of the sequences of this student
        cur_new.execute(
            """SELECT action_id, module_id FROM event WHERE sequence_id=%s""", [sqc[0]])
        events = cur_new.fetchall()
        for evt in events:
            if str(evt[0]) == "None" or str(evt[1]) == "None":
                if "0" not in dictionary:
                    dictionary["0"] = "idle"
            else:
                evtid = str(evt[0]) + "" + str(evt[1])
                if evtid not in dictionary:
                    cur_new.execute("""SELECT label FROM actions WHERE action_id=%s""", [evt[0]])
                    action_label = cur_new.fetchall()
                    aclab = action_label[0]
                    cur_new.execute("""SELECT label FROM modules WHERE module_id=%s""", [evt[1]])
                    module_label = cur_new.fetchall()
                    molab = module_label[0]
                    dictionary[evtid] = str(aclab[0]) + ":" + str(molab[0])

    print "Done with student: " + str(std[0]) + " (" + str(c) + "/" + str(stdsc) + ")"
    c += 1

f.write(str(dictionary) + "\n")
f.close()
