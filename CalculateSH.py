import os
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
    lang = int(input("Input >> "))
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
numUID = int(input(Inputting.uidNum))
print(Inputting.uidName)
# Number of List(uid)
while timeUID < numUID:
    print("##", Inputting.name, timeUID + 1, end=' ')
    strName = input()
    UID.extend([strName])
    timeUID += 1
# Inputting every needed value
while timeValue < numUID:
    print("###", UID[timeValue])
    allTime = int(input(Inputting.allWorkTime))
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

# Exit
os.system('pause')
