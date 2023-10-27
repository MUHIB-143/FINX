import os,platform
os.system('git pull')
 
arcv=platform.architecture()[0]
if arcv=="32bit":
    os.system('chmod 777 FINX32;./FINX32')
elif arcv=="64bit":
    os.system('chmod 777 FINX64;./FINX64')
