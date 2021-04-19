import wx
from ex4 import StringFormatter

class MyFrame(wx.Frame):
    def __init__(self, parent, title, style):
        super().__init__(parent, title=title, size=(500, 400), style=style)
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        f_box = wx.BoxSizer(wx.HORIZONTAL)

        st_string = wx.StaticText(panel, label='Строка:')
        tc_string = wx.TextCtrl(panel, style=wx.TE_CENTER)
        
        f_box.Add(st_string, flag=wx.RIGHT, border=50)
        f_box.Add(tc_string, proportion=1, flag=wx.RIGHT, border=10)
        
        vbox.Add(f_box, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=30)
        panel.SetSizer(vbox)
        self.Show()

app = wx.App()
no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) 
frame = MyFrame(None, 'wxPython', style=no_resize)
app.MainLoop()

