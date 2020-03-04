from datetime import datetime
class AgeCalculator():
	"""docstring for AgeCalculator"""
	
	def __init__(self,YYYY,MM,DD):
		super(AgeCalculator, self).__init__()
		#self.name = name
		self.year=YYYY
		self.month=MM
		self.day=DD
	def printAGE(self):
		#a=datetime.now().date()
		a=str(datetime.now().date())
		b=a.split("-")
		year=int(b[0])-int(self.year)-1
		month=int(b[1])-int(self.month)
		day=int(b[2])-int(self.day)
		hour=str(datetime.now().time())
		hour1=hour.split(":")

		print("\nAge is ",year)
		print("\nFor Next Birthday")
		print("Month remaining :",abs(month))
		print("Day remaining :",abs(day))
		print("Hour remaining :",23-abs(int(hour1[0])))
		print("Minutes remaining :",60-abs(int(hour1[1])))
		#print(hour1[2])
		Seconds1=float(hour1[2])
		Seconds2=int(Seconds1)
		print("Seconds remaining :",60-Seconds2)
#name=input("\nEnter Your Name :")
dob=input("Enter your Age in YYYY MM DD format Ex. 2001 05 16 :\n")
date=dob.split()
YYYY=date[0]
MM=date[1]
DD=date[2]
a=AgeCalculator(YYYY,MM,DD)
a.printAGE()

		
