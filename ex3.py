import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        vbox = wx.BoxSizer()
        list_box = wx.ListBox(self, wx.ID_ANY, style=wx.LB_SINGLE)
        vbox.Add(list_box, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(vbox)

class MyMenu(wx.MenuBar):
    def __init__(self):
        super().__init__()

        file_menu = wx.Menu()
        log_menu = wx.Menu()

        file_menu.Append(wx.ID_ANY, 'Открыть\tCtrl+O')
        log_menu.Append(wx.ID_ANY, 'Экспорт\tCtrl+E')
        log_menu.Append(wx.ID_ANY, 'Добавить в лог\tCtrl+A')
        log_menu.Append(wx.ID_ANY, 'Просмотр\tCtrl+S')

        self.Append(file_menu, 'Файл')
        self.Append(log_menu, 'Лог')

class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent, size=size, title=title)

        menubar = MyMenu()
        self.SetMenuBar(menubar)

        panel = MyPanel(self)

        status_bar = self.CreateStatusBar(2)
        status_bar.SetStatusWidths([-6, -4])
        status_bar.SetStatusText('Some Text')
        status_bar.SetStatusText('Some Text2', 1)

        self.Show()
        
app = wx.App()
frame = MyFrame(None, 'Искатель строк', size=(600, 400))
app.MainLoop()
