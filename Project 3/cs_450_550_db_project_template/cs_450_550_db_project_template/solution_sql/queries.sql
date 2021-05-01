-- Query 1

create view shippedVSCustDemand as
	select cd.customer as customer, cd.item as item,sum(nvl(so.qty,0)) as suppliedQty, cd.qty as demandQty
		from customerDemand cd left outer join shipOrders so on cd.item = so.item and cd.customer = so.recipient
		group by cd.customer,cd.item,cd.qty
		order by cd.customer, cd.item
		;


-- Query 2

create view totalManufItems as 
	select mo.item as item, sum(mo.qty) as totalManufQty
		from manufOrders mo
		group by mo.item
		order by mo.item
		;


-- Query 3
create view matsUsedVsShipped as
	select Req.manuf, req.matItem, req.requiredQty, nvl(sum(so.qty),0) as shippedQty
	from(select mo.manuf as manuf , bom.matItem as matItem, sum( mo.qty * bom.QtyMatPerItem) as requiredQty
	from manufOrders mo,billOfMaterials bom
	where mo.item = bom.prodItem
	group by mo.manuf, bom.matItem) Req left outer join shipOrders so on Req.manuf = so.recipient and Req.matItem = so.item
	group by Req.manuf, req.matItem,req.requiredQty
	order by Req.manuf, req.matItem
	;

-- Query 4
create view producedVsShipped as
	select	mo.item as item, mo.manuf as manuf,nvl(sum(distinct so.qty),0) as shippedOutQty, mo.qty as  orderedQty
	from manufOrders mo left outer join shipOrders so on mo.item = so.item and mo.manuf = so.sender
	group by mo.item, mo.manuf, mo.qty
	order by mo.item, mo.manuf
	;



-- Query 5
create view suppliedVsShipped as
	select	supo.item as item, supo.supplier as supplier, supo.qty as suppliedQty, nvl(sum(distinct shipo.qty),0) as shippedQty
	from supplyOrders supo left outer join shipOrders shipo on supo.item = shipo.item and supo.supplier = shipo.sender
	group by supo.item, supo.supplier, supo.qty
	order by supo.item, supo.supplier
	;

-- Query 6
create view perSupplierCost as
	select supd.supplier,
	nvl((case
		when calc.totalcost<supd.amt1 then calc.totalcost
		when calc.totalcost>supd.amt2 then ((supd.amt1+(supd.amt2-supd.amt1)*(1-supd.disc1))+(calc.totalcost - supd.amt2)*(1-supd.disc2))
		when calc.totalcost>supd.amt1 and calc.totalcost<supd.amt2 then (supd.amt1+(calc.totalcost - supd.amt1)*(1-supd.disc1))
	end),0) as cost
	from (select supo.supplier as supplier, sum(supo.qty*supup.ppu) as totalcost
		from supplyOrders supo, supplyUnitPricing supup
		where supo.item = supup.item and supo.supplier = supup.supplier
		group by supo.supplier) calc right outer join supplierDiscounts supd on calc.supplier = supd.supplier
	order by supd.supplier
	;


-- Query 7
create view perManufCost as
	select mnfd.manuf,
	nvl((case
	when calc.totalcost < mnfd.amt1 then calc.totalcost
	when calc.totalcost > mnfd.amt1 then (mnfd.amt1+(calc.totalcost - mnfd.amt1)*(1-mnfd.disc1))
	end),0) as cost
	from (select mnfo.manuf as manuf, sum(mnfup.setUpCost+(mnfo.qty*mnfup.prodCostPerUnit)) as totalcost
		from manufOrders mnfo, manufUnitPricing mnfup
		where mnfo.item = mnfup.prodItem and mnfo.manuf = mnfup.manuf
		group by mnfo.manuf) calc right outer join manufDiscounts mnfd on calc.manuf = mnfd.manuf
	order by mnfd.manuf
	;



