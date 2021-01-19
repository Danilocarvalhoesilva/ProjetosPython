import xml.etree.ElementTree as ET

tree = ET.parse('txt.xml')
root = tree.getroot()
#print(root.tag)

entry = root.findall(".//entry")
for ep in entry:
    doman = ep.find('domain').text
    receive = ep.find('receive_time').text
    serial = ep.find('serial').text
    seqno = ep.find('seqno').text
    actionflags = ep.find('actionflags').text
    logo = ep.find('is-logging-service').text
    tipo = ep.find('type').text
    subtype = ep.find('subtype').text
    config_ver = ep.find('config_ver').text
    time_generated = ep.find('time_generated').text
    dg_hier_level_1 = ep.find('dg_hier_level_1').text
    dg_hier_level_2 = ep.find('dg_hier_level_2').text
    dg_hier_level_3= ep.find('dg_hier_level_3').text
    dg_hier_level_4 = ep.find('dg_hier_level_4').text
    device_name = ep.find('device_name').text
    vsys_id = ep.find('vsys_id').text
    eventid = ep.find('eventid').text
    objecto = ep.find('object').text
    fmt = ep.find('fmt').text
    id = ep.find('id').text
    module = ep.find('module').text
    severity = ep.find('severity').text
    opaque = ep.find('opaque').text

    print(opaque)
    print(module)
    print(serial)
    print(severity)
    print(id)
    print(fmt)
    print(objecto)
    print(eventid)
    print(vsys_id)
    print(device_name, dg_hier_level_4, dg_hier_level_3, time_generated, config_ver, tipo, logo, actionflags, seqno, subtype)
#print(range(len(entry)))
#print(entry)

#for child in root:
#    print(child.tag, child.attrib)


#for movie in root.iter('entry'):
#    print(movie.attrib)



#for d in root.iter():
#    if not d:
    #print(description.find('domain').text)
#        print(d.tag, d.text)

#for movie in root.findall("./result/log/logs/entry"):
#    print(movie.attrib)

