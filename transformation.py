
'''
Transform sequential data to csv for Apriori algorithm input
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

f = open('basket.txt', 'w+')

# Get students
cur_new.execute("""SELECT DISTINCT student FROM sequences""")
students = cur_new.fetchall()

stdsc = len(students)
c = 1
for std in students:
    std_sqc_str = ""
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
                evtstr = "0000,"
            else:
                evtstr = str(evt[0]) + "" + str(evt[1]) + ","
            std_sqc_str += evtstr
    f.write(std_sqc_str + "\n")
    print "Done with student: " + str(std[0]) + " (" + str(c) + "/" + str(stdsc) + ")"
    c += 1
f.close()
