import requests
from bs4 import BeautifulSoup
from HolidayScraper.email_sender import email_sender
from HolidayScraper.check_similar import similar
from sms_sender import sms_sender
import csv


class WebScraper:

    def __init__(self):
        self.destination_list = ['Dominikana', 'Sri Lanka', 'Meksyk', 'Zanzibar', 'Tanzania', 'Malediwy'
                                                                                              'Wyspy Zielonego Przylądka',
                                 'Kuba', 'Kenia', 'Oman', 'Aruba', 'Bali', 'Indonezja',
                                 'Tajlandia', 'Bangkok', 'Wietnam']

    @staticmethod
    def get_last_list():
        file = open('last.csv')
        reader = csv.reader(file)
        return [tuple(row) for row in reader]

    @staticmethod
    def write_new_line(text, link):
        output_file = open('last.csv', 'a', newline='')
        output_writer = csv.writer(output_file)
        output_writer.writerow([text, link])
        output_file.close()

    def web_scraper_last_minuter(self):
        response = requests.get('https://lastminuter.pl/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            body = soup.body
            last_minuter_result = body.find_all('h2')
            for last in last_minuter_result:
                link = 'https://lastminuter.pl' + last.find('a')['href']
                text = last.find('a').contents[0]
                for destination in self.destination_list:
                    for word in text.split():
                        if similar(destination.lower(), word.lower()) > 0.8:
                            if (text, link) not in self.get_last_list():
                                self.write_new_line(text, link)
                                email_sender(text, link)
                                sms_sender(text, link)
                                print(f"***Nowa oferta!***")
            return 'LastMinuter Check'
        else:
            print("Błąd")

    def web_scraper_fly4free(self):
        response = requests.get('https://fly4free.pl')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            body = soup.body
            fly4free_result = body.find_all('h2', {'class': 'item__title'})
            for last in fly4free_result:
                link = last.find('a')['href']
                text = last.find('a').contents[0]
                for destination in self.destination_list:
                    for word in text.split():
                        if similar(destination.lower(), word.lower()) > 0.8:
                            if (text, link) not in self.get_last_list():
                                self.write_new_line(text, link)
                                email_sender(text, link)
                                sms_sender(text, link)
                                print(f"***Nowa oferta!***")
            return 'Fly4Free Check'
        else:
            print("Błąd")

    def web_scraper_wakacyjni_piraci(self):
        response = requests.get('https://wakacyjnipiraci.pl')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            body = soup.body
            piraci_result = body.find_all('div', {'class': 'hp__sc-1lylu39-1 hPxCnR'})
            for last in piraci_result:
                link = last.find('a')['href']
                text = last.find('span', {'class': 'hp__sc-ro12w0-5 XnFKm'}).contents[0]
                for destination in self.destination_list:
                    for word in text.split():
                        if similar(destination.lower(), word.lower()) > 0.8:
                            if (text, link) not in self.get_last_list():
                                self.write_new_line(text, link)
                                email_sender(text, link)
                                sms_sender(text, link)
                                print(f"***Nowa oferta!***")
            return f'Wakacyjni Piraci Check'
        else:
            print("Błąd")


last = WebScraper()
