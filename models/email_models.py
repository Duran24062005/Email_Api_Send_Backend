from config.database import Base
from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from datetime import datetime

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='emails')
    from_p = Column(String, nullable=False)
    to = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)