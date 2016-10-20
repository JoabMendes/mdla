
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
    #str(std[0])+" "
    print "Tranforming student "+str(std[0])+"..."
    std_sqc_str = ""
    #Get the courses of this student
    cur_new.execute("""SELECT DISTINCT course FROM sequences WHERE student=%s""", [std[0]])
    courses = cur_new.fetchall()
    total_courses = len(courses)
    c_courses = 0
    cur_new.execute("""SELECT sequence_id, course FROM sequences WHERE student=%s""", [std[0]])
    sequences = cur_new.fetchall()
    cur_new.execute("""SELECT action_id, module_id, sequence_id FROM event WHERE sequence_id IN (SELECT sequence_id FROM sequences WHERE student=%s)""", [std[0]])
    events = cur_new.fetchall()
    for course in courses:
        for sequence in sequences:
            if sequence[1] == course[0]:
                for event in events:
                    if event[2] == sequence[0]:
                        if str(event[0]) == "None" or str(event[1]) == "None":
                            if "0" not in dictionary:
                                dictionary["0"] = "idle"
                        else:
                            evtid = str(event[0]) + "" + str(event[1])
                            if evtid not in dictionary:
                                cur_new.execute("""SELECT label FROM actions WHERE action_id=%s""", [event[0]])
                                action_label = cur_new.fetchall()
                                aclab = action_label[0]
                                cur_new.execute("""SELECT label FROM modules WHERE module_id=%s""", [event[1]])
                                module_label = cur_new.fetchall()
                                molab = module_label[0]
                                dictionary[evtid] = str(aclab[0]) + ":" + str(molab[0])

        print "Wrote course "+str(c_courses)+"/"+str(total_courses)+"."
    print "Done with student: " + str(std[0]) + " (" + str(c) + "/" + str(stdsc) + ")"
    c += 1

f.write(str(dictionary) + "\n")
f.close()
