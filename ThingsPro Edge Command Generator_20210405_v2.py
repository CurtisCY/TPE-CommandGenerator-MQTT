import tkinter as tk
import tkinter.messagebox as tm
import tkinter.ttk as tt
import tkinter.scrolledtext as scrolledtext
from tkinter import Menu
from tkinter import Spinbox as sp
from tkinter import filedialog
from datetime import datetime
import json


def message_payload():

    varTime = f'{var_year.get()}' + '-' + f'{var_month.get():0>2}' + '-' + f'{var_date.get():0>2}' \
            + ' ' + f'{var_hour.get():0>2}' + ':' + f'{var_minute.get():0>2}' + ':' + f'{var_second.get():0>2}' \

    try:
        if(combobox_action.get()=="Get device IP"):
            payload = {
                'path':'/device/ethernets',
                'method':'GET',
                'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
            }
        elif(combobox_action.get()=='Get cellular status'):
            payload = {
                'path':'/device/cellulars',
                'method':'GET',
                'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
            }
        elif(combobox_action.get()=='Get device general info'):
            payload = {
                'path':'/device/general',
                'method':'GET',
                'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],    
            }
        elif(combobox_action.get()=='Get DLM cloud status'):
            payload = {
                'path':'/dlm',
                'method':'GET',
                'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],    
            }
        elif(combobox_action.get()=='Get apps status'):
            payload = {
                'path':'/apps',
                'method':'GET',
                'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],    
            }
        elif(combobox_action.get()=='Get Modbus value'):
            
            if(radioValue_slavetype.get()==0):
                    prvdName = 'modbus_tcp_master'
            elif(radioValue_slavetype.get()==1):
                    prvdName = 'modbus_serial_master'

            if(len(var_srcName.get())!=0 and len(var_tagName.get())!=0):
                payload = {
                    'path':'/modbusmaster/operate/direct-read-tag',
                    'method':'PUT',
                    'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                    'requestBody':{'prvdName':f'{prvdName}','srcName':f'{var_srcName.get()}','tagName':f'{var_tagName.get()}'}
                }
            else:
                tk.messagebox.showwarning(title='Warning', message='Device name and tag name shouldn\'t be empty ')
        
        elif(combobox_action.get()=='Others'):
            
            if(radioValue.get()==0):
                request_method = 'GET'
            elif(radioValue.get()==1):
                request_method = 'PUT'
            
            if(len(varAction.get())!=0):
                if(len(var_key_1.get())==0 and len(var_key_2.get())==0 and len(var_key_3.get())==0 and len(var_key_4.get())==0 \
                    and len(var_key_5.get())==0): \
                    payload = {
                        'path':f'{varAction.get()}',
                        'method':f'{request_method}',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}]
                    }
                elif(len(var_key_1.get())!=0 and len(var_key_2.get())==0 and len(var_key_3.get())==0 and len(var_key_4.get())==0 \
                    and len(var_key_5.get())==0): \
                    payload = {
                        'path':f'{varAction.get()}',
                        'method':f'{request_method}',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{f'{var_key_1.get()}':f'{var_value_1.get()}'}
                    }
                elif(len(var_key_1.get())!=0 and len(var_key_2.get())!=0 and len(var_key_3.get())==0 and len(var_key_4.get())==0 \
                    and len(var_key_5.get())==0): \
                    payload = {
                        'path':f'{varAction.get()}',
                        'method':f'{request_method}',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{f'{var_key_1.get()}':f'{var_value_1.get()}',f'{var_key_2.get()}':f'{var_value_2.get()}'}
                    }
                elif(len(var_key_1.get())!=0 and len(var_key_2.get())!=0 and len(var_key_3.get())!=0 and len(var_key_4.get())==0 \
                    and len(var_key_5.get())==0): \
                    payload = {
                        'path':f'{varAction.get()}',
                        'method':f'{request_method}',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{f'{var_key_1.get()}':f'{var_value_1.get()}',f'{var_key_2.get()}':f'{var_value_2.get()}'\
                            ,f'{var_key_3.get()}':f'{var_value_3.get()}'} \
                    }
                elif(len(var_key_1.get())!=0 and len(var_key_2.get())!=0 and len(var_key_3.get())!=0 and len(var_key_4.get())!=0 \
                    and len(var_key_5.get())==0): \
                    payload = {
                        'path':f'{varAction.get()}',
                        'method':f'{request_method}',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{f'{var_key_1.get()}':f'{var_value_1.get()}',f'{var_key_2.get()}':f'{var_value_2.get()}'\
                            ,f'{var_key_3.get()}':f'{var_value_3.get()}',f'{var_key_4.get()}':f'{var_value_4.get()}'} \
                    }
                elif(len(var_key_1.get())!=0 and len(var_key_2.get())!=0 and len(var_key_3.get())!=0 and len(var_key_4.get())!=0 \
                    and len(var_key_5.get())!=0): \
                    payload = {
                        'path':f'{varAction.get()}',
                        'method':f'{request_method}',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{f'{var_key_1.get()}':f'{var_value_1.get()}',f'{var_key_2.get()}':f'{var_value_2.get()}'\
                            ,f'{var_key_3.get()}':f'{var_value_3.get()}',f'{var_key_4.get()}':f'{var_value_4.get()}' \
                            ,f'{var_key_5.get()}':f'{var_value_5.get()}'} \
                    }
                else:
                    print('error')
            else:
               tk.messagebox.showwarning(title='Warning', message='API endpoint shouldn\'t be empty ')

        elif(combobox_action.get()=='Write Modbus value'):
            if(radioValue_slavetype.get()==0):
                prvdName = 'modbus_tcp_master'
            elif(radioValue_slavetype.get()==1):
                prvdName = 'modbus_serial_master'

            if(len(var_srcName.get())!=0 and len(var_tagName.get())!=0 and len(var_tagtype.get())!=0 and len(var_tagvalue.get())!=0):
                

                #Determine the data value type

                int_type = ['boolean','int8','int16','int32','int64','uint8' \
                       ,'uint16','uint32','uint64']     \

                float_type = ['float','double']
                           
                if(f'{var_tagtype.get()}' in int_type):
                    payload = {
                        'path':'/modbusmaster/operate/direct-write-tag',
                        'method':'PUT',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{'prvdName':f'{prvdName}','srcName':f'{var_srcName.get()}','tagName':f'{var_tagName.get()}'\
                                    ,'dataType':f'{var_tagtype.get()}','dataValue':int(f'{var_tagvalue.get()}')} \
                    }
                elif(f'{var_tagtype.get()}' in float_type):
                    payload = {
                        'path':'/modbusmaster/operate/direct-write-tag',
                        'method':'PUT',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{'prvdName':f'{prvdName}','srcName':f'{var_srcName.get()}','tagName':f'{var_tagName.get()}'\
                                    ,'dataType':f'{var_tagtype.get()}','dataValue':float(f'{var_tagvalue.get()}')} \
                    }
                else:
                    payload = {
                        'path':'/modbusmaster/operate/direct-write-tag',
                        'method':'PUT',
                        'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                        'requestBody':{'prvdName':f'{prvdName}','srcName':f'{var_srcName.get()}','tagName':f'{var_tagName.get()}'\
                                    ,'dataType':f'{var_tagtype.get()}','dataValue':(f'{var_tagvalue.get()}')} \
                    }

            else:
                tk.messagebox.showwarning(title='Warning', message='Device name, tag name, data type and value shouldn\'t be empty ')

        elif(combobox_action.get()=='System Reboot'): 
            payload = {
                'path':'/system/reboot',
                'method':'PUT',
                'headers':[{'request-expired-time':f'{varTime}'},{'request-id':f'{varId.get()}'}],
                'requestBody':{'now':bool('true')}
            }

        else:
            payload = {'NO Data'}

        txt.insert('insert',json.dumps(payload)+'\n\n')
    except Exception as e:
        txt.insert('insert','Input Data Error - Please fill in all the argument'+'\n\n')
        print(e)
        

def text_greyedout(event):
    if(combobox_action.get()=='Get Modbus value'):
        ent_tagName['state'] = tk.NORMAL
        ent_srcName['state'] = tk.NORMAL
        rdioTCP['state'] = tk.NORMAL
        rdioRTU['state'] = tk.NORMAL

        ent_tagtype['state'] = tk.DISABLED
        ent_tagvalue['state'] = tk.DISABLED

        ent_key_1['state'] = tk.DISABLED
        ent_value_1['state'] = tk.DISABLED
        ent_key_2['state'] = tk.DISABLED
        ent_value_2['state'] = tk.DISABLED
        ent_key_3['state'] = tk.DISABLED
        ent_value_3['state'] = tk.DISABLED
        ent_key_4['state'] = tk.DISABLED
        ent_value_4['state'] = tk.DISABLED
        ent_key_5['state'] = tk.DISABLED
        ent_value_5['state'] = tk.DISABLED
        
    elif(combobox_action.get()=='Write Modbus value'):
        ent_tagName['state'] = tk.NORMAL
        ent_srcName['state'] = tk.NORMAL
        ent_tagtype['state'] = tk.NORMAL
        ent_tagvalue['state'] = tk.NORMAL
        ent_key_1['state'] = tk.DISABLED
        ent_value_1['state'] = tk.DISABLED
        ent_key_2['state'] = tk.DISABLED
        ent_value_2['state'] = tk.DISABLED
        ent_key_3['state'] = tk.DISABLED
        ent_value_3['state'] = tk.DISABLED
        ent_key_4['state'] = tk.DISABLED
        ent_value_4['state'] = tk.DISABLED
        ent_key_5['state'] = tk.DISABLED
        ent_value_5['state'] = tk.DISABLED
        rdioTCP['state'] = tk.NORMAL
        rdioRTU['state'] = tk.NORMAL

    elif(combobox_action.get()=='Others'):
        entaction['state'] = tk.NORMAL
        rdioGet['state'] = tk.NORMAL
        rdioPut['state'] = tk.NORMAL
        ent_key_1['state'] = tk.NORMAL
        ent_value_1['state'] = tk.NORMAL
        ent_key_2['state'] = tk.NORMAL
        ent_value_2['state'] = tk.NORMAL
        ent_key_3['state'] = tk.NORMAL
        ent_value_3['state'] = tk.NORMAL
        ent_key_4['state'] = tk.NORMAL
        ent_value_4['state'] = tk.NORMAL
        ent_key_5['state'] = tk.NORMAL
        ent_value_5['state'] = tk.NORMAL

        ent_tagName['state'] = tk.DISABLED
        ent_srcName['state'] = tk.DISABLED
        ent_tagtype['state'] = tk.DISABLED
        ent_tagvalue['state'] = tk.DISABLED
        rdioTCP['state'] = tk.DISABLED
        rdioRTU['state'] = tk.DISABLED

    
    else:
        ent_tagName['state'] = tk.DISABLED
        ent_srcName['state'] = tk.DISABLED
        ent_tagtype['state'] = tk.DISABLED
        ent_tagvalue['state'] = tk.DISABLED

        entaction['state'] = tk.DISABLED
        rdioGet['state'] = tk.DISABLED
        rdioPut['state'] = tk.DISABLED
        rdioTCP['state'] = tk.DISABLED
        rdioRTU['state'] = tk.DISABLED
        ent_key_1['state'] = tk.DISABLED
        ent_value_1['state'] = tk.DISABLED
        ent_key_2['state'] = tk.DISABLED
        ent_value_2['state'] = tk.DISABLED
        ent_key_3['state'] = tk.DISABLED
        ent_value_3['state'] = tk.DISABLED
        ent_key_4['state'] = tk.DISABLED
        ent_value_4['state'] = tk.DISABLED
        ent_key_5['state'] = tk.DISABLED
        ent_value_5['state'] = tk.DISABLED

def clear_message():
    txt.delete('1.0','end')


def help_window():
    help_window = tk.Toplevel(window)
    help_window.geometry('480x180+560+200')
    help_window.title('HELP')
    help_window.resizable(0, 0)
    api_document_label = tk.Label(help_window, text = "Online API Document", justify=tk.LEFT, width=150, anchor=tk.W)
    api_document_label.place(x=20, y=10, width = 200, height = 20)

    api_url_label = tk.Label(help_window, text = "https://thingspro-edge.moxa.online/v2.1.0/thingspro-agent/index.html", justify=tk.LEFT, width=400, anchor=tk.W, relief='groove')
    api_url_label.place(x=20, y=30, width = 450, height = 20)

    author_label = tk.Label(help_window, text = "Author", justify=tk.LEFT, width=50, anchor=tk.W)
    author_label.place(x=20, y=70, width = 450, height = 20)

    author_name_label = tk.Label(help_window, text = "Curtis CY Huang, MOXA Asia Pacfic and Taiwan", justify=tk.LEFT, width=50, anchor=tk.W, relief='groove')
    author_name_label.place(x=20, y=90, width = 450, height = 20)

    email_label = tk.Label(help_window, text = "Report Issue/Feedback E-mail", justify=tk.LEFT, width=50, anchor=tk.W)
    email_label.place(x=20, y=130, width = 450, height = 20)

    myemail_label = tk.Label(help_window, text = "curtiscy.huang@moxa.com", justify=tk.LEFT, width=50, anchor=tk.W, relief='groove')
    myemail_label.place(x=20, y=150, width = 450, height = 20)

def save_message():

    #window.withdraw()
    dirname = tk.filedialog.askdirectory(parent=window,initialdir="/",title='Please select a directory')
    if (len(dirname)!=0):
        with open(f'{dirname}'+'/message.txt', 'w') as file:
            file.write(txt.get('1.0', 'end'))
            tk.messagebox.showinfo(title='Save File', message='File has been saved to '+f'{dirname}'+'/message.txt')
            

#Define Window Size
window = tk.Tk()
window.title('ThingsPro Edge Remote Control Command Generator')
window.geometry('840x720+400+20') #Window size 840x720 + _to the left + _to the top
window.resizable(0, 0)

#Menu bar
menubar = Menu(window)
help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help)
help.add_command(label ='About software', command = help_window)


