import wx
import wx.html
import MySQLdb

class NoEntryException(Exception):
	pass

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
		self.error = wx.TextCtrl(self, -1, "", pos=(200,0), size=(200, 25), style=wx.TE_READONLY)

		self.btn1 = wx.Button(self, -1, "Search", pos=(50,25))
		self.btn1.Bind(wx.EVT_BUTTON, self.OnLoadFile)

		self.btn2 = wx.Button(self, -1, "Clear Page", pos=(120,0))
		self.btn2.Bind(wx.EVT_BUTTON, self.OnClearPage)
	
	def OnLoadFile(self, event):
		enroll_no = self.tc.GetValue()
		print "Search: "+str(enroll_no)
		try:	
			vals = self.query(int(enroll_no))
			self.error.SetValue("")
		except NoEntryException as e:
			self.error.SetValue("Invalid Enrollment No")
			return
		except ValueError:
			self.error.SetValue("Invalid Enrollment No")
			return

		name = vals[2]
		clas = vals[3]
		branch = vals[4]
		room_no = vals[6]
		reg_entry = vals[7]
		mobile_no = vals[8]
		mess_reg = vals[9]
		email = vals[10]
		remark = vals[11]
		image_path = '../'+vals[12]
		fan = vals[13]
		tube_light = vals[14]
		study_table = vals[15]
		tea_table = vals[16]
		hard_bed = vals[17]
		lan = vals[18]

		Template = open('HTMLTemplate.html').read()
		template = Template.replace("{{ enroll_no }}", enroll_no)
		template = template.replace("{{ name }}", name)
		template = template.replace("{{ img }}", image_path)
		template = template.replace("{{ class }}", clas)
		template = template.replace("{{ branch }}", branch)
		template = template.replace("{{ room_no }}", str(room_no))
		template = template.replace("{{ reg_entry }}", reg_entry)
		template = template.replace("{{ mobile_no }}", mobile_no)
		template = template.replace("{{ mess_reg }}", mess_reg)
		template = template.replace("{{ email }}", email)
		template = template.replace("{{ remark }}", remark)
		template = template.replace("{{ fan }}", fan)
		template = template.replace("{{ tube_light }}", tube_light)
		template = template.replace("{{ study_table }}", study_table)
		template = template.replace("{{ tea_table }}", tea_table)
		template = template.replace("{{ hard_bed }}", hard_bed)
		template = template.replace("{{ lan }}", lan)
		self.html1.SetPage(template)

	def OnClearPage(self, event):
		self.html1.SetPage("")

	def query(self, enroll_no):
		db = MySQLdb.connect(host="localhost", # your host, usually localhost
		                     user="querier", # your username
		                     passwd="querier", # your password
		                     db="querier") # name of the data base
		cur = db.cursor()
		query = "SELECT * FROM main WHERE enroll_no = "+str(enroll_no)
		cur.execute(query)
		l = cur.fetchall()
		return l[0]



app = wx.PySimpleApp()
# create a window/frame, no parent, -1 is default ID, title, size
frame = wx.Frame(None, -1, "HtmlWindow()", size=(610, 380))
# call the derived class, -1 is default ID
MyHtmlPanel(frame,-1)
# show the frame
frame.Show(True)
# start the event loop
app.MainLoop()