-- Query 1

create view shippedVSCustDemand as
	select __ as customer, __ as item, __ as suppliedQty, __ as demandQty
		from
		;


-- Query 2

create view totalManufItems as 
	select __ as item, __ as totalManufQty
		from
		;


-- Query 3
create view matsUsedVsShipped as
	select __ as manuf , __ as matItem, __ as requiredQty, __ as shippedQty
	from
		;


-- Query 4
create view producedVsShipped as
	select	__ as item, __ as manuf, __ as shippedOutQty, __ as  orderedQty
	from
		;


-- Query 5
create view suppliedVsShipped as
	select	__ as item, __ as supplier, __ as suppliedQty, __ as shippedQty
	from
		;


-- Query 6
create view perSupplierCost as
	select	__ as supplier, __ as cost
	from
		;


-- Query 7
create view perManufCost as
	select	__ as manuf, __ as cost
	from
		;


-- Query 8
create view perShipperCost as
	select __ as shipper, __ as cost
	from
		;


-- Query 9
create view totalCostBreakDown as
	select __ as supplyCost, __ as manufCost, __ as shippingCost, __ as totalCost
	from
		;


-- Query 10
create view customersWithUnsatisfiedDemand as
	select	__ as customer
	from
		;


-- Query 11
create view suppliersWithUnsentOrders as
	select	__ as supplier
	from
		;


-- Query 12
create view manufsWoutEnoughMats as
	select	__ as manuf
	from
		;

-- Query 13
create view manufsWithUnsentOrders as
	select	__ as manuf
	from
		;
