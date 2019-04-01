from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('http://www.puffandpass.co.za/tag/information-technology').text

soup = BeautifulSoup(source, 'lxml')

# Create CSV file with headers
csv_file =  open('pnp_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Summary', 'Post_Link'])

for main in soup.find_all('section', class_ = 'post'):

    try:
        title = main.h2.text
        summary = main.find('section', class_ = 'entry-summary').text
        link = main.h2.a.attrs['href']
    except:
        title = None
        summary = None
        articleLink = None



    print(title)
    print(summary)
    print(link)
    print()
    csv_writer.writerow([title, summary, link])

csv_file.close()
