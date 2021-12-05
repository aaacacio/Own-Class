My program is an adventure simulation, based on real events of course, where you can dig fossils or catch wildlife while also being able to sell them or donate to a museum. Here are all the functions available and what they can do:

dig_fossil() - This adds a fossil to your inventory, your inventory and its contents are stored and remembered throughout the whole code.

assess_fossil() - Takes the fossil from your inventory and randomly classifies it, which can be sold for more. Requires fossil.
 
catch_bug() - Adds a random bug to your inventory.

reel_fish() - Adds a random fish to your inventory.

sell(x) - Requires string input, removes item given from the inventory and puts money into your wallet, another stored variable. Each item gives a different amount and requires the item inputted is in your inventory.

release(x) - Requires string input. You are able to release a bug or fish you have caught. Does not work on fossils.

donate(x) - Requires string input. Able to put an item collected into the museum, another stored variable. The same item cannot be donated twice and fossils must be assessed before being donated.

get_wallet() - Returns the amount in your wallet.

get_inv() - Lists and returns the contents of your inventory as a string.

get_museum() - Returns what items have been donated to the museum.


In the demo program provided, the user will first collect two fossils then asses just one. After it will catch three bugs and two fish. Then it will attempt to sell a ladybug, a sea bass, and a spin tail if, of course, these items were caught or found previously. Next it will attempt to donate an amber, then release a squid. In the end, it will call all the get-set methods to return your inventory, wallet, and museum statuses.
The demo program is found in the main() function at the bottom of the code.







