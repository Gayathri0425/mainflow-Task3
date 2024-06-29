import requests
from bs4 import BeautifulSoup


#uRL of the web page to scrape
url='https://careerfoundry.com/en/blog/data-analytics/web-scraping-guide/'   #Replace with the URL of the web page you want to scrape

#send a GET requests to the web page
response = requests.get(url)

#check if the requests was successful
if response.status_code == 200:
    #parse the HTML contect of the page
    soup = BeautifulSoup(response.text,'html.parser')

    #Extract all the text from the page
    page_text=soup.get_text()

    #Extract all the links from the page
    links =[a['href']for a in soup.find_all('a',href=True)]

    # Extract all the image from the page
    images =[img['src']for img in soup.find_all('img',src=True)]

    # print the extracted data
    print("page Text:")
    print(page_text)

    print("\nlinks:")
    for link in links:
        print(link)

    print("\nImages:")
    for image in images:
        print(image)
else:
    print(f"Failed to retrive the web page.status code:{response.status_code}")        