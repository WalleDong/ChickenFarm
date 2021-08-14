from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, DECIMAL, VARCHAR, CHAR, BIGINT

Base = declarative_base()


class OperationRecordTable(Base):

    __tablename__ = 'tbl_operation_record'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    code = Column(CHAR(6), nullable=False)
    operate_type = Column(VARCHAR(32), nullable=False)
    amount = Column(DECIMAL(10, 2))
    info_after_change = Column(VARCHAR(2048), nullable=False)
    info_before_change = Column(VARCHAR(2048), nullable=False)
    operate_time = Column(DateTime, default=datetime.now, nullable=False)
    comment = Column(VARCHAR(255))
