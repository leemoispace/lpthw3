# Exercise 28: Boolean Practice

print "01. This is true:", True and True
print "02. This is false:", False and True
print "03. This is false:", 1 == 1 and 2 == 1
print "04. This is true:", "test" == "test"
print "05. This is true:", 1 == 1 or 2 != 1
print "06. This is true:", True and 1 == 1
print "07. This is false:", False and 0 != 0
print "08. This is true:", True or 1 == 1
print "09. This is true:", "test" != "testing"
print "10. This is false:", 1 != 0 and 2 == 1
print "11. This is true:", "test" != "testing"
print "12. This is false:", "test" == 1
print "13. This is true:", not(True and False)
print "14. This is false:", not(1 == 1 and 0 != 1)
print "15. This is false:", not(10 == 1 or 1000 == 1000)
print "16. This is false:", not(1 != 10 or 3 == 4)
print "17. This is true:", not("testing" == "testing" and 
	"Zed" == "Cool Guy")
print "18. This is true:", 1 == 1 and not("testing" == 1 or 1 == 0)
print "19. This is false:", "chunky" == "bacon" and not(3 == 4 or 3 == 3)
print "20. This is false:", 3 == 3 and not("testing" == "testing" or "Python" == "Fun") # made mistake: mentally evalusted as True