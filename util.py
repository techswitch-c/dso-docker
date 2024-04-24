#!/usr/bin/env python3
import shutil
# import psutil

def check_disk(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free


# def check_cpu():
#     usage = psutil.cpu_percent(1)
#     return usage


# if not check_disk("/") or not check_cpu():
if not check_disk("/"):
    print("ERROR!")
else:
    print("Everything is OK!")

# print(check_cpu())
print(check_disk(disk="/"))