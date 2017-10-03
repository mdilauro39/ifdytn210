palabra = str(raw_input("escriba una palabra"))

def vocal(letra):
	vocales = ["A","a","E","e","I","i","O","o","U","u"]
	for k in letra:
		#print "k: " + str(k)
		for v in vocales:
			if k == v:
				print " %s es vocal" % (k) 
print vocal(palabra)
