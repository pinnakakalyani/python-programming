from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import time
import xlsxwriter as xlsx

workbook = xlsx.Workbook("Newyork_times.xlsx")
worksheet = workbook.add_worksheet("World News")
cellRow = 0
cellCol = 0
worksheet.write(cellRow, cellCol, "Date")
worksheet.write(cellRow, cellCol + 1, "Heading")
worksheet.write(cellRow, cellCol + 2, "By")
cellRow += 1 

country=['africa','america','austrila','asia','canada']

for i in country:
    url = "https://www.nytimes.com/section/world/"+str(i)
    uclient = req(url)
    page = uclient.read()
    uclient.close()

    pagesoup = soup(page, 'html.parser')
    allDateHtml = pagesoup.findAll("div", {"class":"css-n1vcs8 e1xfvim33"})
    allHeadingHtml = pagesoup.findAll("div", {"class":"css-79elbk"})
    alByHtml = pagesoup.findAll("div", {"class":"css-n1vcs8 e1xfvim33"})
    print(allDateHtml)
    print(len(allHeadingHtml))
    print(alByHtml)
    counter = 0
    while counter < 6:
        #eachtitlediv = allDateHtml[counter]
        eachtitleheading = allHeadingHtml[counter]
        #eachtitleby = alByHtml[counter]
        #print(str(i) + " Date: " + eachtitlediv.text ) 
        print(str(i) + " HeadLine: " + str(eachtitleheading.text))
        #print(str(i) + " BY: " + str(eachtitleby.text))
        #worksheet.write(cellRow, cellCol, eachtitlediv.text )
        worksheet.write(cellRow, cellCol + 1, eachtitleheading.text)
        #worksheet.write(cellRow, cellCol + 2, eachtitleby.text)
        cellRow += 1 
        counter += 1
    time.sleep(2)
workbook.close()
