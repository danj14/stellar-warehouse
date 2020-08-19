# General Ideas
## Overall idea list:
* *Prioritize data-focused ideas; common features on other sites should be lower priorities*
* Publish crafting and refining recipes 
* Publish trade entry information  
  * Log player sell prices, demand, etc. 
  * Share location information for players to identify nearby profit centers
  * Provide some level of sorting to imply best trade combos (more info on this later)
* Session builder
  * Plan out your game session; input would be activities and output would be potential yield of currencies
  * Eventually be able to accept session duration and recommend activities?
    * Similarly, accept target currency amount and of which kind?
  * Craft (and what recipes), trade (and what routes), refine (and what outputs), etc.
* Player to player trading
  * Big stretch; relies on honor system
    * Player rank for this too; trustworthiness
  * Players exchange sellable/refine-able items (e.g. Living Mold for Salvage Devices; convert currency)
    * Requires input for/supply demand
    * e.g. players play other payers for a ride to other galaxies/systems
  * ML/Algo to reverse demand and price to figure out how to calculate from base price
* Player to player verification of entries
  * Verify that you have visited and the entered information is accurate
  * Reliability rank part of player profile
  * Other player/social ranks ideas? 
* Trade route builder
  * Build and share trade routes in web
  * See if we can use planet/system coordinates and light years to model/visualize path
  * Provide path coordinates/names (by player entry) 
* Base builder?
  * Research ability to ingest save data to put together data representation of base
  * Gather ingredients, cost, etc.
* Build "pragmatically" and be able to use core components for other games w/similar systems
* Fauna data? --> might be better as a later release (model anyways)
# ETL Inputs and Outputs
### Game file extract
#### Inputs:
* Raw game file
* Exported MBIN file
* Converted/unpacked EXML file
* Game files (.EXML) required for dimensional data model
*  
#### Outputs:
# Crafting/Refining/Etc. Inputs and Outputs
## Inputs:
* Selected ingredients
* Selected goal output
* (add-on) Selected currency goal
##  Outputs:
* List of recipes matching input ingredient(s)
* List of recipes matching desired output(s)
* (add-on) Possible recipe combos meeting or exceeding currency goal
