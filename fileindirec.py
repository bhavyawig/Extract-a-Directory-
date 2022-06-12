import os

totalbite = 0

direc = os.listdir() # to get the current directory 

for i in direc:
       if os.path.isfile(i): # to check it is a file and not directory 
              size=os.path.getsize(i)     # get size of the file 
              totalbite=totalbite+size         # add size to total size


os.mkdir("answer12") # make answer12 directory 
myfile = open("answer12/results.txt","w+") # make a txt file inside the directory, open it in write mode
if myfile.mode == "w+": # check that the file is opened in write mode 
       for i in direc: 
            myfile.write(i+" has size " + str(os.path.getsize(i))+"\n") # iterate the list to add filename and size in txt file 

       myfile.write("TOTAL SIZE IS : " + str(totalbite))     # add total size at the end of txt file 


myfile.close() # close the txt file 



