# -*- coding: utf-8 -*-
from pyotrs import Article, Client, DynamicField, Ticket
from datetime import datetime
from datetime import timedelta


client = Client("http://192.168.0.98/otrs/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST", "adm-dsilva", "abdi@2020")
#client.session_restore_or_create()
print(client.session_create())
#client.ticket_get_by_id(6818180, articles=True, attachments=True, dynamic_fields=True)
#print(client.ticket_search(TicketCreateTimeOlderDate=datetime(2021, 1, 20)))
#print(client.ticket_search(TicketCreateTimeNewerDate=datetime.utcnow() - timedelta(days=1)))


ticket_ids = client.ticket_search(States=['new', 'open'], Queues=['Raw'], OwnerIDs=[32])

print("number of my tickets：" + str(len(ticket_ids)))

