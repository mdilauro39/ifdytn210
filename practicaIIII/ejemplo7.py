def palindromo(a):
	pal = ""
	for i in a:
		pal = i+pal
	if pal == a:
		info = "Palindromo"
	else:
		info = "no Palindromo"
	return info

jerjes = "jerjrej"
print palindromo(jerjes)
