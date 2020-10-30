insert into landing_product_ingredient (
	product_id,
	ingredient_id,
	ingredient_amount
) values (
    {{parent_id as str}},
    {{ID as str}},
    {{Amount as int}}
);
