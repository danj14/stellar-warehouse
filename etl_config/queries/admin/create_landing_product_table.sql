create table landing_product (
	p_id varchar (32) not null,
	p_name varchar (64) not null,
	name_lower varchar (128) not null,
	base_value int,
	consumable boolean not null,
	charge_value int,
	stack_multiplier int,
	default_craft_amount int,
	craft_amount_step_size int,
	recipe_cost int,
	specific_charge_only boolean not null,
	normalised_value_on_world varchar (128),
	normalised_value_off_world varchar (128),
	wiki_category varchar (64) not null,
	is_craftable boolean not null,
	deploys_into varchar (32),
	economy_influence_multiplier real,
	cooking_ingredient boolean not null,
	good_for_selling boolean not null,
	substance_category varchar (64),
	product_category varchar (64) not null,
	rarity varchar (32) not null,
	legality varchar (32) not null,
	space_station_markup real,
	low_price_mod real,
	high_price_mod real,
	buy_base_markup real,
	buy_markup_mod real,
	trading_class varchar(32),
	has_requirements boolean not null
);