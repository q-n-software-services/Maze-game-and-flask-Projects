import sqlite3
import csv
con = sqlite3.connect("data.db")
cur = con.cursor()

a_file = open("C:\\Users\\HP\\Downloads\\archive\\flights.csv")
rows = csv.reader(a_file)
cur.execute('''DROP TABLE IF EXISTS flights''')

cur.execute('''CREATE TABLE 'flights' ('YEAR' INTEGER, 'MONTH' INTEGER, 'DAY' INTEGER, 'DAY_OF_WEEK' INTEGER, 'AIRLINE' TEXT, 'FLIGHT_NUMBER' INTEGER, 'TAIL_NUMBER' TEXT, 'ORIGIN_AIRPORT' TEXT, 'DESTINATION_AIRPORT' TEXT, 'SCHEDULED_DEPARTURE' INTEGER, 'DEPARTURE_TIME' REAL, 'DEPARTURE_DELAY' REAL, 'TAXI_OUT' REAL, 'WHEELS_OFF' REAL, 'SCHEDULED_TIME' REAL, 'ELAPSED_TIME' REAL, 'AIR_TIME' REAL, 'DISTANCE' INTEGER, 'WHEELS_ON' REAL, 'TAXI_IN' REAL, 'SCHEDULED_ARRIVAL' INTEGER, 'ARRIVAL_TIME' REAL, 'ARRIVAL_DELAY' REAL, 'DIVERTED' INTEGER, 'CANCELLED' INTEGER, 'CANCELLATION_REASON' TEXT, 'AIR_SYSTEM_DELAY' TEXT, 'SECURITY_DELAY' TEXT, 'AIRLINE_DELAY' TEXT, 'LATE_AIRCRAFT_DELAY' TEXT, 'WEATHER_DELAY' TEXT)''')
cur.executemany("INSERT INTO flights VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)
con.commit()

b_file = open("C:\\Users\\HP\\Downloads\\archive\\airports.csv")
rows2 = csv.reader(b_file)
cur.execute('''DROP TABLE IF EXISTS airports''')

cur.execute('''CREATE TABLE 'airports' ('IATA_CODE' TEXT, 'AIRPORT' TEXT, 'CITY' TEXT, 'STATE' TEXT, 'COUNTRY' TEXT, 'LATITUDE' REAL, 'LONGITUDE' REAL)''')
cur.executemany("INSERT INTO airports VALUES (?, ?, ?, ?, ?, ?, ?)", rows2)
con.commit()


c_file = open("C:\\Users\\HP\\Downloads\\archive\\airlines.csv")
rows3 = csv.reader(c_file)
cur.execute('''DROP TABLE IF EXISTS airlines''')

cur.execute('''CREATE TABLE 'airlines' ('IATA_CODE' TEXT, 'AIRLINE' TEXT)''')
cur.executemany("INSERT INTO airlines VALUES (?, ?)", rows3)
con.commit()

"""cur.execute('''SELECT flights.ORIGIN_AIRPORT, DESTINATION_AIRPORT, airports.IATA_CODE, airports.STATE, Count(*) AS ORIGIN_AIRPORT, Count(*) AS DESTINATION_AIRPORT 
FROM flights INNER JOIN airports ON flights.ORIGIN_AIRPORT = airports.IATA_CODE 
GROUP BY airports.STATE
ORDER BY Count(*) DESC , airports.STATE;
''')
print(cur.fetchall())"""

con.close()