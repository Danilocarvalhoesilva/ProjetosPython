#!/usr/bin/env python3
import logging
from zabbix.api import ZabbixAPI
import time
import sys

logging.basicConfig(level = logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

# Create ZabbixAPI class instance
zapi = ZabbixAPI(url='http://192.168.0.249/zabbix/', user='adm-dsilva', password='abdi@2020')

zhost = "WEBSCENARIO-ABDI"

# Get all disabled hosts
result2 = zapi.do_request('host.get',
                          {
                              'filter': {'host': [zhost] },
                              #'filter': {'status': 1},
                              'output': 'extend'
                          })

# Filter results
hostname = result2['result'][0]['host'] #[host['host'] for host in result2['result']]
hostid = result2['result'][0]['hostid'] 
print(hostname)
print(hostid)

zversion = zapi.do_request('apiinfo.version')
print("Zabbix API version: {}".format(zversion['result']))
version_number = zversion['result']
print(version_number)
# API func changed from 2.x to 3.x
zfunc = "httptest" if version_number>"2." else "webcheck"
print(zfunc)

# create web scenario to google main landing page

service_name= sys.argv[1]
service_url= sys.argv[2]
service_expected_status="200,301,302,304"
agent="Google Chrome"

def zabbix_http_test_create(zfunc,hostid,service_name,agent,service_url,service_expected_status):
    # makes zabbix api call out to create httptest object
    createRes = zapi.do_request(zfunc+'.create',
                      {
                          'name': service_name,
                          'agent': agent,
                          'hostid': hostid,
                          'steps': [
                            {
                              'name': service_name,
                              'url': service_url,
                              'status_codes': service_expected_status,
                              'no': 1
                            }
                          ]
                      })
    return createRes

def zabbix_trigger_get(hostid, service_name):
    # retrieves trigger
    getRes = zapi.do_request('trigger.get',{ 'hostids': hostid,
           'output': 'extend',
           'selectHosts': 'extent',
           'expandExpression': True,
           'expandDescription': True,
           'skipDependent': False,
           'filter': {'description': service_name } })
    return getRes
tpriority=int(4)
def zabbix_webfail_trigger_create(webTestId,service_name,tpriority):
    # makes zabbix api call to create trigger for http test
    trigRes = zapi.do_request('trigger.create',
                  {
                          'hostid': webTestId,
                          'description': service_name + ' is down',
                          'expression': '{' + zhost + ':web.test.fail[' + service_name + '].last(#3)}=1',
                          'priority': tpriority
                  })
    return trigRes


###CRIANDO WEB SCENARIO
print("============CRIACAO WEB SCENARIO===================")
# do http test creation
getRes = zapi.do_request(zfunc + '.get',{ 'hostids': hostid, 'filter': {'name': service_name} })
print(getRes['result'])
print(getRes)
print(len(getRes['result']))

if len(getRes['result'])<1:
    print("CRIANDO WEB SCENARIO PARA O HOST: {}".format(service_name))
    createRes = zabbix_http_test_create(zfunc,hostid,service_name,agent,service_url,service_expected_status)
    webTestId = createRes['result']['httptestids'] # no arrayed result
    print("CRIADO WEB SCENARIO {} COM ID {}".format(service_name,webTestId))
else:
    print("JA EXISTE WEB SCENARIO PARA O HOST: {}".format(service_name))
    webTestId = getRes['result'][0]['httptestid']
print("")

print("WEB SCENARIO CRIADO, MOVENDO PARA A TRIGGER")


##CRIANDO TRIGGER 
print("============CRIACAO DA TRIGGER===================")
# do trigger creation for http test
print("VERIFICANDO NA TRIGGER O ID DO TESTE HTTP: {}".format(webTestId))
getRes = zabbix_trigger_get(hostid,service_name+' is down')

if len(getRes['result'])<1:
    print("CRIANDO TRIGGER PARA HOST: {}".format(service_name))
    trigRes = zabbix_webfail_trigger_create(webTestId,service_name,tpriority)
    time.sleep(1)
else:
    print("TRIGGER JA EXISTE PARA O HOST: {} ID: {}".format(service_name,getRes['result'][0]['triggerid']))
print("")


# Logout from Zabbix
zapi.user.logout()
