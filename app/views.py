from flask import *
import os
from app import app

import psycopg2 as pg
connection = pg.connect(host="ec2-54-83-23-91.compute-1.amazonaws.com",database="d85fepf5uvs059", user="sijlscnpyawdzh", password="b201ad69864dbfaaabf6ef0b55d0c2347b587f6812e1ee3ef58665657f0c71cf")
cur = connection.cursor()


# Web page renders
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensor')
def sensor():
    return render_template('sensor.html')

@app.route('/asset/<assetType>')
def about(assetType):
    data = {}
    tagdata = {}

    if assetType=='assettag':
      cur.execute("select * from sensorassetlist where category = 'assetTag'");
      vals = cur.fetchall()
      data = {}
      links = []
      data["name"]="AssetTag Sensors List"
      link = {}
      link['val'] = 'RF receiver for active RFID (Sunrom)'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'RFID reader - Passive RC522'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'RFID Tag (125khz) – Passive'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'RFID transmitter Tag - Active (sunrom)'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Barcodes'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'NFC Tags'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Wifi, IR and Bluetooth'
      link['href'] = "#"
      links.append(link)
      link = {}
      link = {}
      link['val'] = 'Sensor tags'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Security tags'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Smart Alarm Motion Sensor'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'UHF RFID Tag'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Long Range UHF RFID reader (ISO18000-6C EPC G2)'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Strain gauge'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'IR Tag'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Vibration Sensor Active Tag'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'GPS Tracker'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'Tamper Proof RFID UHF Windshield Tag for Vehicles (Pack of 50) 110 X 45 mm size'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'UHF RFID Antenna'
      link['href'] = "#"
      links.append(link)
      link = {}
      link['val'] = 'UHF RFID Key Tag, EPC Gen2 (900MHz)'
      link['href'] = "#"
      links.append(link)
      data['links']=links

      allVals = []

      data["name1"]="Sensor List"

      for assets in vals:
          astag = {}

          astag['imgs'] = assets[13]
          astag['names'] = assets[1]
          astag['descrp'] = assets[2]
          astag['ref'] = assets[3]
          astag['procure'] = assets[4]

          allVals.append(astag)
          tagdata['allVals']=allVals

    if assetType=='health':
        cur.execute("select * from sensorassetlist where category = 'health'");
        vals = cur.fetchall()
        links = []
        data["name"]="Health Sensors List"
        link = {}
        link['val'] = 'Patient Position Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Glucometer Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Body Temperature Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Blood Pressure Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Pulse and Oxygen in Blood Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Airflow Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Galvanic Skin Response Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Electrocardiogram Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Electromyography Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Muscle Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Body position sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Spirometer Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Snore Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Glucometer Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'SPO2 Pulsioximeter Sensor'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals


    if assetType=='energy':
        cur.execute("select * from sensorassetlist where category = 'energy'");
        vals = cur.fetchall()
        links = []
        data["name"]="Energy Sensors List"
        link = {}
        link['val'] = 'Pyroelectric Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Photodiode Energy Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'EnergyMax Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Vernier Energy Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'PIR sensor (motion detection)'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'IR proximity sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Light sensors(LDR)'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    if assetType=='agri':
        cur.execute("select * from sensorassetlist where category = 'agri'");
        vals = cur.fetchall()
        links = []
        data["name"]="Agriculture Sensors List"
        link = {}
        link['val'] = 'Optical Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Electrochemical Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Dielectric Soil Moisture Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Soil Humidity Sensor Hygrometer AR605'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Soil moisture sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Soil Temperature and Humidity Sensor SHT20'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = ' Rain Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'pH Sensor'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    if assetType=='transport':
        cur.execute("select * from sensorassetlist where category = 'transport'");
        vals = cur.fetchall()
        links = []
        data["name"]="Transportion Sensors List"
        link = {}
        link['val'] = 'Ladar Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Magnetic Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Piezoelectric Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Radar Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'ODB'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Throttle Position Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Manifold Absolute Pressure Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Engine Coolant Temperature Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Mass Air Flow Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Crankshaft Position Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Camshaft position Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'EGR Temperature Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Boost Pressure Sensor'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    
    if assetType=='oil':
        cur.execute("select * from sensorassetlist where category = 'oil'");
        vals = cur.fetchall()
        links = []
        data["name"]="Oil And Gas Sensors List"
        link = {}
        link['val'] = 'Piezoelectric Pressure Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Engine Pressure Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Level Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Honeywell Sensors and Switches'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Fiber Optic Sensors '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Alcohol sensor MQ3 '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Gas sensor MQ2 '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'LPG sensor MQ6 '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Pressure Sensor '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Carbon Monoxide Sensor '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Hydrogen Sulfide Sensor '
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    if assetType=='power':
        cur.execute("select * from sensorassetlist where category = 'power'");
        vals = cur.fetchall()
        links = []
        data["name"]="Power Sensors List"
        link = {}
        link['val'] = 'MA2400xA series thermal Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'MA24106A power Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'MA2411B pulse power Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'MA244XD standard diode Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = ' Light Meter'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Multimeter'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Oscilloscope'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Smart Meter'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    if assetType=='whealth':
        cur.execute("select * from sensorassetlist where category = 'whealth'");
        vals = cur.fetchall()
        links = []
        data["name"]="Smart Health Wearables"
        link = {}
        link['val'] = 'Fitbit'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Withings Blood Pressure'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Viatom Checkme'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Muse headband'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Gymwatch Fitness Tracker'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Jawbone'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Poly Implant Prothse Device'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    if assetType=='whome':
        cur.execute("select * from sensorassetlist where category = 'whome'");
        vals = cur.fetchall()
        links = []
        data["name"]="Smart Home Wearables"
        link = {}
        link['val'] = 'Alarm Sensors'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Smart Thermostat'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Video doorbell'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Leak/moisture detection'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Fire/CO detection '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Hall effect sensor MH183 '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'CURB Home Energy Monitoring System '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Ecobee3 Thermostat with Sensor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Sonos Play'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Philips Hue'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Amazone Echo'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Sensor List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals


    return render_template('assetList.html',data=data,tagdata=tagdata)

