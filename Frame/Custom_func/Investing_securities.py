import requests
from bs4 import BeautifulSoup
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
# from ..Investor.settings import BASE_DIR

personal_data = {'email': 'andreyleshko2001@gmail.com', 'password': '12Qwerty'}
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36',
           'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

log_in_email_link = "https://ru.investing.com/members-admin/auth/signInByEmail/"
session = requests.Session()
response = session.post(log_in_email_link, data=personal_data, headers=HEADERS).text
link_my_portfolio = 'https://ru.investing.com/portfolio/?portfolioID=Y281YGAxMWtjM21iNGU%3D'


def portfolio_securities_to_file(): # создаст файл с информацией об избранных акциях
    # итоговый файл, содержит название бумаги, тикер, цену, изменение абсолютное, изменение в %, ссылку
    file = open('inv_securities_list.csv', 'w', encoding='UTF-8')
    r = session.get(link_my_portfolio, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    # таблица с избранными бумагама
    table_my_portfolio = (soup.find('div', class_='wrapper').find('section', id='fullColumn').find('div', class_="allPortfoliosWrapper")
                .find('div', id="portfolioblock_9676632").find('div', class_="cardBlock portfolioCardBlock").find('div', id="portfolioData_9676632")
                .find('div', class_="js-watchlist-content").find('tbody'))
    securities_list = table_my_portfolio.find_all('tr')
    for tr in securities_list:
        name = tr.find('td', class_="symbol plusIconTd left bold elp alert js-injected-user-alert-container").find(
            'span', class_="aqPopupWrapper js-hover-me-wrapper").find('a').text.strip()
        tiker = tr.find('td', class_="left bold").find('a').text.strip()
        cost = tr.find('td', {'data-column-name': "last"}).text.strip()
        change_abs = tr.find('td', {'data-column-name': "chg"}).text.strip()
        change_per = tr.find('td', {'data-column-name': "chgpercent"}).text.strip()
        link = 'https://ru.investing.com' + tr.find('td', class_="left bold").find('a')['href']
        all_data = [name, tiker, cost, change_abs, change_per, link]
        for i in all_data:
            file.write(i)
            file.write('; ')
        file.write('\n')
    file.close()

def security_graph():
    securities = ['AAPL', 'SBER.ME', 'YNDX.ME']
    current_date = datetime.datetime.today()
    start_data = datetime.datetime.today() - datetime.timedelta(days=60)
    for i in securities:
        '''data = yf.download(i, start_data, current_date)
        data['Adj Close'].plot()
        plt.title(i)
        if __name__ == "__main__":
            plt.savefig(f'{i}.png')
        else:
            plt.savefig(f'Securities/static/Security/img/{i}.png')
        '''
        data = yf.download(i, start_data, current_date)
        fig = plt.figure(figsize=(5, 5))
        ax = fig.add_subplot()
        ax.plot(data['Adj Close'], '-m')
        ax.grid()
        plt.xticks(rotation=90)
        # plt.show()
        if __name__ == "__main__":
            plt.savefig(f'{i}.png')
        else:
            plt.savefig(f'Frame/static/Frame/img/{i}.png')



# security_graph()


def portfolio_securities():
    all_securities = []
    r = session.get(link_my_portfolio, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    # таблица с избранными бумагама
    table_my_portfolio = (
        soup.find('div', class_='wrapper').find('section', id='fullColumn').find('div', class_="allPortfoliosWrapper")
        .find('div', id="portfolioblock_9676632").find('div', class_="cardBlock portfolioCardBlock").find('div',
                                                                                                          id="portfolioData_9676632")
        .find('div', class_="js-watchlist-content").find('tbody'))
    securities_list = table_my_portfolio.find_all('tr')
    for tr in securities_list:
        name = tr.find('td', class_="symbol plusIconTd left bold elp alert js-injected-user-alert-container").find(
            'span', class_="aqPopupWrapper js-hover-me-wrapper").find('a').text.strip()
        tiker = tr.find('td', class_="left bold").find('a').text.strip()
        cost = tr.find('td', {'data-column-name': "last"}).text.strip()
        change_abs = tr.find('td', {'data-column-name': "chg"}).text.strip()
        change_per = tr.find('td', {'data-column-name': "chgpercent"}).text.strip()
        link = 'https://ru.investing.com' + tr.find('td', class_="left bold").find('a')['href']
        all_data = [name, tiker, cost, change_abs, change_per, link]
        all_securities.append(all_data)
    # security_graph()
    return all_securities








