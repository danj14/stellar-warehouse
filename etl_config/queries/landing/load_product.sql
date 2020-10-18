insert into landing_product (
	p_id,
	p_name,
	name_lower,
	base_value,
	consumable,
	charge_value,
	stack_multiplier,
	default_craft_amount,
	craft_amount_step_size,
	recipe_cost,
	specific_charge_only,
	normalised_value_on_world,
	normalised_value_off_world,
	wiki_category,
	is_craftable,
	deploys_into,
	economy_influence_multiplier,
	cooking_ingredient,
	good_for_selling,
	substance_category,
	product_category,
	rarity,
	legality,
	space_station_markup,
	low_price_mod,
	high_price_mod,
	buy_base_markup,
	buy_markup_mod,
	trading_class,
	has_requirements
) values (
	{{Id as str}},
	{{Name as str}},
	{{NameLower as str}},
	{{BaseValue as int}},
	{{Consumable as bool}},
	{{ChargeValue as int}},
	{{StackMultiplier as int}},
	{{DefaultCraftAmount as int}},
	{{CraftAmountStepSize as int}},
	{{RecipeCost as int}},
	{{SpecificChargeOnly as bool}},
	{{NormalisedValueOnWorld as str}},
	{{NormalisedValueOffWorld as str}},
	{{WikiCategory as str}},
	{{IsCraftable as bool}},
	{{DeploysInto as str}},
	{{EconomyInfluenceMultiplier as real}},
	{{CookingIngredient as bool}},
	{{GoodForSelling as bool}},
	{{SubstanceCategory as str}},
	{{ProductCategory as str}},
	{{Rarity as str}},
	{{Legality as str}},
	{{SpaceStationMarkup as real}},
	{{LowPriceMod as real}},
	{{HighPriceMod as real}},
	{{BuyBaseMarkup as real}},
	{{BuyMarkupMod as real}},
	{{TradingClass as str}},
	{{HasRequirements as bool}}
);
