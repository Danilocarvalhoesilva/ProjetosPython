
import inotify.adapters

def _main():
    i = inotify.adapters.Inotify()
    i.add_watch('/root')
    i.add_watch('/root/teste')
    i.add_watch('/root/Desktop')

    for event in i.event_gen():#yield_nones=False):
        if event is not None:
            (header, type_names, path, filename) = event

            x = type_names[0]
            listIF = ['IN_CLOSE_WRITE','IN_CREATE', 'IN_MODIFY', 'IN_DELETE']         
            if x in listIF:
                #print("Arquivo modificado: ",filename)
                if filename.endswith('.conf'):
                    print("ARQUIVO MODIFICADO: ", filename)
                    print("https://"+filename)
                    words = filename.split('.')[0]
                    print(words.upper())

        
if __name__ == '__main__':
    _main()