@app.route('/industry/industrial')
def industry():
    # print ("industrial.html")
    return render_template('industrial.html')

@app.route('/wearable')
def wearable():
    return render_template('wearable.html')

@app.route('/operation')
def operation():
    return render_template('operation.html')

@app.route('/health')
def health():
    return render_template('health.html')


@app.route('/actuatordirectory')
def actuatordirectory():
    return render_template('actuatordir.html')

@app.route('/actuator/<actuatorLists>')
def actuator(actuatorLists):
    data = {}
    tagdata = {}
    if actuatorLists=='actuator':
        cur.execute("select * from sensorassetlist where category = 'actuator'");
        vals = cur.fetchall()
        links = []
        data["name"]="Actuators"
        link = {}
        link['val'] = 'Servo Motor '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Stepper Motor'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Electric Actuator'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Hydraulic actuators'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Pneumatic actuator'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Thermal or magnetic Actuator'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Mechanical Actuator'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Actuators List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    return render_template('actuatorlist.html', data=data,tagdata=tagdata)

@app.route('/controllerdirectory')
def controllerdirectory():
    return render_template('controllerdir.html')

@app.route('/control/<controllers>')
def control(controllers):
    data = {}
    tagdata = {}
    if controllers=='controller':
        cur.execute("select * from sensorassetlist where category = 'controller'");
        vals = cur.fetchall()
        links = []
        data["name"]="Controller"
        link = {}
        link['val'] = 'Raspberry Pi '
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'NodeMCU'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Particle Photon'
        link['href'] = "#"
        links.append(link)
        link = {}
        link['val'] = 'Arduino'
        link['href'] = "#"
        links.append(link)
        data['links']=links

        allVals = []

        data["name1"]="Controller List"

        for assets in vals:
            astag = {}

            astag['imgs'] = assets[13]
            astag['names'] = assets[1]
            astag['descrp'] = assets[2]
            astag['ref'] = assets[3]
            astag['procure'] = assets[4]

            allVals.append(astag)
            tagdata['allVals']=allVals

    return render_template('control.html', data=data,tagdata=tagdata)


@app.route('/module')
def module():
    return render_template('module.html')


@app.route('/cloud')
def cloud():
    return render_template('cloud.html')

# Webservices
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/storeBalance/<bal>')
def storeData(bal):
    fopen = open('balance','w')
    fopen.write(bal)
    fopen.close()
    return 'Balance Updated, {}!'.format(bal)
