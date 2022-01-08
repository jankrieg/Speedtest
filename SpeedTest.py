import SpeedTestServices

testExecutor = SpeedTestServices.SpeedTestExecutor()
CSVFile = SpeedTestServices.CSVWriter('/home/pi/Python/speedtest.csv')

testExecutor.execute()

CSVFile.setDownload(testExecutor.getDownload())
CSVFile.setUpload(testExecutor.getUpload())
CSVFile.setPing(testExecutor.getPing())
CSVFile.writeToFile()