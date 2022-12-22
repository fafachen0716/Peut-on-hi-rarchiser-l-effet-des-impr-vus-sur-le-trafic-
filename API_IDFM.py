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


api_url= "https://opendata.paris.fr/api/records/1.0/search/?dataset=comptage-multimodal-comptages&q=&facet=label&facet=t&facet=mode&facet=voie&refine.t=2022%2F12"

api_pwd ='357b149b931893ee9e6ece99609651cf136256d17d2763b930dfd278'

    
headers = {'Accept':'application/json', 'apikey':api_pwd}
req = requests.get(api_url, headers = headers)
data = req.json()

compteurs=data['records'][0]
for compteur in compteurs:
    print('*****************')
    print("localisation_record : " + compteurs['fields']['label'])
    print('mode : '+ compteurs['fields']['mode'])
    print('type_voie : '+ compteurs['fields']['voie'])
    print('temps_record : '+ compteurs['fields']['t'])
    
open('Reponse.xml', 'wb').write(req.content)





   




