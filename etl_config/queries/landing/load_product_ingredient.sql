    product_id varchar (32) not null,
	ingredient_id varchar (32) not null,
	ingredient_amount int not null


insert into landing_product (
	product_id,
	ingredient_id,
	ingredient_amount
) values (
	%%Requirements
	    {{parent_Id as str}},
	    {{ingredient_ID as str}},
	    {{ingredient_Amount as int%}}
	%%
);
