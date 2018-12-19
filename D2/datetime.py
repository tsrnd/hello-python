import time; 
# print (time.localtime(time.time()))
localtime = time.asctime( time.localtime(time.time()) )
time = time.localtime(time.time())
print (time)
print ("time: ", localtime)