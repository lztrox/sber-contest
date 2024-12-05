from decimal import Decimal
from enum import Enum

class AssetPrice(Enum):
    """
    Котированный список активов
    """
    LKOH = Decimal(5896)
    SBER = Decimal(250)

class Portfolio:
    """
    Класс для работы с портфелем
    """
    def __init__(self):
        self.assets = {}

    def buy_asset(self, asset, quantity):
        """
        Метод для покупки активов
        :param asset: выбранный актив
        :param amount: количество активов для покупки
        """
        if asset not in self.assets:
            self.assets[asset] = 0
        self.assets[asset] += quantity

    def sell_asset(self, asset, quantity):
        """
        Метод для продажи активов
        :param asset: выбранный актив
        :param amount: количество активов для продажи
        """
        if asset in self.assets:
            if quantity >= self.assets[asset]:
                del self.assets[asset]
            else:
                self.assets[asset] -= quantity

    def get_portfolio_value(self):
        """
        Метод для получения текущей стоимости портфеля
        :return: текущая стоимость портфеля
        """
        total_value = 0
        for asset, quantity in self.assets.items():
            price = asset.value
            total_value += price * quantity
        return total_value

portfolio = Portfolio()
portfolio.buy_asset(AssetPrice.LKOH, 10)
portfolio.buy_asset(AssetPrice.SBER, 5)
portfolio.sell_asset(AssetPrice.LKOH, 3)
portfolio.sell_asset(AssetPrice.SBER, 2)

portfolio_value = portfolio.get_portfolio_value()
print(f"Текущая стоимость портфеля: {portfolio_value}")