from sense_emu import SenseHat
import time
import sqlite3 
print('File Imported')

sense=SenseHat()

#define connection and cursor
#cursor is used to interact with the database
connection = sqlite3.connect('/home/pi/Documents/SenseHATDB/SenseHATEmulatorDB.db')
cursor = connection.cursor()
data=[]
idd=0
acceleration={'x': 0 , 'y': 0, 'z' :0}
cursor.execute("""CREATE TABLE Test (id integer primary key, Temp Text, Humidity Text, accelerometer_raw Text, Date Text)""")
while True:
    date=time.ctime()   
    temp=sense.get_temperature()
    humidity=sense.get_humidity()
    sense.set_imu_config(False,False,True)
    acc=sense.accelerometer_raw
    x=acc['x']
    y=acc['y']
    z=acc['z']
    
    x=round(x,0)
    y=round(y,0)
    z=round(z,0)
    
    acceleration.update({'x':x,'y': y,'z':z}) # updating acceleration dict
    
    print(temp)
    print("----------------------")
    
    idd=idd+1
    
    data.append(str(idd))
    data.append(str(temp))
    data.append(str(humidity))
    data.append(str(acceleration))
    data.append(str(date))
    
    
    
    cursor.execute("insert into Test values (?,?,?,?,?)",data)
    
    connection.commit()
    print("Data Inserted")
    acceleration.clear()
    data.clear()
    
    time.sleep(60)
    
#cursor.execute("INSERT INTO Test (id,sensor1,sensor2) VALUES ('1','25','50')")
#cursor.execute("INSERT INTO Test (id,sensor1,sensor2) VALUES ('2','26','55')")
#cursor.execute("INSERT INTO Test (id,sensor1,sensor2) VALUES ('3','27','60')")
#cursor.execute("INSERT INTO Test (id,sensor1,sensor2) VALUES ('4','28','65')")

#get result
#cursor.execute("SELECT * FROM Test")

#result=cursor.fetchall()
#print(result)
#connection.commit()

#connection.close()
#print("Closing Connection to DB")
