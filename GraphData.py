import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
rect = fig.patch
f= open("tempCO2.csv","w")
f.write('')#clears file before writing to it
f2= open("tempTVOC.csv","w")
f2.write('')#clears file before writing to it
f3= open("tempTEMP.csv","w")
f3.write('')#clears file before writing to it

def animate(i):
    fco = 'tempCO2.csv'
    fh = open(fco)
    co = list()
    timeC = list()
    for line in fh:
        pieces = line.split(',')
        degree = pieces[0]
        timeB=  pieces[1]
        timeA= timeB[:8]
        #print timeA
        time_string = datetime.strptime(timeA,'%H:%M:%S')
        #print time_string
        try:
            co.append(float(degree))
            timeC.append(time_string)
        except:
            print "dont know"
            
        ax1 = fig.add_subplot(5,1,1)
        #ax1=plt.subplot2grid((6,1),(0,0),rowspan=4,colspan=1)
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        #ax1.clear()
        ax1.plot(timeC,co,'m')
        plt.title('Current CO2 Level')
        plt.xlabel('Time')##add this back in if needed
        plt.ylabel('CO2 ppm')

    fTVOC = 'tempTVOC.csv'
    fh2 = open(fTVOC)
    TVOC = list()
    timeC2 = list()
    for line in fh2:
        pieces = line.split(',')
        degree = pieces[0]
        timeB=  pieces[1]
        timeA= timeB[:8]
        #print timeA
        time_string = datetime.strptime(timeA,'%H:%M:%S')
        #print time_string
        try:
            TVOC.append(float(degree))
            timeC2.append(time_string)
        except:
            print "dont know"
            
        ax2 = fig.add_subplot(5,1,5)
        #ax2=plt.subplot2grid((6,1),(3,0),rowspan=4,colspan=1)
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        #ax1.clear()
        ax2.plot(timeC2,TVOC,'c')
        plt.title('Current TVOC Level')
        plt.xlabel('Time')
        plt.ylabel('TVOC')
        
        
    fTEMP = 'tempTEMP.csv'
    fh3 = open(fTEMP)
    TEMP = list()
    timeC3 = list()
    for line in fh3:
        pieces = line.split(',')
        degree = pieces[0]
        timeB=  pieces[1]
        timeA= timeB[:8]
        #print timeA
        time_string = datetime.strptime(timeA,'%H:%M:%S')
        #print time_string
        try:
            TEMP.append(float(degree))
            timeC3.append(time_string)
        except:
            print "dont know"
            
        ax3 = fig.add_subplot(5,1,3)
        #ax2=plt.subplot2grid((6,1),(3,0),rowspan=4,colspan=1)
        #---ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        #ax1.clear()
        ax3.plot(timeC3,TEMP,'g')
        plt.title('Current Temperature')
        plt.xlabel('Time')
        plt.ylabel('Temperature (C)')
ani = animation.FuncAnimation(fig, animate, interval = 2000)
plt.show()
plt.clf()


