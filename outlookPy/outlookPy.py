#-*- coding:utf-8 -*-
from win32com.client import constants
from win32com.client.gencache import EnsureDispatch as Dispatch

outlook = Dispatch("Outlook.Application")
mapi = outlook.GetNamespace("MAPI")

print(mapi.GetDefaultFolder(6))


class Oli():
    def __init__(self, outlook_object):
        self._obj = outlook_object

    def items(self):
        array_size = self._obj.Count
        for item_index in range(1,array_size+1):
            yield (item_index, self._obj[item_index])

    def prop(self):
        return sorted( self._obj._prop_map_get_.keys() )
def saveHtml(htmlName, htmlBody):
    with open(htmlName+str('.html'), 'w') as f:
        f.write(htmlBody)

def mailMessage(folderName):
    i = 0
    messages = subfolder1.Items
    message = messages.GetFirst()
    while message:
        inboxMessage.append(message.Subject + message.Categories)
        # print(message.Subject)
        #print(message.Categories)
        # print(message.ReceivedTime)
        saveHtml(str(i),message.HTMLBody)
        # Process a message
        #print("%s;%s;%s" % (message.Categories, message.Subject, message.SentOn))
        message = messages.GetNext()
        i += 1

        if i > 20:
            exit()
            break
    
def writeMail(liness):
    with open("outlook.out",'wb') as f:
        for line in inboxMessage:
            try:
                f.write(line)
                f.write('\n')
            except:
                continue

if __name__ == '__main__':

    inboxMessage = []
    for inx, folder in Oli(mapi.Folders).items():
        # iterate all Outlook folders (top level)
        print(folder.Name)
        print("|----------|")
        for inx,subfolder in Oli(folder.Folders).items(): 
            for inx1, subfolder1 in Oli(subfolder.Folders).items():
                mailMessage(subfolder1)
                print("(%i)" % inx1, subfolder1.Name,"=> ", type(subfolder1))       
            print("(%i)" % inx, subfolder.Name,"=> ", type(subfolder))
    writeMail(inboxMessage)