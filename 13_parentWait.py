"""Call a child python script from parent. 
Parent scripts to wait for output from child 
script to move ahead
execute the next instructions"""
import subprocess
import time 


# daata = exec(open('Child.py').read())

# print("daata = %s" %daata)

# if daata == None:
#     print("success")
# else:
#     print("failed")


p = subprocess.run(['python', 'Child.py'], capture_output=True, text=True) #Call a child python script from parent
print("Return code is:", p.returncode)
print("Output of the clild python file execution is:", p.stdout)
# time.sleep(5)
# blocking process
# fork


if p.returncode >= 1:  # Parent scripts to wait for output from child script 
    pass
else: 
    time.sleep(5)

if p.returncode == 0:
    print("Next command execute successfully") # ahead execute the next instructions
else:
    print("Next command not executed because child python script is not executed successfully")    






