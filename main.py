import ESP8266WebServer as server
from dht12 import DHT12
from machine import I2C, Pin, SPI, RTC
import st7735
from rgb import color565
from rgb_text import text as displayText
from WifiConnect import wifiConnect
import network
import urandom
import time
import json
import time


def getTemperature():
    '''liefert Temperaturmessung vom Sensor '''
    sensorDht12.measure()
    return sensorDht12.temperature()

def getHumidity():
    '''liefert Feuchtigkeitsmessung vom Sensor'''
    sensorDht12.measure()
    return sensorDht12.humidity()

# Wi-Fi configuration

ssid = "gsog-iot"
password = "IOT_Projekt_BFK-S_2022"

wifiConnect(ssid, password)

# Liefert CSS fuer Webseite
def get_css():
    css = """<style>
        body {
           background-color: #ffffff;
           font-family: Arial, Helvetica, Sans-Serif;
           Color: #000000;
        }
        .table-header {
            border: 1px solid #ddd;
            padding: 8px;
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #04AA6D;
            color: white;
        }
        .table-row {
            border: 1px solid #ddd;
            padding: 8px;
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
        }
        #temp {
            text-align: right;
            color: #FF0000;
        }
        #hum {
            text-align: right;
            color: #0000FF;
        }
      </style>"""  
    return css

       
def handleRoot(socket,args):
#    print("in handleRoot")

    jsonData=loadJson()
    
    #initialize variables incase list doesnt have the data
    time0=""
    time1=""
    time2=""
    time3=""
    time4=""
    time5=""
    time6=""
    time7=""
    time8=""
    time9=""
    
    temp0=""
    temp1=""
    temp2=""
    temp3=""
    temp4=""
    temp5=""
    temp6=""
    temp7=""
    temp8=""
    temp9=""
    
    hum0=""
    hum1=""
    hum2=""
    hum3=""
    hum4=""
    hum5=""
    hum6=""
    hum7=""
    hum8=""
    hum9=""
    
    #override variables with data from Json
    if len(jsonData)>0:
        #string cast removing brackets
        time0=str(jsonData[0]["Time"])[1:-1]
        temp0=str(jsonData[0]["Temp"])
        hum0=str(jsonData[0]["Hum"])
        
    if len(jsonData)>1:
        time1=str(jsonData[1]["Time"])[1:-1]
        temp1=str(jsonData[1]["Temp"])
        hum1=str(jsonData[1]["Hum"])
        
    if len(jsonData)>2:
        time2=str(jsonData[2]["Time"])[1:-1]
        temp2=str(jsonData[2]["Temp"])
        hum2=str(jsonData[2]["Hum"])
        
    if len(jsonData)>3:
        time3=str(jsonData[3]["Time"])[1:-1]
        temp3=str(jsonData[3]["Temp"])
        hum3=str(jsonData[3]["Hum"])
        
    if len(jsonData)>4:
        time4=str(jsonData[4]["Time"])[1:-1]
        temp4=str(jsonData[4]["Temp"])
        hum4=str(jsonData[4]["Hum"])
    
    if len(jsonData)>5:
        time5=str(jsonData[5]["Time"])[1:-1]
        temp5=str(jsonData[5]["Temp"])
        hum5=str(jsonData[5]["Hum"])
        
    if len(jsonData)>6:
        time6=str(jsonData[6]["Time"])[1:-1]
        temp6=str(jsonData[6]["Temp"])
        hum6=str(jsonData[6]["Hum"])
               
    if len(jsonData)>7:
        time7=str(jsonData[7]["Time"])[1:-1]
        temp7=str(jsonData[7]["Temp"])
        hum7=str(jsonData[7]["Hum"])
    
    if len(jsonData)>8:
        time8=str(jsonData[8]["Time"])[1:-1]
        temp8=str(jsonData[8]["Temp"])
        hum8=str(jsonData[8]["Hum"])
        
    if len(jsonData)>9:
        time9=str(jsonData[9]["Time"])[1:-1]
        temp9=str(jsonData[9]["Temp"])
        hum9=str(jsonData[9]["Hum"])
    
    page = """<!DOCTYPE HTML>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="utf-8">
    <html>
    <head>
      <title>HTML Marvin and Martin</title>
      {0}
    </head>
    <body>
      <p>to get current values please refresh the page</p>
      <h3>last sensor readings:</h3>
      <p>Temperature: {1}°C</p>
      <p>Humidity: {2}</p>

        <table>
          <tr class="table-header">
            <th>Time</th>
            <th>Temperature</th>
            <th>Humidity</th>
          </tr>
          <tr class="table-row">
            <td>{3}</td>
            <td id="temp">{13}°C</td>
            <td id="hum">{23}%</td>
          </tr>
          <tr class="table-row">
            <td>{4}</td>
            <td id="temp">{14}°C</td>
            <td id="hum">{24}%</td>
          </tr>
          <tr class="table-row">
            <td>{5}</td>
            <td id="temp">{15}°C</td>
            <td id="hum">{25}%</td>
          </tr>
          <tr class="table-row">
            <td>{6}</td>
            <td id="temp">{16}°C</td>
            <td id="hum">{26}%</td>
          </tr>
          <tr class="table-row">
            <td>{7}</td>
            <td id="temp">{17}°C</td>
            <td id="hum">{27}%</td>
          </tr>
          <tr class="table-row">
            <td>{8}</td>
            <td id="temp">{18}°C</td>
            <td id="hum">{28}%</td>
          </tr>
          <tr class="table-row">
            <td>{9}</td>
            <td id="temp">{19}°C</td>
            <td id="hum">{29}%</td>
          </tr>
          <tr class="table-row">
            <td>{10}</td>
            <td id="temp">{20}°C</td>
            <td id="hum">{30}%</td>
          </tr>
          <tr class="table-row">
            <td>{11}</td>
            <td id="temp">{21}°C</td>
            <td id="hum">{31}%</td>
          </tr>
          <tr class="table-row">
            <td>{12}</td>
            <td id="temp">{22}°C</td>
            <td id="hum">{32}%</td>
          </tr>
        </table>  
        <button type="button">
            <a href="/TempHum.json" download="TempHum.json">Download</a>
        </button>      
    </body>
    </html>""".format(get_css(),
                      getTemperature() ,
                      getHumidity(),
                      time0, #3
                      time1,
                      time2,
                      time3,
                      time4,
                      time5,
                      time6,
                      time7,
                      time8,
                      time9, #12
                      temp0, #13
                      temp1,
                      temp2,
                      temp3,
                      temp4,
                      temp5,
                      temp6,
                      temp7,
                      temp8,
                      temp9, #22
                      hum0, #23
                      hum1,
                      hum2,
                      hum3,
                      hum4,
                      hum5,
                      hum6,
                      hum7,
                      hum8,
                      hum9 #32
                      )
    server.ok(socket,"200","text/html",page)
    
