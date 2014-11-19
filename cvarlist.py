#!/usr/bin/env python
import re
# condump_stripcolors 1
# log_file cvarlist
# cvarlist
# log_file ""
# condump_stripcolors 0
with open('cvarlist.log', 'r') as f:
	l = 1
	for line in f.readlines():
		l += 1
		if not ' is ' in line:
			continue
		parts = line.split(' is ', maxsplit=1)
		var = re.sub('\^[0-9]', '', parts[0])
		rest = parts[1]
		tokens = rest.split('"')
		if len(tokens) > 3:
			current = tokens[1]
			default = tokens[3]
			if default != current:
			#print(var + ' "' + default + '"')
				print(var + ' "' + current + '"')
		else:
			print(str(l) + ":" + str(tokens))
		
