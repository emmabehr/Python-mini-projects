# May need to install the wx module using pip
# pip install wxPython or python3 -m pip install wxPython

import wx

counter = 0
def OnUpdate(event):
    global counter, label
    counter += 1
    label.SetLabel(str(counter))

app = wx.App()

frame = wx.Frame(None, wx.ID_ANY, "Simple Counter") # A Frame is a top-level window.

sizer = wx.BoxSizer(wx.VERTICAL)

label = wx.StaticText(frame, label=str(counter))
button = wx.Button(frame, wx.ID_APPLY, "Update Counter")
frame.Bind(wx.EVT_BUTTON, OnUpdate, button)

sizer.Add(label, 0, wx.EXPAND)
sizer.Add(button, 0, wx.EXPAND)

frame.SetSizer(sizer)
frame.SetAutoLayout(1)
sizer.Fit(frame)

frame.Show(True)
app.MainLoop()