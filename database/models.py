from tokenize import Double
from sklearn.metrics import confusion_matrix
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Double,
    Text,
    SmallInteger,
    DateTime,
    Time,
    Sequence,
    BigInteger,
    Float,
    UniqueConstraint,
    CheckConstraint,
    Index,
    ARRAY,
)
from sqlalchemy.orm import relationship
from database.db import Base
from dataclasses import dataclass
import sys



from sqlalchemy import (
 Column, Integer, String, Float, ForeignKey, DateTime
)
from sqlalchemy.orm import relationship, declarative_base

from database.dto import (
    POSUserSchema, 
    CustomerSchema, 
    BranchSchema, 
    CategorySchema, 
    ItemSchema,
    BranchStockSchema,
    BigStockSchema)

Base = declarative_base()

class POSUser(Base):
    __tablename__ = 'pos_users'

    pos_user_id = Column(Integer, primary_key=True, index=True)
    pos_user_role = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint('pos_user_id', name='uq_pos_user_id'),
    )
    def schema(self) -> POSUserSchema:
        return POSUserSchema(
            pos_user_id=self.pos_user_id,
            pos_user_role=self.pos_user_role
        )
class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_phone_number = Column(String, nullable=True)
    customer_location = Column(String, nullable=True)

    __table_args__ = (
        UniqueConstraint('customer_id', name='uq_customer_id'),
    )
    def schema(self) -> CustomerSchema:
        return CustomerSchema(
            customer_id=self.customer_id,
            customer_name=self.customer_name,
            customer_phone_number=self.customer_phone_number,
            customer_location=self.customer_location
        )

class Branch(Base):
    __tablename__ = 'branches'

    branch_id = Column(Integer, primary_key=True, index=True)
    branch_name = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint('branch_id', name='uq_branch_id'),
    )
    def schema(self) -> BranchSchema:
        return BranchSchema(
            branch_id=self.branch_id,
            branch_name=self.branch_name
        )
class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint('category_id', name='uq_category_id'),
    )
    def schema(self) -> CategorySchema:
        return CategorySchema(
            category_id=self.category_id,
            category_name=self.category_name
        )
class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    item_price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'), nullable=False)

    category = relationship("Category", back_populates="items")

    __table_args__ = (
        UniqueConstraint('item_id', name='uq_item_id'),
    )
    def schema(self) -> ItemSchema:
        return ItemSchema(
            item_id=self.item_id,
            item_name=self.item_name,
            item_price=self.item_price,
            category_id=self.category_id
        )

class BranchStock(Base):
    __tablename__ = 'branch_stock'

    branch_id = Column(Integer, ForeignKey('branches.branch_id'), primary_key=True)
    branch_stock_id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    branch_item_quantity = Column(Integer, nullable=False)

    branch = relationship("Branch", back_populates="stock")
    item = relationship("Item", back_populates="stock")

    def schema(self) -> BranchStockSchema:
        return BranchStockSchema(
            branch_stock_id=self.branch_stock_id,
            branch_id=self.branch_id,
            item_id=self.item_id,
            branch_item_quantity=self.branch_item_quantity
        )

class BigStock(Base):
    __tablename__ = 'big_stock'

    big_stock_id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)
    big_stock_quantity = Column(Integer, nullable=False)

    item = relationship("Item", back_populates="big_stock")

    def schema(self) -> BigStockSchema:
        return BigStockSchema(
            big_stock_id=self.big_stock_id,
            item_id=self.item_id,
            big_stock_quantity=self.big_stock_quantity
        )
