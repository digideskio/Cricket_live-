class Get_comm(object):
    def __init__(self):
        self.commentary_overs  = []
        self.commentary_text = []
        self.details = []
        # self.universityURL = None
        # self.imageURL = None

    def getComm(self, data):
        # self.commentary_overs = data.find_all("div",{'class': 'commentary-overs'})
        # for i in data.select('div.commentary-overs'):
        #     self.commentary_overs = i.string
        for i in data.find_all("div",{'class': 'commentary-overs'}):
            self.commentary_overs.append(i.string)

        for i in data.find_all('div',attrs={"class":"commentary-text"}):
            self.commentary_text.append(i.find("p").string)




    def makdict(self, list1, list2):
        for ovr, comm in zip(list1, list2):
            self.details.append({'over': ovr, 'commentry': comm})