#Define Action combobox
labName_action = tk.Label(window, text = 'Choose the command to invoke action: ', justify=tk.LEFT, width=150, anchor=tk.W)
labName_action.place(x=20, y=10, width=250, height=20)

request_action = ('Get device IP','Get device general info','Get cellular status','Get DLM cloud status','Get apps status'\
    ,'Get Modbus value','Write Modbus value','System Reboot','Others')\

combobox_action = tt.Combobox(window, width=100, values=request_action)
combobox_action.place(x=300, y=10, width=250, height=20)
combobox_action.current(0)

combobox_action.bind("<<ComboboxSelected>>", text_greyedout)

#Define API Endpoint
labName_otheraction = tk.Label(window, text = 'API Endpoint: (Others only)', justify=tk.LEFT, width=150, anchor=tk.W)
labName_otheraction.place(x=20, y=40, width=250, height=20)

varAction = tk.StringVar()
entaction = tk.Entry(window, width = 120, textvariable = varAction, state=tk.DISABLED)
entaction.place(x=300, y=40, width=250, height=20)


#radio button - GET/PUT
radioValue = tk.IntVar() 

rdioGet = tk.Radiobutton(window, text='GET', variable=radioValue, value=0, state=tk.DISABLED) 
rdioPut = tk.Radiobutton(window, text='PUT', variable=radioValue, value=1, state=tk.DISABLED) 
rdioGet.place(x=300, y=80, width=40, height=20)
rdioPut.place(x=380, y=80, width=40, height=20)

