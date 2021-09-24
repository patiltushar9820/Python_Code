#Log  in 
import PySimpleGUI as sg
log_in_form = [
    [
        sg.Text("User Name :"),
        sg.In(size=(25, 1), enable_events=True, key="-USER_NM-"),
        
    ],
    [
        sg.Text("Password :"),
        sg.In(size=(25, 1), enable_events=True, key="-PASSWORD-"),
    ],
    [
        sg.Button("Log In "),

        #sg.In(size=(25, 1), enable_events=True, key="-BTN_LOG_IN-"),
    ]]
layout = [
    [
        sg.Column(log_in_form),
    ]
]
window = sg.Window("Log In", layout).read(  )
