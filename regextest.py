import sys
import re


message = '''Trigger: PROBLEMA
Trigger severity: 1
Trigger nseverity: 2
Trigger status: PROBLEMA
Trigger URL: http
Host: VMWARETESTE
Host description: HOSTAQUI
Event age: 22222
Zabbix event ID: 33333
'''

zabbixtrigger = {
    # capiturando o host da messagem
    'host': {
        'configuration_item': '^Host: .*',
        #'zabbix_event_id': '^Zabbix event ID: .*',
    },
    'eventid': {
        'zabbix_event_id': '^Zabbix event ID: .*',
    }
}
for key in zabbixtrigger['host']:
    itemshost=re.findall(zabbixtrigger['host'][key], message, re.MULTILINE)
    itemshost[0] = itemshost[0].split(':')[1].strip()
    hostname=itemshost[0]
    print(hostname)

for key in zabbixtrigger['eventid']:
    itemsid=re.findall(zabbixtrigger['eventid'][key], message, re.MULTILINE)
    itemsid[0] = itemsid[0].split(':')[1].strip()
    eventid=itemsid[0]
    print(eventid)
