import yfinance as yf
import matplotlib.pyplot as plt
import datetime

current_date = datetime.date.today()
week_before = datetime.date.today() - datetime.timedelta(days=30)

data = yf.download('SBER.ME', week_before, current_date)
# print(data['Adj Close'])
data['Adj Close'].plot()
plt.title('SBER')
# plt.savefig('sberbank.png', transparent=True)
plt.show()