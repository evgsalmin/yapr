import datetime as dt


date_format = '%d.%m.%Y'


class Record:
    def __init__(self, amount:float, comment:str, date):
        self.amount=amount
        self.comment=comment
        self.date=date


class Calculator:
    def __init__(self, limit: int):
        self.limit = limit
        self.records=[]

    def add_record(self, record: Record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats=0
        now=dt.datetime.now()
        today=now.date()
        for record in self.records:
            moment = dt.datetime.strptime(record.date, date_format)
            day = moment.date()
            if day==today:
                today_stats+=record.amount
        print(f'сегодня {today} потрачено {today_stats}')
        return(today_stats)
        
    def get_week_stats(self):
        week_stats=0
        now=dt.datetime.now()
        today=now.date()
        delta=dt.timedelta(7)
        week_ago=today-delta
        for record in self.records:
            moment = dt.datetime.strptime(record.date, date_format)
            day = moment.date()
            if (day<=today) & (day>=week_ago):
                week_stats+=record.amount
        print(f'за неделю {week_ago} - {today} потрачено {week_stats}')


class CashCalculator(Calculator):
    def get_today_cash_remained(self):
        remained=self.limit-self.get_today_stats()
        print(f'сегодня осталось {remained} денег')



class CaloriesCalculator(Calculator):
    def get_today_calories_remained(self):
        remained=self.limit-self.get_today_stats()
        print(f'сегодня еще можно съесть {remained} еды')


cash_calculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(1000)


r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
r2 = Record(amount=1568,
            comment='Наполнение потребительской корзины',
            date='17.05.2024')
r3 = Record(amount=691, comment='Катание на такси', date='19.05.2024')

r4 = Record(amount=1186,
            comment='Кусок тортика. И ещё один.',
            date='24.02.2019')
r5 = Record(amount=84, comment='Йогурт.', date='17.05.2024')
r6 = Record(amount=1140, comment='Баночка чипсов.', date='19.05.2024')

cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)
calories_calculator.add_record(r4)
calories_calculator.add_record(r5)
calories_calculator.add_record(r6)

cash_calculator.get_today_cash_remained()