def handlePlainValue(socket,args):
#    print("in handlePlainValue")
    server.ok(socket,"200",str(randint(10,40)))
    
def handleTemperatureValue(socket,args):
#    print("in handlePlainValue")
    server.ok(socket,"200",str(sensorDht12.temperature()))

def handleHumidityValue(socket,args):
#    print("in handlePlainValue")
    server.ok(socket,"200",str(sensorDht12.humidity()))
    
def handleJson(socket,args):
#    print("in handleJson")
    server.ok(socket,"200",str(loadJson()))

def handleOnNotFound(socket):
#    print("in handleOnNotFound")
    server.err(socket,"404","File Not Found")

def loadJson():
    """laden der TempHum.json Datei"""
    
    # laden und return der JSON Datei
    with open('TempHum.json') as json_data:
        returnJson = json.load(json_data)
        json_data.close
        return returnJson
        
def setJson():
    """Generieren einer TempHum.json Datei"""

    #meassure Temperature
    temp = getTemperature()
    tempUnit="C"
    #meassure Humidity
    hum = getHumidity()
    humUnit="%"
    #get current time
    measureTime = RTC().datetime()
    
    #check if Json file exists
    try:
        TempHum = loadJson()
    except:
        TempHum = []
    
    #remove first position when 10 entries
    if len(TempHum) == 10:
        TempHum.pop(0)
        
    #add stored values to list
    TempHum.append({'Time': measureTime, 'Temp': temp, 'Hum': hum, 'TempUnit': tempUnit, 'HumUnit': humUnit})
    
    #save list to file
    with open('TempHum.json', 'w', encoding='utf-8') as f:
        json.dump(TempHum, f)
        return True
    

def drawTempHum():
    """Zeichnet die aktuellen Temperatur und Feuchtigkeitswerte auf den Display"""
    
    displayText(display, ("temp:" + str(getTemperature())), x=5, y=20)
    displayText(display, ("hum:" + str(getHumidity())), x=5, y=30)
    

