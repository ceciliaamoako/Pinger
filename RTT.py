
# Cecilia Amoako
# CS 470 Project 2
# Pinging servers and recording their RTTs

from matplotlib import pyplot as plt
import numpy as np
import os
import re
import time


# # University Servers Used
# ----------------------------
# # University of Athens in Greece: 195.134.71.228 # Europe 
# # Hong Kong University of Science and Technology: 143.89.12.134 # Asia
# # KNUST in Ghana: 129.122.16.228 # Africa 
# # Monash University in Australia 203.82.24.7 # Australia

# A function to ping a server in a 
# 5 seconds interval
def ping(ipAdd):
    while True:
            
        # sleep time to ping the server
        sleep_time = 5
        
        # command to ping the server
        ping_value = os.popen('ping -c 1 ' + ipAdd).read()
        
        # Using regular expression to get the time it 
        # takes to ping the server
        time_taken = re.findall('time=(\d+)',ping_value)
        
        # Causing a 5 seconds sleep time in between each ping
        time.sleep(sleep_time)
        
        # returning an int time taken
        if time_taken:
            return int(time_taken[0])
        else:
            return 0
          
# This chunk of code gets the 
# server ipAddress from the user and stores
# then in array called ipAddress       
print("Please input the four servers you want to ping")
ipAddress = []
for i in range(0, 4):
    address = input("IPAdress of server" + str(i+1) + " : ")
    ipAddress.append(address)

sampleRTT1 = []
sampleRTT2 = []
sampleRTT3 = []
sampleRTT4 = []

# # Pinging each server 100 times by calling
# # the ping function and appending the return
# # value which is the time it takes to ping
# # each server in an array for each server
for i in range(0,100):
    sampleRTT1.append(ping(ipAddress[0]))
    sampleRTT2.append(ping(ipAddress[1]))
    sampleRTT3.append(ping(ipAddress[2]))
    sampleRTT4.append(ping(ipAddress[3]))
    


alpha = 0.125
temp1 = sampleRTT1[0]
temp2 = sampleRTT2[0]
temp3 = sampleRTT3[0]
temp4 = sampleRTT4[0]

EstimatedRTT1 = []
EstimatedRTT2 = []
EstimatedRTT3 = []
EstimatedRTT4 = []

# Calculating the EstimatedRTT based on the sampleRTT
# Add each time calculated to the EstimatedRTT array
for i in range(0,100):
   EstimatedRTT1.append((1 - alpha) * temp1 + alpha * sampleRTT1[i])
   EstimatedRTT2.append((1 - alpha) * temp2 + alpha * sampleRTT2[i])
   EstimatedRTT3.append((1 - alpha) * temp3 + alpha * sampleRTT3[i])
   EstimatedRTT4.append((1 - alpha) * temp4 + alpha * sampleRTT4[i])
   
   temp1 = EstimatedRTT1[i]
   temp2 = EstimatedRTT2[i]
   temp3 = EstimatedRTT3[i]
   temp4 = EstimatedRTT4[i]

x = np.linspace(0,5*100,100)

fig, axs = plt.subplots(2,2, sharex=True, constrained_layout=True)
fig.suptitle('SampleRTT vrs EstimatedRTT')

# Plotting the SampleRTT vrs EstimatedRTT for Europe

axs[0,0].plot(x, EstimatedRTT1)
axs[0,0].plot(x, sampleRTT1)
axs[0, 0].set_title('University of Athens in Greece: Europe')

# Plotting the SampleRTT vrs EstimatedRTT for Asia

axs[0,1].plot(x, EstimatedRTT2)
axs[0,1].plot(x, sampleRTT2)
axs[0, 1].set_title('Hong Kong University of Science and Technology: Asia')

# Plotting the SampleRTT vrs EstimatedRTT for Africa

axs[1,0].plot(x, EstimatedRTT3)
axs[1,0].plot(x, sampleRTT3)
axs[1, 0].set_title('KNUST in Ghana: Africa')

# Plotting the SampleRTT vrs EstimatedRTT for Australia

axs[1,1].plot(x, EstimatedRTT4)
axs[1,1].plot(x, sampleRTT4)
axs[1,1].set_title(' Monash University in Australia: Australia')
axs[1,1].set(xlabel='Time (s)', ylabel='Time Intervals (ms)')

axs.legend()
plt.show()

##### Time Intervals #####

beta = 0.25

temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0


devRTT1 = []
devRTT2 = []
devRTT3 = []
devRTT4 = []

timeout1 = []
timeout2 = []
timeout3 = []
timeout4 = []

# Calculating the devRTT based on the sampleRTT and EstimatedRTT
# Add each time calculated to the devRTT array

for i in range(0,100):
   devRTT1.append((1-beta) * temp1 + beta * np.abs(sampleRTT1[i] - EstimatedRTT1[i]))
   temp1 = devRTT1[i]
   timeout1.append(4 * devRTT1[i] + EstimatedRTT1[i])
   
   devRTT2.append((1-beta) * temp2 + beta * np.abs(sampleRTT2[i] - EstimatedRTT2[i]))
   temp2 = devRTT2[i]
   timeout2.append(4 * devRTT2[i] + EstimatedRTT2[i])
   
   devRTT3.append((1-beta) * temp3 + beta * np.abs(sampleRTT3[i] - EstimatedRTT3[i]))
   temp3 = devRTT3[i]
   timeout3.append(4 * devRTT3[i] + EstimatedRTT3[i])
   
   devRTT4.append((1-beta) * temp4 + beta * np.abs(sampleRTT4[i] - EstimatedRTT4[i]))
   temp4 = devRTT4[i]
   timeout4.append(4 * devRTT4[i] + EstimatedRTT4[i])

fig1, axs1 = plt.subplots(2,2, sharex=True, constrained_layout=True)
fig1.suptitle('Time Intervals')

# Plotting the Time Interval for Europe

axs1[0,0].plot(x, timeout1)
axs1[0, 0].set_title('University of Athens in Greece: Europe')

# Plotting the Time Interval for Asia

axs1[0,1].plot(x, timeout2)
axs1[0, 1].set_title('Hong Kong University of Science and Technology: Asia')

# Plotting the Time Interval for Africa

axs1[1,0].plot(x, timeout3)
axs1[1, 0].set_title('KNUST in Ghana: Africa')

# Plotting the Time Interval for Australia

axs1[1,1].plot(x, timeout4)
axs1[1,1].set_title(' Monash University in Australia: Australia')
axs1[1,1].set(xlabel='Time (s)', ylabel='Time Intervals (ms)')


axs1.legend()
plt.show()