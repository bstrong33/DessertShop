from typing import Protocol
from enum import Enum

class Payable(Protocol):
    pay_type: str

    def get_pay_type(self):
        if isinstance(self.pay_type, PayType):
            return self.pay_type
        else:
            raise ValueError
    
    def set_pay_type(self, new_pay_type):
        if isinstance(new_pay_type, PayType):
            self.pay_type = new_pay_type
        else:
            raise ValueError

class PayType(Enum):
    CASH = "CASH"
    CARD = "CARD"
    PHONE = "PHONE"