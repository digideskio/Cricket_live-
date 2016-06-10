class Article():

    def __init__(self):
        self.headline = None
        self.author = None
        self.date = None
        self.imageURL = None
        self.content = None


    def getArticle(self, section):

        head = section.text
        list =[]
        self.headline = section.find('h1', {'class': 'col-1-1'}).text
        self.author = section.find('span', {'class': 'author-name'}).text
        self.date = section.find('span', {'class': 'date'}).get_text()

        main_content = section.find('section', {'class': 'story-content-main'})
        content = ''

        for contents in main_content.find_all('p', {'class': ''}):

            content = content + contents.text.replace('\n', '')
            # print content
        self.content = content

        try:
            imagesrc = section.figure
            self.imageURL = "http://www.espncricinfo.com"+ imagesrc.find_next("img").attrs['src']
        except:
            self.imageURL = None
            return



