import os,platform
os.system('git pull')
 
acvh=platform.architecture()[0]
if acvh=="32bit":
    os.system('chmod 777 FINX32;./FINX32')
elif acvh=="64bit":
    os.system('chmod 777 FINX64;./FINX64')
