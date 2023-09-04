# import datetime
# import time
# while True:
#     localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result)
#   time.sleep(1)
    
# 	x = datetime.datetime.now()
# 	second = x.strftime("%S")
# 	print(second[1])
#         time.sleep(1)



import time
import datetime
while True:
    x = datetime.datetime.now()
    second = x.strftime("%S")[1]
    print(second)
    time.sleep(1)
