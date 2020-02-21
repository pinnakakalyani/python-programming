from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import time
import xlsxwriter as xlsx

#https://www.flipkart.com/search?q=mobiles&page=2

workbook = xlsx.Workbook("Flipkart_Mobile.xlsx")
worksheet = workbook.add_worksheet("Flipkart Mobiles")
cellRow = 0
cellCol = 0
worksheet.write(cellRow, cellCol, "Mobile Name")
worksheet.write(cellRow, cellCol + 1, "Price")
worksheet.write(cellRow, cellCol + 2, "Rating")
cellRow += 1 

for i in range(1, 2):
    url = "https://www.flipkart.com/search?q=mobiles&page="+str(i)
    uclient = req(url)
    page = uclient.read()
    uclient.close()

    pagesoup = soup(page, 'html.parser')
    allMobileHtml = pagesoup.findAll("div", {"class":"_3wU53n"})
    allMobilePriceHtml = pagesoup.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
    allMobileRatingHtml = pagesoup.findAll("div", {"class":"hGSR34"})
    counter = 0
    while counter < len(allMobileHtml):
        eachtitlediv = allMobileHtml[counter]
        eachtitleprice = allMobilePriceHtml[counter]
        eachtitlerating = allMobileRatingHtml[counter]
        print(str(i) + " Title: " + eachtitlediv.text ) 
        print(str(i) + " Price: " + str(eachtitleprice.text))
        print(str(i) + " Rating: " + str(eachtitlerating.text))
        worksheet.write(cellRow, cellCol, eachtitlediv.text )
        worksheet.write(cellRow, cellCol + 1, eachtitleprice.text)
        worksheet.write(cellRow, cellCol + 2, eachtitlerating.text)
        cellRow += 1 
        counter += 1
    time.sleep(2)
workbook.close()




