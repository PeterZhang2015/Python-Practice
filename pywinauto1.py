from pywinauto import application


application_name = "Notepad.exe"
app = application.Application.start(application_name)

app.Notepad.MenuSelect("Help->About Notepad")
app.AboutNotepad.OK.Click()
app.Notepad.MenuSelect("File->Exit")