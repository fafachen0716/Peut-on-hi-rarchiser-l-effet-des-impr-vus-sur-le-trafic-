#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os
import numpy as np
import pandas as pd
import io
import json
import datetime as pkgdt
import time
import requests 
from requests.adapters import HTTPAdapter
import itertools # list operators

  

from requests.auth import HTTPBasicAuth
import requests

file = open('API_STOP.txt', "r")
line = file.readlines()

for lines in line: 
# URL de l'API par arrêt
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef='+ str(lines)
# utilisez readline() pour lire la ligne suivante
    line = file.readline()    
    #header doit contenir la clé API
    
    headers = {'Accept':'application/json', 'apikey':'SjlvM6V0HLNnz2SrHK2v5xxVMArX2N5R'}
    
    
    #envoi de la requête au serveur
    req = requests.get(url, headers = headers)
    data = req.json()
            
            #print('Status:',req)
           
    MonitoredStopVisit_list = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']
    MonitoredVehicleJourney_list = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['DirectionName']
    StopPointName_list = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']
    MonitoredCall_DS = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']['DepartureStatus']
    MonitoredCall_EA = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']       
    MonitoredCall_ED = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedDepartureTime']
    
    
    for MonitoredStopVisit in MonitoredStopVisit_list:
        for DirectionName in MonitoredVehicleJourney_list:
            for StopPointName in StopPointName_list['StopPointName']:
                for DepartureStatus in MonitoredCall_DS:
                    for ExpectedArrivalTime in MonitoredCall_EA: 
                        for ExpectedDepartureTime in MonitoredCall_ED:
                        
                            print ("*********************")
                            print ("Nom de l'opérateur de la ligne : " + MonitoredStopVisit['MonitoredVehicleJourney']['OperatorRef']['value'])
                            print ("Direction du bus : " + DirectionName['value'] )
                            print ("Nom de l'arrêt : "+ StopPointName['value'])
                            print ( "Statut :" + MonitoredCall_DS )
                            print ("Horaire d'arrivée : " + MonitoredCall_EA )
                            print ("Horaire de départ : " + MonitoredCall_ED)
                            
 
                     
open('Reponse.xml', 'wb').write(req.content)

   




