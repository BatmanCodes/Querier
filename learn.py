import wx
import wx.html

name = "Kartik"
enroll_no = "No"
img = "Photo.jpg"
class MyHtmlPanel(wx.Panel):
	"""
	class MyHtmlPanel inherits wx.Panel and adds a button and HtmlWindow
	"""
	def __init__(self, parent, id):
	# default pos is (0, 0) and size is (-1, -1) which fills the frame
		wx.Panel.__init__(self, parent, id)
		# self.SetBackgroundColour("yellow")
		self.html1 = wx.html.HtmlWindow(self, id, pos=(0,50), size=(300, 300))

		self.tc = wx.TextCtrl(self, -1, "")
		# .Add(tc, proportion=1)

		self.btn1 = wx.Button(self, -1, "Load", pos=(50,25))
		self.btn1.Bind(wx.EVT_BUTTON, self.OnLoadFile)

		self.btn2 = wx.Button(self, -1, "Clear Page", pos=(120,0))
		self.btn2.Bind(wx.EVT_BUTTON, self.OnClearPage)
	def OnLoadFile(self, event):
		path = self.tc.GetValue()
		Template = open('E:/Programs and Codes/Work/Querier/HTMLTemplate.html').read()
		template = Template.replace("{{ enroll_no }}", path)
		template = template.replace("{{ name }}", name)
		template = template.replace("{{ img }}", img)
		self.html1.SetPage(template)

	def OnClearPage(self, event):
		self.html1.SetPage("")


app = wx.PySimpleApp()
# create a window/frame, no parent, -1 is default ID, title, size
frame = wx.Frame(None, -1, "HtmlWindow()", size=(610, 380))
# call the derived class, -1 is default ID
MyHtmlPanel(frame,-1)
# show the frame
frame.Show(True)
# start the event loop
app.MainLoop()