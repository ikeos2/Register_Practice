###Set up
Configure a virtual environment

`virtualenv venv`

Activate the virtual environment and install the required packages

`pip install requirements.txt`

Once installed, make sure everything works by running the included tests! 
These tests can be run inside PyCharm easily or in the command line as shown below.

`python test_register.py`

###Using the register
The register object is designed to copy a common cash register.

When you scan an item, the register will display the price and add the item(and weight) to a list.
At any time, a total can be calculated that will automatically include any applicable specials or discounts.
Given the constraints of this simple example, all items this register "knows" about are contained in the price repository(`priceRepository.py`).
Likewise, all discounts and specials info ~~are~~ will be housed in the discounts repository(`discountsRepository.py`)