def drawCoordinateSystem(systemPosX=25, systemPosY=43, systemHeight=72):
    """Zeichnet das Koordinatensystem fuer den Graphen auf den Display"""
    
    #coordinate Y description
    for i in range(0, 7):
        displayText(display, (str(i*10)), x=5, y=systemPosY+systemHeight-(i*10)-5, color=color565(255,0,0), background=0xFFFF)
    
    #fill rectangle to remove lines from draw text
    display.fill_rectangle(systemPosX, systemPosY, 20, systemHeight-3, 0xFFFF)
       
    #coordinatesystem
    display.hline(x=systemPosX, y=115, width=60, color=0x0000)
    display.vline(x=systemPosX, y=45-2, height=70+2, color=0x0000) #height goes down
    
    #coordinate segmentation Y
    for i in range(0, 14):
        posY= 45+(i*5)
        display.hline(x=systemPosX-1, y=posY, width=3, color=0x0000)
        
    #coordinate segmentation X
    for i in range (0,10):
        posX = systemPosX+5+(i*5)
        display.vline(x=posX, y=systemPosY+systemHeight-1, height=3, color=0x0000)
        
    
def drawGraphs(systemPosX=25, systemPosY=43, systemHeight=72):
    """Zeichnet werte aus Json in das Koordinatensystem auf dem Display"""
    #draw on globally stored previous Json value
    global storedValues
    
    #overwrite screen with white color on old coordinates
    if len(storedValues) > 0:
        for i in range(len(storedValues)):
            posX = (systemPosX+2)+(5*i)
            posHumY = (systemPosY+systemHeight)-int(storedValues[i]["Hum"])
            posTempY = (systemPosY+systemHeight)-int(storedValues[i]["Temp"])
            display.hline(x=posX, y=posHumY, width=5, color=0xFFFF)
            display.hline(x=posX, y=posTempY, width=5, color=0xFFFF)
            
    #try opening json file and override storedValues variable with the Json data
    try:   
        currentValues=loadJson()
        storedValues=currentValues
    except:
        currentValues=[]
        storedValues=[]
        
    #overwrite screen with currentValues
    if len(currentValues) > 0:
        for i in range(len(currentValues)):
            posX = (systemPosX+2)+(5*i) 
            posHumY = (systemPosY+systemHeight)-int(currentValues[i]["Hum"])
            posTempY = (systemPosY+systemHeight)-int(currentValues[i]["Temp"])
            #draw humidity (blue line)
            display.hline(x=posX, y=posHumY, width=5, color=color565(0, 0, 255))
            #draw temperature (red line)
            display.hline(x=posX, y=posTempY, width=5, color=color565(255, 0, 0))
    
#initialize i2c and dht12 sensor
i2c = I2C(scl=Pin(5), sda= Pin(4))
sensorDht12 = DHT12(i2c)

#initialize display
display = st7735.ST7735R(SPI(1, baudrate=900000), dc=Pin(0), cs=Pin(2), rst=Pin(15), height=131, width=130)
#clear screen
display.fill(0xFFFF)
#draw caption
#displayText(display, ("Marvin & Martin"), x=5, y=5, color=color565(255, 0, 0), background=color565(0, 0, 255))
#draw coordinate system and initialize stored Values variable to store previous iterations Json values
drawCoordinateSystem()

#initialize real time clock
RTC()
#store current Time
currentTime=RTC().datetime()
print("server start time: " + str(currentTime)[1:-1])

#initialize Value variable to save previous cycles Json data. Necessary to clear previously drawn graph lines
storedValues=[]

#server start
server.begin()
server.onPath("/", handleRoot)
server.onPath("/plainValue", handlePlainValue)
server.onPath("/temperatureValue", handleTemperatureValue)
server.onPath("/humidityValue", handleHumidityValue)
server.onPath("/json", handleJson)
server.onNotFound(handleOnNotFound)

try:
    while True:
        # Let server process requests
        server.handleClient()
        #check whether at least 1 second passed, then update Json and draw updated Graph
        if (currentTime[6] != RTC().datetime()[6]):
            currentTime=RTC().datetime()
            try:
                #generate Json file or update existing one
                setJson()
            except:
                print('setJson failed')
            try:
                #draw graphs on display
                drawGraphs()
                #draw temperature and humidity values on display
                drawTempHum()
                #print("currentTime= " + str(currentTime))
            except:
                print('draw failed')

except Exception as e:
    print(e)
    server.close()
    