#Define Command Expired time
labName_time = tk.Label(window, text = 'Command expired time (Y-M-D H:M:S): ', justify=tk.LEFT, width=100, anchor=tk.W)
labName_time.place(x=20, y=120, width=300, height=20)

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
dt_string_year = dt_string[0:4]
dt_string_month = dt_string[5:7]
dt_string_date = dt_string[8:10]
dt_string_hour = dt_string[11:13]
dt_string_minute = dt_string[14:16]
dt_string_second = dt_string[17:19]

#Define time spinbox

var_year = tk.StringVar(window)
var_year.set(f'{dt_string_year}')
year = tk.Spinbox(window, from_=1, to=9999, textvariable=var_year)
year.place(x=300, y=120, width=50, height=20)

var_month = tk.StringVar(window)
var_month.set(f'{dt_string_month}')
month = tk.Spinbox(window, from_=1, to=12, textvariable=var_month)
month.place(x=360, y=120, width=30, height=20)

var_date = tk.StringVar(window)
var_date.set(f'{dt_string_date}')
date = tk.Spinbox(window, from_=1, to=31, textvariable=var_date)
date.place(x=400, y=120, width=30, height=20)

var_hour = tk.StringVar(window)
var_hour.set(f'{dt_string_hour}')
hour = tk.Spinbox(window, from_=0, to=60, textvariable=var_hour)
hour.place(x=440, y=120, width=30, height=20)

