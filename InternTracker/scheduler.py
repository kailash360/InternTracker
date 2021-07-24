import schedule
import time
import os
import threading
import sys
from Routes.internships import app

# Gets the number of cores present in system
cpus = os.cpu_count()

def run() :

    path = os.path.dirname(os.path.abspath(__file__))
    # Runs program based on host os
    if (os.name == "nt") :
        os.system("python ./new_main.py")
    else :
        os.system(f"python3 {path}/new_main.py") 

# Runs the internship API endpoint
def internships_api() :

    print(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.dirname(os.path.abspath(__file__))
    if (os.name == "nt") :
        # os.system("python ./Routes/internships.py")
        pass
    else :
        # os.system(f"""python3 {path}/Routes/internships.py""") 
        app.run(debug=True)

def auth_api() :

    path = os.path.dirname(os.path.abspath(__file__))
    if (os.name == "nt") :
        # os.system("python ./Routes/auth.py")
        pass
    else :
        # os.system(f"python3 {path}/Routes/auth.py")
        pass

# Scheduler has been set to run everyday at 0000 hrs
schedule.every().day.do(run)

thread1 = threading.Thread(target = app.run)
thread1.start()
thread2 = threading.Thread(target = auth_api)
thread2.start()

while True :

    schedule.run_pending()
    time.sleep(1)