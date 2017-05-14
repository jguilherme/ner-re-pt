import sys

if len(sys.argv) > 4:
	level = sys.argv[1]
	repeat = sys.argv[2]
	classifier = sys.argv[3]
	param = sys.argv[4]
	values = sys.argv[5:]
else:
	print "Usage: " + sys.argv[0] + " <level> <repeat> <param> <values>+\n"
	sys.exit()

for v in values:
	one = open('repeat-'+repeat+'/ner-results/experiences/'+param+'/'+v+'/out-'+level+'-'+classifier+'.txt','r').read().splitlines()
	two = open('repeat-'+repeat+'/ner-results/experiences/'+param+'/'+v+'/out-'+level+'-gold.txt','r').read().splitlines()

	i = 0
	for i,line in enumerate(one):
		if not line.split()[0] == two[i].split()[0]:
			print "ERROR: " + line.split()[0] + " vs. " + two[i].split()[0] + " | line: " + str(i)
			print "Value: " + v + " | Level: " + level
			break
		i += 1
