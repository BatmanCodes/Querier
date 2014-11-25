#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class demo(wx.Frame):

  def __init__(self, parent, title):
    super(demo, self).__init__(parent, title=title, size=(600,700))

    self.InitUI()
    self.Centre()
    self.Show()

  def InitUI(self):
    panel = wx.Panel(self)

    font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
    font.SetPointSize(9)    

    vbox = wx.BoxSizer(wx.VERTICAL)

    #control.SetPosition((100,100))
    #vbox.Add(control, flag=wx.TOP, border=100)

    hbox1 = wx.BoxSizer(wx.HORIZONTAL)
    st1 = wx.StaticText(panel, label='Name')
    st1.SetFont(font)
    hbox1.Add(st1, flag=wx.RIGHT, border=8)
    tc = wx.TextCtrl(panel, -1, "Jain Nishank N.")
    hbox1.Add(tc, proportion=1)
    vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
    
    hbox2 = wx.BoxSizer(wx.HORIZONTAL)
    st2 = wx.StaticText(panel, label='Branch')
    st2.SetFont(font)
    hbox2.Add(st2, flag=wx.RIGHT, border=8)
    tc = wx.TextCtrl(panel, -1, "Electronics & Communication Engineering")
    hbox2.Add(tc, proportion=1)
    vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
    
    hbox3 = wx.BoxSizer(wx.HORIZONTAL)
    st3 = wx.StaticText(panel, label='Year')
    st3.SetFont(font)
    hbox3.Add(st3, flag=wx.RIGHT, border=8)
    tc = wx.TextCtrl(panel, -1, "2")
    hbox3.Add(tc, proportion=0)
    st4 = wx.StaticText(panel, label='Enrollment No.')
    st4.SetFont(font)
    hbox3.Add(st4, flag=wx.RIGHT|wx.LEFT, border=8)
    tc = wx.TextCtrl(panel, -1, "13116033")
    hbox3.Add(tc, proportion=0)
    vbox.Add(hbox3, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)

    hbox4 = wx.BoxSizer(wx.HORIZONTAL)
    st5 = wx.StaticText(panel, label='E-mail')
    st5.SetFont(font)
    hbox4.Add(st5, flag=wx.RIGHT, border=8)
    tc = wx.TextCtrl(panel, -1, "nishankj96@gmail.com")
    hbox4.Add(tc, proportion=1)
    vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

    hbox5 = wx.BoxSizer(wx.HORIZONTAL)
    st6 = wx.StaticText(panel, label='Room No.')
    st6.SetFont(font)
    hbox5.Add(st6, flag=wx.RIGHT, border=8)
    tc = wx.TextCtrl(panel, -1, "654")
    hbox5.Add(tc, proportion=0)
    st7 = wx.StaticText(panel, label='Contact No.')
    st7.SetFont(font)
    hbox5.Add(st7, flag=wx.LEFT|wx.RIGHT, border=8)
    tc = wx.TextCtrl(panel, -1, "9756574995")
    hbox5.Add(tc, proportion=0)
    vbox.Add(hbox5, flag=wx.LEFT|wx.RIGHT|wx.TOP, border=10)
    panel.SetSizer(vbox)

    filepath = 'C:\Users\DELL\Desktop\\nish.png'

    img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
    W = img.GetWidth()
    H = img.GetHeight()
    if W > H:
      NewW = 400
      NewH = 400 * H / W
    else:
      NewH = 400
      NewW = 400 * W / H
    img = img.Scale(NewW,NewH)
    imgBitmap = wx.BitmapFromImage(img)
    control = wx.StaticBitmap(self, -1, imgBitmap)        
    imgc = app.ImageCtrl(panel, -1, control)
    vbox.Add(imgc, proportion=0)

if __name__ == '__main__':
  app = wx.App()
  app.PhotoMaxSize = 500
  demo(None, title='Querier')
  app.MainLoop()