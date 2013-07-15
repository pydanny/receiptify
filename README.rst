receiptify
==========

Builds customer receipts quickly.

Usage
------

0. pip install the requirements.txt

1. Shell fun (TODO - make this one command)

.. code-block:: bash

    $ simplicity receipts.rst > input/receipts.json
    $ python receiptify.py receipts.rst
    $ complexity

2. Point your browser at http://127.0.0.1:9090/receipts/

3. Save as PDF

4. Email

5. Profit

Screenshot from sample data
----------------------------

.. image:: ../master/sample.png


Simplicity-based Format
----------------------------

Input (using simplicity_)

.. code-block:: RestructuredText

    seller
    -----------------
    :company: Two Scoops Press / Cartwheel Web
    :address1: 4607 Lakeview Cyn Rd
    :address2: #285
    :address3: Westlake Village, CA 91361
    :country: United States
    :email: authors@cartwheelweb.com
    
    customer
    --------
    :person: John Doe
    :company: Megacorp
    :address1: 1234 Corporate Way
    :address2: 
    :address3: Corpolis, CO
    :address4: ar@megacorp.com
    :country: Corpornation


    products
    ----------
    :item1: 1 | 17 | uyqN | Two Scoops of Django: Best Practices for Django 1.5
    :item2: 1 | 29.95 | 1481879707 | Two Scoops of Django: Best Practices for Django 1.5

    
.. _simplicity: https://pypi.python.org/pypi/simplicity

TODO
-----

1. Maybe release on PyPI?
2. Make it one command to build the receipts
3. Save the incremental receipts to a single RST/JSON file for storage
4. Add the LICENSE file