import docx2txt
lines=docx2txt.process('C:\\Users\\VPrakas\\Desktop\\ChangeControlForm_Schema_compact_capc-capitalone01.docx').lower().splitlines()
for i in lines:
    if("maintenance window" in i):
        print(i)


        
