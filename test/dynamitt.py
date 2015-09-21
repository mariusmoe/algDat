import readline
import time

def main():
	try:
		f = open('input.txt', 'r')
		filen = f.readlines()

		li_=[line.rstrip() for line in filen]
		#print(li_) 	#debug


		#print(len(li_))	#debug
		bigest_number = li_[0]
	
		for number in li_:
			if int(bigest_number) < int(number):
				bigest_number = number
				

		print(bigest_number + " is teh biggest number :)")
 

	except:
		print("Shit happend")
		pass

	finally:
		f.close()

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))