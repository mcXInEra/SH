#WARNING: This program is changed as demo. Please run CalculateSH.py under normal conditions
# import os
import time

# Initialize parameter
UID = []
timeValue = 0
timeUID = 0
weights = []
serverTime = time.asctime(time.localtime(time.time()))

# Apply language
print("Select language:\n1. English;  2. Chinese (Simplified);  3. Chinese (Tradition)")
while True:
    lang = 2
    print("Input >> 1")
    if lang == 1:
        from lang.en import Opening, Inputting
        break
    if lang == 2:
        from lang.zh_CN import Opening, Inputting
        break
    if lang == 3:
        print("Not available now.")
        # from lang.zh_TW import Lang
    else:
        print("Invalid input. Retry.")

print(Opening.loading, end='')
for i in range(3):
    print(".", end='', flush=True)
    time.sleep(0.5)
    # Here we try to add '#' as loading bar

# Name and list persons
print(Opening.welcome.format(serverTime))
print(Inputting.uidNum, "3")
numUID = 3
print(Inputting.uidName)
# Number of List(uid)

print("##", Inputting.name, timeUID + 1, end=' ')
strName = 'Seton'
    UID.extend([strName])
print("##", Inputting.name, timeUID + 2, end=' ')
strName = 'XH_xr'
    UID.extend([strName])
print("##", Inputting.name, timeUID + 3, end=' ')
strName = 'April'
    UID.extend([strName])
#while timeUID < numUID:
#    print("##", Inputting.name, timeUID + 1, end=' ')
#    strName = input()
#    UID.extend([strName])
#    timeUID += 1

# Inputting every needed value
while timeValue < numUID:
    print("###", UID[timeValue])
    print(Inputting.allWorkTime, "30")
    allTime = 30
    weights.append(allTime)
    timeValue += 1

# Calculating WEIGHTS
# It's now on developing, referring to our SHAREHOLDING LICENCE

# Print result
print("\n*** The program is still on developing, \n*** please wait for the newer release!")
print("# Everything you entered:")
times = 0
while times < numUID:
    print("****", UID[times], weights[times])
    # Here we try to align characters
    times += 1

print("So that's the reason why there's no more result. Goodbye!")
