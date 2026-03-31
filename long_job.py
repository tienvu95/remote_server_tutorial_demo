import time
from datetime import datetime


for i in range(1, 7):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Step {i}/6: job is still running...")
    time.sleep(30)

print("Done. This demo job finished after about 3 minutes.")
