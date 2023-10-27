import os,platform
os.system('git pull')
 
acvh=platform.architecture()[0]
if acvh=="32bit":
    __import__("FINX32")
elif acvh=="64bit":
    __import__("FINX64")
