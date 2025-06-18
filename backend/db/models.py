from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String, nullable=False, unique=True)
    mac_address = Column(String, nullable=False)
    vendor = Column(String)
    hostname = Column(String)
    last_seen = Column(DateTime)
    ip_release_type = Column(String)  # User-defined field for IP release type
    connection_type = Column(String)   # User-defined field for connection type
    device_type = Column(String)        # User-defined field for device type
    last_ip = Column(String)            # Last known IP address

    def __repr__(self):
        return f"<Device(ip_address='{self.ip_address}', mac_address='{self.mac_address}', vendor='{self.vendor}', hostname='{self.hostname}', last_seen='{self.last_seen}')>"