var_minute = tk.StringVar(window)
var_minute.set(f'{dt_string_minute}')
minute = tk.Spinbox(window, from_=0, to=60, textvariable=var_minute)
minute.place(x=480, y=120, width=30, height=20)

var_second = tk.StringVar(window)
var_second.set(f'{dt_string_second}')
second = tk.Spinbox(window, from_=0, to=60, textvariable=var_second)
second.place(x=520, y=120, width=30, height=20)

#Define Task ID
labName_Id = tk.Label(window, text = 'Task id: ', justify=tk.LEFT, width=100, anchor=tk.W)
labName_Id.place(x=20, y=150, width=300, height=20)

varId = tk.Spinbox(window, from_= 1, to = 999)
varId.place(x=300, y=150, width=50, height=20)

#Define Payload parameters
labName_payload_parameters = tk.Label(window, text = 'Modbus Related Command Parameters', justify=tk.LEFT, width=100, anchor=tk.W, relief='groove')
labName_payload_parameters.place(x=20, y=200, width=240, height=20)

#Define Modbus slave type (Modbus TCP Device or Modbus RTU device)
labName_srcName = tk.Label(window, text = 'Modbus slave device type (TCP/RTU): ', justify=tk.LEFT, width=100, anchor=tk.W)
labName_srcName.place(x=20, y=230, width=300, height=20)

