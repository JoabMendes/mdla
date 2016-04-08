
import time

print "Teste orders"

print "test sequences:"
sequences = [ time.ctime(1368136883), time.ctime(1368214777) , time.ctime(1368747495), time.ctime(1368830501) ]

for sequence in sequences:
    print sequence


print "\nteste events"
events  = [time.ctime(1368214777), time.ctime(1368214803), time.ctime(1368214815), time.ctime(1368214826)]

for event in events:
    print event
