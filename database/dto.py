from abc import ABC, abstractmethod
from typing import List, Optional
from dataclasses import dataclass

class BaseSchema(ABC):
    @abstractmethod
    def as_dict(self):
        pass


@dataclass
class POSUserSchema(BaseSchema):
    pos_user_id: int
    pos_user_role: str

    def as_dict(self):
        return {
            "pos_user_id": self.pos_user_id,
            "pos_user_role": self.pos_user_role
        }

@dataclass
class CustomerSchema(BaseSchema):
    customer_id: int
    customer_name: str
    customer_phone_number: Optional[str]
    customer_location: Optional[str]

    def as_dict(self):
        return {
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "customer_phone_number": self.customer_phone_number,
            "customer_location": self.customer_location
        }

@dataclass
class BranchSchema(BaseSchema):
    branch_id: int
    branch_name: str

    def as_dict(self):
        return {
            "branch_id": self.branch_id,
            "branch_name": self.branch_name
        }

@dataclass
class CategorySchema(BaseSchema):
    category_id: int
    category_name: str

    def as_dict(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name
        }

@dataclass
class ItemSchema(BaseSchema):
    item_id: int
    item_name: str
    item_price: float
    category_id: int

    def as_dict(self):
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "item_price": self.item_price,
            "category_id": self.category_id
        }

@dataclass
class BranchStockSchema(BaseSchema):
    branch_stock_id: int
    branch_id: int
    item_id: int
    branch_item_quantity: int

    def as_dict(self):
        return {
            "branch_stock_id": self.branch_stock_id,
            "branch_id": self.branch_id,
            "item_id": self.item_id,
            "branch_item_quantity": self.branch_item_quantity
        }

@dataclass
class BigStockSchema(BaseSchema):
    big_stock_id: int
    item_id: int
    big_stock_quantity: int

    def as_dict(self):
        return {
            "big_stock_id": self.big_stock_id,
            "item_id": self.item_id,
            "big_stock_quantity": self.big_stock_quantity
        }