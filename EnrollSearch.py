import wx
import wx.html
import MySQLdb

class NoEntryException(Exception):
    pass

class ImageNotFound(Exception):
    pass

class MainPanel(wx.Panel):
    """
    class MainPanel inherits wx.Panel and adds a button and HtmlWindow
    """
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.html1 = wx.html.HtmlWindow(self, id, pos=(0,55), size=(850, 310))
        self.tc = wx.TextCtrl(self, -1, "", pos=(300,5))    
        self.error = wx.TextCtrl(self, -1, "", pos=(300,32), size=(207, 20), style=wx.TE_READONLY|wx.TE_CENTRE)
        self.btn1 = wx.Button(self, -1, "Search", pos=(420,4))
        self.btn1.Bind(wx.EVT_BUTTON, self.OnLoadFile)
    
    def OnLoadFile(self, event):
        enroll_no = self.tc.GetValue()
        print "Search: "+str(enroll_no)
        try:    
            vals = self.query(int(enroll_no))
            self.error.SetValue("")
        except NoEntryException as e:
            self.error.SetValue("Enrollment No does not exist")
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
        try:
            width, height = self.resize(image_path)
        except:
            self.error.SetValue("Image not Found")
            width = 0
            height = 0


        Template = open('HTMLTemplate.html').read()
        template = Template.replace("{{ enroll_no }}", enroll_no)
        template = template.replace("{{ name }}", name)
        template = template.replace("{{ img }}", image_path)
        template = template.replace("{{ height }}", str(height))
        template = template.replace("{{ width }}", str(width))
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

    def resize(self, path):
        try:
            img = wx.Image(path, wx.BITMAP_TYPE_ANY)
        except:
            raise ImageNotFound()
        W = img.GetWidth()
        H = img.GetHeight()
        NewW = 1
        NewH = 1
        if W > H:
            NewW = 240
            NewH = 240 * H / W
        else:
            NewH = 240
            NewW = 240 * W / H
        return (NewW, NewH)

    def query(self, enroll_no):
        db = MySQLdb.connect(host="localhost", # your host, usually localhost
                             user="user_name", # your username
                             passwd="db_password", # your password
                             db="db_name") # name of the data base
        cur = db.cursor()
        query = "SELECT * FROM main WHERE enroll_no = "+str(enroll_no)
        cur.execute(query)
        l = cur.fetchall()
        db.close()
        try:
            return l[0]
        except:
            raise NoEntryException()


app = wx.App()
frame = wx.Frame(None, -1, "Enrollment Search", size=(850, 365), style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
MainPanel(frame,-1)
frame.Show(True)
app.MainLoop()
