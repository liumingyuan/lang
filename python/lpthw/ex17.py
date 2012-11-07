# -*- encoding:utf-8 -*-

from sys import argv
from os.path import exists

script, file_from, file_to = argv

print "Copying from %s to %s." %(file_from, file_to)

in_file = open(file_from)
in_data = in_file.read()

print "The file is %d bytes long." % len(in_data)

print "Does the output file exists? %r", exists(file_to)
print "Ready, hit RETURN to continue or CTRL-C to abort."
raw_input('?')

out_file = open(file_to, 'w')
out_file.write(in_data)

print "Done."
out_file.close()
in_file.close()

