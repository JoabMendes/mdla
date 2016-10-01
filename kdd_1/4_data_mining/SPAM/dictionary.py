
'''
Transform sequential data to json to build a dictionary for humanize script.

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

c = 1
dictionary = {}

cur_new.execute("""SELECT event.action_id, event.module_id, event.sequence_id, actions.label, modules.label  FROM event
                        JOIN actions ON actions.action_id = event.action_id
                        JOIN modules ON modules.module_id = event.module_id""")
events = cur_new.fetchall()

count = 0
for event in events:
    if str(event[0]) == "None" or str(event[1]) == "None":
        if "0" not in dictionary:
            dictionary["0"] = "idle"
    else:
        eventid = str(event[0]) + str(event[1])
        if eventid not in dictionary:
            dictionary[eventid] = str(event[3]) + ":" + str(event[4])
    count += 1
    print "Event " + str(count) + "/"+ str(len(events))


f.write(str(dictionary) + "\n")
f.close()
