###Set up
Configure a virtual environment

`virtualenv venv`

Activate the virtual environment and install the required packages

`pip install requirements.txt`

Once installed, make sure everything works by running the included tests! 
These tests can be run inside PyCharm easily or in the command line as shown below.

`python test_register.py`

###Use cases
* Accept a scanned item. The total should reflect an increase by the per-unit price after the scan. You will need a way to configure the prices of scannable items prior to being scanned.
* Accept a scanned item and a weight. The total should reflect an increase of the price of the item for the given weight.
* Support a markdown. A marked-down item will reflect the per-unit cost less the markdown when scanned. A weighted item with a markdown will reflect that reduction in cost per unit.
* Support a special in the form of "Buy N items get M at %X off." For example, "Buy 1 get 1 free" or "Buy 2 get 1 half off."
* Support a special in the form of "N for $X." For example, "3 for $5.00"
* Support a limit on specials, for example, "buy 2 get 1 free, limit 6" would prevent getting a third free item.
* Support removing a scanned item, keeping the total correct after possibly invalidating a special.
* Support "Buy N, get M of equal or lesser value for %X off" on weighted items.