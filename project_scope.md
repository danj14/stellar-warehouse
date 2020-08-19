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
* Raw game files (possible to run shell script to run windows program? <-- may want to seek out native library in future)
* Exported MBIN files (possible to run shell script to run windows program?)
* Game files (.EXML) required for dimensional data model (Converted/unpacked EXML files)
* Expected file list and when/if those files were last extracted for transformation
* .EXML -> JSON conversion spec/map
#### Outputs:
* Initially transformed JSON for later work
* Expected file alias list
* Status of validations, transformations, KPIs of job
### JSON Extract to Staging Tables
#### Inputs:
* .json files from game file extraction output
* JSON Landing -> Dimensional Staging spec/map
  * Need to research best format for storing output of transformed data for "pragmatic loading" to final warehouse
#### Outputs:
* Transformed data in dimensional schema with updated metadata (tables)
  * Natural to SK map
  * Can we avoid using DB for all steps of ETL? Volume of game file data is so small, we might be able to save on cost
    * That works because we need to be able to run fact tables at a different frequency than dim tables
* Status of validations, transformations, KPIs of job
### Staged data extract to Database (Postgresql?)
#### Inputs:
* 
#### Outputs:
* 
# Crafting/Refining/Etc. Inputs and Outputs
## Inputs:
* Selected ingredients
* Selected goal output
* (add-on) Selected currency goal
##  Outputs:
* List of recipes matching input ingredient(s)
* List of recipes matching desired output(s)
* (add-on) Possible recipe combos meeting or exceeding currency goal