#radio button - TCP/RTU
radioValue_slavetype = tk.IntVar() 

rdioTCP = tk.Radiobutton(window, text='TCP', variable=radioValue_slavetype, value=0, state=tk.DISABLED) 
rdioRTU = tk.Radiobutton(window, text='RTU', variable=radioValue_slavetype, value=1, state=tk.DISABLED) 
rdioTCP.place(x=300, y=230, width=40, height=20)
rdioRTU.place(x=380, y=230, width=40, height=20)

#Define Modbus device name
labName_srcName = tk.Label(window, text = 'Modbus device name: ', justify=tk.LEFT, width=100, anchor=tk.W)
labName_srcName.place(x=20, y=260, width=300, height=20)

var_srcName = tk.StringVar()
ent_srcName = tk.Entry(window, width = 120, textvariable = var_srcName, state=tk.DISABLED)
ent_srcName.place(x=300, y=260, width=150, height=20)

#Define Modbus tag name
labName_tagName = tk.Label(window, text = 'Modbus tag name: ', justify=tk.LEFT, width=100, anchor=tk.W)
labName_tagName.place(x=20, y=300, width=300, height=20)

var_tagName = tk.StringVar()
ent_tagName = tk.Entry(window, width = 120, textvariable = var_tagName, state=tk.DISABLED)
ent_tagName.place(x=300, y=300, width=150, height=20)

#Define Modbus tag type
labName_tagtype = tk.Label(window, text = 'Modbus tag data type: ', justify=tk.LEFT, width=100, anchor=tk.W)
labName_tagtype.place(x=20, y=340, width=300, height=20)

var_tagtype = tk.StringVar()
ent_tagtype = tk.Entry(window, width = 120, textvariable = var_tagtype, state=tk.DISABLED)
ent_tagtype.place(x=300, y=340, width=150, height=20)

#Define Modbus tag value
labName_tagvalue = tk.Label(window, text = 'Desired value of the Modbus tags: ', justify=tk.LEFT, width=100, anchor=tk.W)
labName_tagvalue.place(x=20, y=380, width=300, height=20)

