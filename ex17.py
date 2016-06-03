from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long." % len(indata)

print "Dose the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()



#MBP-Ethan:TextWrangler xing$ python ex17.py FirstLesson.txt ex17sample.txt
#Copying from FirstLesson.txt to ex17sample.txt
#The input file is 54 bytes long.
#Dose the output file exist? False
#Ready, hit RETURN to continue, CTRL-C to abort.

#Alright, all done.
