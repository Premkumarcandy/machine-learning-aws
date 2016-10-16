import sys

try: 
	predicted_filename = sys.argv[1]
except: 
	print "Give filename for predicted results. \nEx: python compare_results.py predicted.csv"
	sys.exit(0)


antall_like = 0; 
antall_ulike = 0; 

with open('true-results.csv') as resultfile, open(predicted_filename) as predictedfile: 

	for true_result, predicted in zip(resultfile, predictedfile): 


		predicted.split(",")

   		if true_result.strip() == predicted.strip()[0]: 
   			antall_like+=1
    	else:
    		antall_ulike+=1

print ("Antall korrekte: %i\nAntall feil: %i" %(antall_like, antall_ulike))