-- Query 8
create view perShipperCost as
	select sp.shipper,
	nvl(sum(greatest((case
	when calc.basecost<sp.amt1 then calc.basecost
	when calc.basecost>sp.amt2 then ((sp.amt1+(sp.amt2-sp.amt1)*(1-sp.disc1))+(calc.basecost - sp.amt2)*(1-sp.disc2))
	when calc.basecost>sp.amt1 and calc.basecost<sp.amt2 then (sp.amt1+(calc.basecost - sp.amt1)*(1-sp.disc1))
	end),sp.minPackagePrice)),0) as cost
	from (select ship_ord.shipper, BE1.shipLoc as fromloc, BE2.shipLoc as toloc , sum(distinct ship_ord.qty*itm.unitWeight*ship_prc.pricePerLb) as basecost
		from shipOrders ship_ord, busEntities BE1, busEntities BE2, items itm, shippingPricing ship_prc
		where ship_ord.sender = BE1.entity and ship_ord.recipient = BE2.entity and ship_ord.item = itm.item and ship_ord.shipper = ship_prc.shipper and BE1.shipLoc = ship_prc.fromloc and BE2.shipLoc = ship_prc.toloc
		group by ship_ord.shipper, BE1.shipLoc, BE2.shipLoc) calc right outer join shippingPricing sp on calc.shipper = sp.shipper and calc.fromloc = sp.fromloc and calc.toloc = sp.toloc
	group by sp.shipper
	order by sp.shipper
	;

-- Query 9
create view totalCostBreakDown as
	select sc.cost as supplyCost, mc.cost as manufCost,  ship_c.cost as shippingCost, (sc.cost+mc.cost+ship_c.cost) as totalCost
	from(select sum(sup_cost.cost) as cost from perSupplierCost sup_cost) sc, (select sum(manf_cost.cost) as cost from  perManufCost manf_cost) mc, (select sum(ship_cost.cost) as cost from perShipperCost ship_cost) ship_c
	;

-- Query 10
create view customersWithUnsatisfiedDemand as
	select distinct calc.customer
	from(select cust_d.customer,cust_d.item, nvl(sum(distinct ship_o.qty),0) as recieved
	from customerDemand cust_d left outer join shipOrders ship_o on cust_d.customer = ship_o.recipient and cust_d.item = ship_o.item
	group by cust_d.customer,cust_d.item
	order by cust_d.customer) calc,customerDemand cd
	where cd.item = calc.item and cd.customer = calc.customer and cd.qty>calc.recieved
	order by calc.customer
	;


-- Query 11
create view suppliersWithUnsentOrders as
	select distinct sup_ord.supplier as supplier
	from(select sup_o.supplier,sup_o.item, nvl(sum(ship_o.qty),0) as sent
	from supplyOrders sup_o left outer join shipOrders ship_o on sup_o.supplier = ship_o.sender and sup_o.item = ship_o.item
	group by sup_o.supplier,sup_o.item
	order by sup_o.supplier) calc, supplyOrders sup_ord
	where  sup_ord.item = calc.item and sup_ord.supplier = calc.supplier and sup_ord.qty > calc.sent
	;



-- Query 12
create view manufsWoutEnoughMats as
	select distinct Req.manuf
	from (select manu_ord.manuf, BM.matitem, sum(distinct manu_ord.qty * BM.QtyMatPerItem) as required
	from manufOrders manu_ord, billOfMaterials BM
	where manu_ord.item = BM.prodItem
	group by manu_ord.manuf, BM.matitem) Req,
	(select Test.manuf, Test.item, nvl(sum(distinct SO2.qty),0) as recieved
	from (select mo2.manuf, BM2.matitem as item
		from manufOrders MO2, billOfMaterials BM2 
		where MO2.item = BM2.prodItem
		) Test left outer join shipOrders SO2 on Test.Item = SO2.item and SO2.recipient = Test.manuf
	group by Test.manuf, Test.item) Got 
	where Req.manuf = Got.manuf and Req.matItem = Got.Item and Req.required > Got.recieved
	order by Req.manuf
	;

-- Query 13
create view manufsWithUnsentOrders as
	select distinct mnf2.manuf
	from(select mnf.manuf, mnf.item, nvl(sum(ship_o.qty),0) as sent
	from manufOrders mnf left outer join shipOrders ship_o on mnf.manuf = ship_o.sender and mnf.item = ship_o.item
	group by mnf.manuf,mnf.item
	order by mnf.manuf) calc, manufOrders mnf2
	where mnf2.manuf = calc.manuf and mnf2.item = calc.item and mnf2.qty > calc.sent
	;