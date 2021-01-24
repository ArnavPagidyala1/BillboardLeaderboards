from bs4 import BeautifulSoup
import requests

class Billboard():
    def hot100():
        results = []
        
        url = 'https://www.billboard.com/charts/hot-100'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        chart = soup.find(class_="chart-list__elements")
        topFive = chart.find_all("li")[:5]

        for i in range(len(topFive)):
            name = topFive[i].find(class_="chart-element__information__artist").text
            song = topFive[i].find(class_="chart-element__information__song").text
            results.append(song + " by " + name)
        
        return results

    def billboard200():
        results = []

        url = 'https://www.billboard.com/charts/billboard-200'

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        chart = soup.find(class_="chart-list__elements")
        topFive = chart.find_all("li")[:5]

        for i in range(len(topFive)):
            name = topFive[i].find(class_="chart-element__information__artist").text
            song = topFive[i].find(class_="chart-element__information__song").text
            results.append(song + " by " + name)
        
        return results

    def billboardGlobal200():
        results = []
        
        url = 'https://www.billboard.com/charts/billboard-global-200'

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        chart = soup.find(class_="chart-list__elements")
        topFive = chart.find_all("li")[:5]

        for i in range(len(topFive)):
            name = topFive[i].find(class_="chart-element__information__artist").text
            song = topFive[i].find(class_="chart-element__information__song").text
            results.append(song + " by " + name)
        
        return results

    def artist100():
        results = []

        url = 'https://www.billboard.com/charts/artist-100'

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        chart = soup.find(class_="chart-list")
        topFive = chart.find_all(class_="chart-list-item__text-wrapper")[:5]

        for i in range(len(topFive)):
            name = topFive[i].find(class_="chart-list-item__title-text").text.strip()
            results.append(name)
        
        return results
