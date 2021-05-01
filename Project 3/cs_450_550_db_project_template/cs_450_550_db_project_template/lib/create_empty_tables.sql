create table items (
   item varchar2(25),
   unitWeight number(10),
   primary key(item) 
); 

create table busEntities (
   entity varchar2(25),
   shipLoc varchar2(25),
   address varchar2(25),
   phone number(10),
   web varchar2(100),
   contact number(20),
   primary key(entity)
); 

create table billOfMaterials(
prodItem varchar2(25), 
matItem varchar2(25), 
QtyMatPerItem number(10),
primary key(prodItem, matItem),
foreign key(prodItem) references items(item),
foreign key(matItem) references items(item)
);

create table supplierDiscounts
(supplier varchar2(25), 
amt1 number(10), 
disc1 number(5,2), 
amt2 number(10), 
disc2 number(5,2),
primary key(supplier));

create table supplyUnitPricing(supplier varchar2(25), 
item varchar2(25), 
ppu number(10),
primary key(supplier,item),
foreign key(item) references items(item));

create table manufDiscounts(
manuf varchar2(25), 
amt1 number(10), 
disc1 number(5,2),
primary key(manuf));

create table manufUnitPricing
(manuf varchar2(25), 
prodItem varchar2(25), 
setUpCost number(10), 
prodCostPerUnit number(10),
primary key(manuf,prodItem),
foreign key(prodItem) references items(item)
);

create table shippingPricing(
shipper varchar2(25), 
fromLoc  varchar2(25), 
toLoc varchar2(25), 
minPackagePrice number(10), 
pricePerLb number(10), 
amt1 number(10), 
disc1 number(5,2), 
amt2 number (10), 
disc2 number(5,2),
primary key (shipper, fromLoc, toLoc));

create table customerDemand(
customer varchar2(25), 
item varchar2(25), 
qty number(10),
primary key(customer, item),
foreign key(item) references items(item),
foreign key(customer) references busEntities(entity)
 );

create table supplyOrders(
item varchar2(25), 
supplier varchar2(25), 
qty number(10),
primary key(item, supplier),
foreign key(item) references items(item),
foreign key(supplier) references BUSENTITIES(entity)
);

create table manufOrders(
item varchar2(25), 
manuf varchar2(25), 
qty number(10),
primary key(item, manuf),
foreign key(item) references items(item),
foreign key(manuf) references BUSENTITIES(entity));
 

create table shipOrders(
item varchar2(25), 
shipper varchar2(25), 
sender varchar2(25), 
recipient varchar2(25), 
qty number(10),
primary key(item, shipper, sender, recipient),
foreign key(shipper) REFERENCES busEntities(entity),
foreign key(item) REFERENCES items(item),
foreign key(sender) REFERENCES BUSENTITIES(entity),
foreign key(recipient) REFERENCES BUSENTITIES(entity));
