import sqlite3
import speedtest
import os
import time
from sqlite3.dbapi2 import Connection, Cursor

class speedtest_db:
    __database = 'speedtest.db'
    __table = 'speedtest'
    __connection: Connection 
    __cursor : Cursor

    def __init__(self) -> None:
        self.__connection = sqlite3.connect('speedtest.db')
        self.__cursor = self.__connection.cursor()
        if not self.__table_exists():{
            self.__cursor.execute('''create table speedtest ('Date','Time','Download','Uload','Ping') ''')
        }

    def __table_exists(self) -> bool:
        self.__cursor.execute('''select count(name) from sqlite_master where type ='table' and name = 'speedtest' ''')    
        return self.__cursor.fetchone()[0] == 1

class SpeedTestExecutor:
    st : speedtest.Speedtest

    def __init__(self) -> None:
        self.st = speedtest.Speedtest( )

    def execute(self) :
        self.st.get_servers()
        self.st.get_best_server()
        self.st.download()
        self.st.upload()

    def getDownload(self) -> int:
        return str(int(self.st.results.download/1000000))

    def getUpload(self) -> int:
        return str(int(self.st.results.upload/1000000))

    def getPing(self) -> int:
        return str(int(self.st.results.ping))

class CSVWriter:

    def __init__(self, CSVFile) -> None:
        if not os.path.isfile(CSVFile):
            self.__csvFile = open(CSVFile, 'a')
            self.__csvFile.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s) \n')
        else:
            self.__csvFile = open(CSVFile, 'a')

    def __del__(self):
        self.__csvFile.close()
        
    def setDownload(self, d):
        self.__download = d

    def setUpload(self, u):
        self.__upload = u

    def setPing(self, p):
        self.__ping = p
    
    def writeToFile(self):
        self.__csvFile.write('{},{},{},{},{}'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), self.__download, self.__upload, self.__ping))
        self.__csvFile.write('\n')
        

    



