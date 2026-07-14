from IT215_SS17_BTTH1.BTTH1.database import Base, engine
from sqlalchemy import Integer, Column, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


package_truck = Table(
    "package_truck",
    Column("package_id", Integer, ForeignKey("packages.id"), primary_key=True),
    Column("truck_id", Integer, ForeignKey("trucks.id"), primary_key=True)
)

class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    warehouse_name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)

class Package(Base):
    __tablename__ = "packages"

    id = Column (Integer, primary_key=True, index=True, autoincrement=True)
    package_code = Column (String(255), unique=True)
    weight = Column(Float, nullable=False)
    warehouse_id = Column(String, ForeignKey("warehouses.id"))
    warehouse = relationship("Warehouse", back_populates="packages")
    waybill = relationship("Waybill", back_populates="package", uselist=False)
    trucks = relationship("Truck", secondary=package_truck, back_populates="packages")

class Waybill(Base):
    __tablename__ = "waybills"

    id = Column (Integer, primary_key=True, index=True, autoincrement=True)
    tracking_number = Column(String(255), nullable=False)
    shipping_status = Column(String(255), nullable=False)
    package_id = Column(String(255), ForeignKey("packages.id"), unique=True)
    package = relationship(
        "Package",
        back_populates="waybill"
    )

class Truck(Base):
    __tablename__ = "Truck"
    
    id = Column (Integer, primary_key=True, index=True, autoincrement=True)
    license_plate = Column(String(255), nullable=False)
    packages = relationship(
        "Package",
        secondary=package_truck,
        back_populates="trucks"
    )


Base.metadata.create_all(bind=engine)
