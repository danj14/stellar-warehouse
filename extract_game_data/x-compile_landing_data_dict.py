# TODO: New approach? Land raw files to small set of tables (refactor landing dict based on columns to input from XML)-->
# TODO: Extract data from landing tables and join on Natural Keys in Staging
# TODO: Populate warehouse
# TODO LANDING -> extract files to JSON -> save JSON to archive for back-up loads
# TODO STAGING -> extract data from landing tables -> massage to dimensions -> save .csv's to archive for back-up loads

landing_dict = {
    'product_table': {
        'source_files': ['nms_product'],
        'language_file_id': 'NameLower',
        'schema': {
            'Id': None,
            'Name': None,
            'NameLower': None,
            'BaseValue': None,
            'SubstanceCategory': None,
            'ProductCategory': None,
            'Rarity': None,
            'Legality': None,
            'Consumable': None,
            'ChargeValue': None,
            'StackMultiplier': None,
            'DefaultCraftAmount': None,
            'CraftAmountStepSize': None,
            'CraftAmountMultiplyer': None,
            'Recipe': [{
                'ID': None,
                'InventoryType': None,
                'Amount': None
            }],
            'SpaceStationMarkup': None,
            'LowPriceMod': None,
            'HighPriceMod': None,
            'BuyBaseMarkup': None,
            'BuyMarkupMod': None,
            'RecipeCost': None,
            'SpecifyChargeOnly': None,
            'NormalisedValueOnWorld': None,
            'NormalisedValueOffWorld': None,
            'TradingClass': None,
            'WikiCategory': None,
            'IsCraftable': None,
            'DeploysInto': None,
            'EconomyInfluenceMultiplier': None,
            'CookingIngredient': None,
            'GoodForSelling': None
        }
    },
    'substance_table': {
        'source_files': ['nms_substance'],
        'language_file_id': 'NameLower',
        'schema': {
            'Name': None,
            'NameLower': None,
            'ID': None,
            'SubstanceCategory': None,
            'Rarity': None,
            'Legality': None,
            'ChargeValue': None,
            'StackMultiplier': None,
            'SpaceStationMarkup': None,
            'LowPriceMod': None,
            'HighPriceMod': None,
            'BuyBaseMarkup': None,
            'BuyMarkupMod': None,
            'NormalisedValueOnWorld': None,
            'NormalisedValueOffWorld': None,
            'TradingClass': None,
            'EconomyInfluenceMultiplier': None,
            'CookingIngredient': None,
            'GoodForSelling': None
        }
    },
    'trading_class_table': {
        'source_files': ['nms_trading'],
        'file_section': 'TradingClassesData',
        'class_name_lookup': {
            'Mining': 'MINING',
            'HighTech': 'TECH',
            'Trading': 'TRADE',
            'Manufacturing': 'MANUFACT',
            'Fusion': 'ALLOY',
            'Scientific': 'SCIENCE',
            'PowerGeneration': 'POWER'
        },
        'schema': {
            'ClassName': None,
            'SellsClassName': None,
            'NeedsClassName': None,
            'MinSellingPriceMultiplier': None,
            'MaxSellingPriceMultiplier': None,
            'MinBuyingPriceMultiplier': None,
            'MaxBuyingPriceMultiplier': None
        }
    },
    'trade_category_table': {
        'source_files': ['nms_trading'],
        'file_section': 'CategoryData',
        'language_file_id': 'Name',
        'schema': {
            'CategoryName': None,
            'CategoryLanguageID': None,
            'ProductMultiplierChangePer100': None,
            'SubstanceMultiplierChangePer100': None
        }
    },
    'farm_plant_table': {
        'source_files': [
            'nms_farm_pearl', 'nms_farm_cactus', 'nms_farm_mordite',
            'nms_farm_gravitino', 'nms_farm_star', 'nms_farm_bud',
            'nms_farm_poop', 'nms_farm_gamma', 'nms_farm_solar',
            'nms_farm_frost', 'nms_farm_fungal', 'nms_farm_venom'
        ],
        'language_file_id': 'Name',
        'xml_file_root': 'name~Components',
        'schema': [
            'value~GcScannableComponentData.xml>name~ScanName~value',
            'value~GcScannableComponentData.xml>name~DisableIfBuildingPart~value',
            'value~GcScannableComponentData.xml>name~DisableIfInBase~value',
            'value~GcScannableComponentData.xml>name~ScanIconType~value',
            'value~GcScannableComponentData.xml>name~ScannableType~value',
            'value~GcSimpleInteractionComponentData.xml>name~Id~value',
            'value~GcSimpleInteractionComponentData.xml>name~Rarity&&value~GcRarity.xml>name~Rarity~value',
            'value~GcSimpleInteractionComponentData.xml>name~ActivationCost&&value~GcInteractionActivationCost.xml>'
            + 'name~Cost~value!!ActivationCost',
            'value~GcSimpleInteractionComponentData.xml>name~ActivationCost&&value~GcInteractionActivationCost.xml>'
            + 'name~SubstanceId~value',
            'value~GcSimpleInteractionComponentData.xml>name~ActivationCost&&value~GcInteractionActivationCost.xml>'
            + 'name~RequiredTech~value',
            'value~GcSimpleInteractionComponentData.xml>name~Name~value',
            'value~GcSimpleInteractionComponentData.xml>name~ScanType~value',
            'value~GcSimpleInteractionComponentData.xml>name~BaseBuildingTriggerActions>'
            + 'value~GcInteractionBaseBuildingState.xml>name~TriggerAction&&value~STEP0>name~Time~value!!STEP0_Time',
            'value~GcSimpleInteractionComponentData.xml>name~BaseBuildingTriggerActions>'
            + 'value~GcInteractionBaseBuildingState.xml>name~TriggerAction&&value~STEP1>name~Time~value!!STEP1_Time',
            'value~GcSimpleInteractionComponentData.xml>name~BaseBuildingTriggerActions>'
            + 'value~GcInteractionBaseBuildingState.xml>name~TriggerAction&&value~STEP2>name~Time~value!!STEP2_Time',
            'value~GcSimpleInteractionComponentData.xml>name~CanCollectInMech~value'
        ]
    },
    'refiner_recipe_table': {
        'source_files': ['nms_recipe'],
        'language_file_id': 'Name',
        'schema': {
            'Id': None,
            'Name': None,
            'TimeToMake': None,
            'Cooking': None,
            'ResultId': None,
            'ResultType': None,
            'ResultAmount': None,
            'Ingredients': [{
                'Id': None,
                'Type': None,
                'Amount': None
            }]
        }
    },
    # TODO: first grab regex language entries and then scan prior tables for ids to add
    'language_table': {
        'source_files': ['nms_language1', 'nms_language3', 'nms_language4', 'nms_language5', 'nms_language6'],
        'schema': {
            'Id': None,
            'Value': None
        },
        'source_id_regex_priority': [
            {'source_file': 'nms_language1', 'regex': [
                {'pattern': 'RARITY_\w*\d$', 'context': 'planet_rarity_class'},
                {'pattern': '^PLANETCLASS\d*$', 'context': 'celestial_body_class'},
                {'pattern': '^AGE\d{1,2}$', 'context': 'fauna_age'},
                {'pattern': '^SEX\d{1,2}$', 'context': 'fauna_gender'}
            ]},
            {'source_file': 'nms_language3', 'regex': [
                {'pattern': '^[A-Z]{3}_RACE_NAME_L$', 'context': 'system_life_form'},
                {'pattern': '^UI_CONFLICT_LEVEL_[A-Z]{3,5}_\d{1,2}$', 'context': 'system_conflict_level'},
                {'pattern': '^UI_ECON_LEVEL_[A-Z]{3,5}_\d{1,2}$', 'context': 'system_economy_strength'},
                {'pattern': '^UI_ECON_CLASS_[A-Z]{3,10}_\d{1,2}$', 'context': 'system_economy_class'},
                {'pattern': '^WEATHER_.*\d{1,2}$', 'context': 'planet_weather_class'},
                {'pattern': '^SCORCHED\d*$', 'context': 'planet_environment_scorched'},
                {'pattern': '^FROZEN\d*$', 'context': 'planet_environment_frozen'},
                {'pattern': '^IRRADIATED\d*$', 'context': 'planet_environment_irradiated'},
                {'pattern': '^TOXIC\d*$', 'context': 'planet_environment_toxic'},
                {'pattern': '^BARREN\d*$', 'context': 'planet_environment_barren'},
                {'pattern': '^DEAD\d*$', 'context': 'planet_environment_dead'},
                {'pattern': '^LUSH\d*$', 'context': 'planet_environment_lush'},
                {'pattern': '^WIRECELLSBIOME\d*$', 'context': 'planet_environment_wirecell'},
                {'pattern': '^CONTOURBIOME\d*$', 'context': 'planet_environment_contour'},
                {'pattern': '^BONESPIREBIOME\d*$', 'context': 'planet_environment_bonespire'},
                {'pattern': '^IRRISHELLSBIOME\d*$', 'context': 'planet_environment_irrishell'},
                {'pattern': '^HYDROGARDENBIOME\d*$', 'context': 'planet_environment_hydrogarden'},
                {'pattern': '^MSTRUCTBIOME\d*$', 'context': 'planet_environment_mstruct'},
                {'pattern': '^BEAMSBIOME\d*$', 'context': 'planet_environment_beam'},
                {'pattern': '^HEXAGONBIOME\d*$', 'context': 'planet_environment_hexagon'},
                {'pattern': '^FRACTCUBEBIOME\d*$', 'context': 'planet_environment_fractcube'},
                {'pattern': '^BUBBLEBIOME\d*$', 'context': 'planet_environment_bubble'},
                {'pattern': '^SHARDSBIOME\d*$', 'context': 'planet_environment_shards'},
                {'pattern': '^REDBIOME\d*$', 'context': 'planet_environment_red'},
                {'pattern': '^GREENBIOME\d*$', 'context': 'planet_environment_green'},
                {'pattern': '^BLUEBIOME\d*$', 'context': 'planet_environment_blue'},
                {'pattern': '^GLITCHBIOME\d*$', 'context': 'planet_environment_glitch'}
            ]},
            {'source_file': 'nms_language4', 'regex': [
                {'pattern': '^TEMPERAMENT_[A-Z]{1,26}\d{1,2}$', 'context': 'fauna_behavior'},
                {'pattern': '^UI_CREATURE_NOTE_\d{1,3}$', 'context': 'fauna_note'},
                {'pattern': '', 'context': ''}
            ]},
            {'source_file': 'nms_language5', 'regex': [
                {'pattern': 'SENTINEL_\w*\d$', 'context': 'planet_sentinel_class'},
                {'pattern': '^UI_CRE_TERRAIN_[A-Z]{3,24}$', 'context': 'fauna_habitat'},
                {'pattern': '^FISHDIET\d{1,2}$', 'context': 'fauna_diet'},
                {'pattern': '^PREDFISHDIET\d{1,2}$', 'context': 'fauna_diet'},
                {'pattern': '^HERBIVORE.*', 'context': 'fauna_diet'},
                {'pattern': '^CARNIVORE.*', 'context': 'fauna_diet'},
                {'pattern': '^OMNIVORE.*', 'context': 'fauna_diet'}
            ]}
        ]
    }
}

for item in landing_dict:
    print(item)
