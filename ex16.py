
from sys import argv

script, filename = argv
Prompt = "\n>"

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")

with open(filename,'r+') as target:
	print "Opening the file..."
	
	str = target.read()
	print "here is the file:"
	print str
	print Prompt
	lineout = raw_input("what is the last line you want to keep? %s" % Prompt) 
	target.seek(0)
	
	line = target.readline()
	print "Read Line: %s" % line
	isline = (lineout + '\n') != line
	while isline:
		line = target.readline()
		print "Read Line: %s" % line
		isline = (lineout + '\n') != line
	
	print "Now truncate remaining file."
	print "Truncating the file.  Goodbye!"
	target.truncate()
	
	print "Now I'm going to ask you for three lines."

	line1 = raw_input("line 1: ")
	line2 = raw_input("line 2: ")
	line3 = raw_input("line 3: ")

	print "I'm going to write these to the file."

	target.write(line1)
	target.write("\n")
	target.write(line2)
	target.write("\n")
	target.write(line3)
	target.write("\n")
		
	target.close()
	
with open(filename,) as target:	
	print "here is the new contents of %s" % filename
	print target.read()




#
#toread = raw_input("Do you want to read it? y/n %s" % Prompt)
#if "y" in toread:
#	print datas