# Exercise 44: Inheritance vs Composition
    # Composition

class Other(object):
    
    def implicit(self):
        print "Other implicit()"

    def override(self):
        print "Other override()"
        
    def altered(self):
        print "Other altered()"
        

class Child(object):
    
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print "Child override()"
        
    def altered(self):
        print "Child before Other altered()"
        self.other.altered()
        print "Child, after Other altered()"
        
son = Child()

son.implicit()
son.override()
son.altered()