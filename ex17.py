
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
with open(from_file) as in_file:
	indata = in_file.read()

print "Does the output file exist? %r" % exists(to_file)
if exists(to_file):
	print "Ready, hit RETURN to overwrite, CTRL-C to abort."
	raw_input()

with open(to_file, 'w') as out_file:
	out_file.write(indata)


with open(to_file) as target:
	str = target.read()
	print "this is the new file contents:"
	print str
	
with open(from_file) as target:
	str = target.read()
	print "> \ndoes it match the old file contents?: \n>"
	print str