var_tagvalue = tk.StringVar()
ent_tagvalue = tk.Entry(window, width = 120, textvariable = var_tagvalue, state=tk.DISABLED)
ent_tagvalue.place(x=300, y=380, width=150, height=20)


#Define other API endpoint key and value parameters
labName_payload_parameters = tk.Label(window, text = 'Others API Endpoint key and values', justify=tk.LEFT, width=100, anchor=tk.W, relief='groove')
labName_payload_parameters.place(x=500, y=200, width=210, height=20)

#Others - key and value

labName_key = tk.Label(window, text = 'Key', justify=tk.LEFT, width=100, anchor=tk.W)
labName_key.place(x=500, y=230, width=300, height=20)

labName_value = tk.Label(window, text = 'Value', justify=tk.LEFT, width=100, anchor=tk.W)
labName_value.place(x=660, y=230, width=300, height=20)


var_key_1 = tk.StringVar()
ent_key_1 = tk.Entry(window, width = 120, textvariable = var_key_1, state=tk.DISABLED)
ent_key_1.place(x=500, y=260, width=150, height=20)

var_value_1 = tk.StringVar()
ent_value_1 = tk.Entry(window, width = 120, textvariable = var_value_1, state=tk.DISABLED)
ent_value_1.place(x=660, y=260, width=150, height=20)

var_key_2 = tk.StringVar()
ent_key_2 = tk.Entry(window, width = 120, textvariable = var_key_2, state=tk.DISABLED)
ent_key_2.place(x=500, y=300, width=150, height=20)

var_value_2 = tk.StringVar()
ent_value_2 = tk.Entry(window, width = 120, textvariable = var_value_2, state=tk.DISABLED)
ent_value_2.place(x=660, y=300, width=150, height=20)

var_key_3 = tk.StringVar()
ent_key_3 = tk.Entry(window, width = 120, textvariable = var_key_3, state=tk.DISABLED)
ent_key_3.place(x=500, y=340, width=150, height=20)

var_value_3 = tk.StringVar()
ent_value_3 = tk.Entry(window, width = 120, textvariable = var_value_3, state=tk.DISABLED)
ent_value_3.place(x=660, y=340, width=150, height=20)

var_key_4 = tk.StringVar()
ent_key_4 = tk.Entry(window, width = 120, textvariable = var_key_4, state=tk.DISABLED)
ent_key_4.place(x=500, y=380, width=150, height=20)

var_value_4 = tk.StringVar()
ent_value_4 = tk.Entry(window, width = 120, textvariable = var_value_4, state=tk.DISABLED)
ent_value_4.place(x=660, y=380, width=150, height=20)

var_key_5 = tk.StringVar()
ent_key_5 = tk.Entry(window, width = 120, textvariable = var_key_5, state=tk.DISABLED)
ent_key_5.place(x=500, y=420, width=150, height=20)

var_value_5 = tk.StringVar()
ent_value_5 = tk.Entry(window, width = 120, textvariable = var_value_5, state=tk.DISABLED)
ent_value_5.place(x=660, y=420, width=150, height=20)

#Generate message payload
btnAdd = tk.Button(window, text='Generate', width=40, command=message_payload)
btnAdd.place(x=300, y=460, width=150, height=20)

#Clear Message
btnClear = tk.Button(window, text='Clear', width=40, command=clear_message)
btnClear.place(x=500,y=460, width=150, height=20)

#Save Message to file
btnSave = tk.Button(window, text='Save', width=40, command=save_message)
btnSave.place(x=660,y=460, width=150, height=20)

#Show payload
labName_payload = tk.Label(window, text = 'Request Command Message', justify=tk.LEFT, width=200, anchor=tk.W, relief='groove')
labName_payload.place(x=20, y=460, width=170, height=20)

#Text box
txt = scrolledtext.ScrolledText(window, undo=True)
txt['font'] = ('arial', '8')
txt.place(x=20, y=500, width=800, height=200)

#Show menu bar
window.config(menu = menubar)

window.mainloop()
