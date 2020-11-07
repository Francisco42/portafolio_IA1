def parse_file(readFilename, writeFilename):
	headerRow = "id ccf age sex painloc painexer relrest pncaden cp trestbps htn chol smoke cigs years fbs dm famhist restecg ekgmo ekgday ekgyr dig prop nitr pro diuretic proto thaldur thaltime met thalach thalrest tpeakbps tpeakbpd dummy trestbpd exang xhypo oldpeak slope rldv5 rldv5e ca restckm exerckm restef restwm exeref exerwm thal thalsev thalpul earlobe cmo cday cyr num lmt ladprox laddist diag cxmain ramus om1 om2 rcaprox rcadist lvx1 lvx2 lvx3 lvx4 lvf cathef junk name\n"
	readfile = open(readFilename, 'r', errors='ignore')
	writefile = open(writeFilename, 'w')
	writefile.write(headerRow)
	writeRow = ""
	for row in readfile:
		writeRow += row 
		if ("name" in row):
			writefile.write(writeRow)
			writeRow = ""
		else:
			writeRow = writeRow.rstrip()
			writeRow += " "
	readfile.close()
	writefile.close()

parse_file("datasets/switzerland.data", "datasets/switzerland_parsed.data")