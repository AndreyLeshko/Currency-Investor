import yfinance as yf
import matplotlib.pyplot as plt
import datetime

def security_graph():
    securities = ['AAPL', 'SBER.ME', 'YNDX.ME']
    current_date = datetime.datetime.today()
    start_data = datetime.datetime.today() - datetime.timedelta(days=60)
    for i in securities:
        data = yf.download(i, start_data, current_date)
        # data['Adj Close'].plot()
        # plt.title(i)
        fig = plt.figure(figsize=(5,5))
        ax = fig.add_subplot()
        ax.plot(data['Adj Close'], '-m')
        ax.grid()
        plt.xticks(rotation=90)
        # plt.show()
        if __name__ == "__main__":
            plt.savefig(f'{i}.png')
        else:
            plt.savefig(f'Securities/static/Security/img/{i}.png')

security_graph()
