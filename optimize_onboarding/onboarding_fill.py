import PySimpleGUI as sg
import tempfile 
from fdfgen import forge_fdf
import subprocess

sg.theme("DarkAmber")
fields = ["Client Name","Client Name_2","Portfolio Manager","CRM Contact ID","Optimize Relationship Manager"]
layout = [map(lambda field: [sg.Text(field),sg.InputText(key=f"-{field}-")],fields)] + [[sg.Button('OK'),sg.Button('Cancel')]]
window=sg.Window("Enter the data",layout)
# Event Loop to process "events" and get the "values" of the inputs

event, values = window.read()
if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
    exit(1)
print(f'event: {event} You entered {values}')
tf=tempfile.NamedTemporaryFile

fields_o1= [ ("Adviser Representative",values["-Portfolio Manager-"]), ("Client Name",values["-Client Name-"]),("Client Name_2",values["-Client Name_2-"]) ]
fields_o2= [ ("Licensed Portfolio Manager",values["-Portfolio Manager-"]), 
            ("Client Name 1",values["-Client Name-"]),("Client Name 2",values["-Client Name_2-"]),
           ("Optimize Relationship Manager", values["-Optimize Relationship Manager-" ]),
           ('CRM Contact ID',values["-CRM Contact ID-"])]
fields_o3= [ ("Name",values["-Client Name-"]),("Name_2",values["-Client Name_2-"]) ]
inputs=["o1.pdf","o2.pdf","o3.pdf"]
outputs=["Onboarding.1.pdf","Onboarding.2.pdf","Onboarding.3.pdf"]
fields=[fields_o1,fields_o2,fields_o3]

for i,o,f in zip(inputs,outputs,fields):
    with tf(delete=False) as fdf_file:
        fdf= forge_fdf("",fields_o3,[],[],[])
        fdf_file.write(fdf)
        fdf_file.close()
        print(f"Wrote {fdf_file.name}")
        pdf_cmd1=["pdftk",i,"fill_form",fdf_file.name,"output",o]

        print(f"pdftk command: {pdf_cmd1}")
        subprocess.run(pdf_cmd1)


    
    



window.close()