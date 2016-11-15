class FloatRange:
	def __init__(self,start,end,step=0.1):
		self.start = start
		self.end = end
		self.step = step 
		
	def __iter__(self):
		t = self.start
		while t < self.end:
			yield t
			t += self.step
		
	def __reversed__(self):
		t = self.end
		while t > self.start:
			yield t
			t -= self.step
	
print "normal output: "	
for x in FloatRange(10,13,0.5):
	print x
	
print '-' *20	
print "reversed output: "
for x in reversed(FloatRange(10,13,0.5)):
	print x