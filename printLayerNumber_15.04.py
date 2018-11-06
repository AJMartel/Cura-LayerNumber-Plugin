#Name: Print Layer Number
#Info: Prints layer number on LCD screen
#Depend: GCode
#Type: postprocess

with open(filename, "r") as f:
	lines = f.readlines()

with open(filename, "w") as f:
	for lIndex in xrange(len(lines)):
		line = lines[lIndex]
		
		if line.startswith(';Layer count:'):
			totLayers = int(line[13:].strip())
		
		if line.startswith(';LAYER:'):
			currentLayer = int(line[7:].strip())
			f.write(line)
			f.write('M117 Layer %d/%d\n' % (currentLayer + 1, totLayers))
			continue

		f.write(line)
