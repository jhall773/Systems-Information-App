import sqlite3
import pandas as pd
import random
import math

conn = sqlite3.connect("Computer_Manager.db")
#Makes an In-House Database That Exists on Computer Disk in this Programming Folder
                                            
cur = conn.cursor()

#Lines to Use when fist displaying Database
#cur.execute("CREATE TABLE Computer_Data (CPU, Memory, Screen_Time, Battery)")

CPU = [3.0, 2.8, 1.1, 5.2, 6.9, 7.8, 8.8, 9.6, 5.7, 4.1, 3.4] #Simulates CPU Data from gpuntil Data Mining

data = pd.DataFrame({"CPU": CPU})

specfic = {"CPU": CPU}

dissected_data = data.loc[data["CPU"] > 2.0]

print (data)


#for item in CPU:
    #cur.execute(f"INSERT INTO Computer_Data VALUES ({item}, 0, 0, 0);")
    #conn.commit() #Changes don't actually happen unless you do this!!!

#Lines to Delete Table After to Running Tests
#cur.execute("DROP TABLE Computer_Data")
#conn.commit()

cur.close()
conn.close()
