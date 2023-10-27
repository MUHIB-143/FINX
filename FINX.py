import os,platform
os.system('git pull')
 
acvh=platform.architecture()[0]
if acvh=="32bit":
    os.system('chmod +x;./FINX32')
elif acvh=="64bit":
    os.system('chmod +x;./FINX32')
