receiptify
==========

Builds customer receipts quickly


Format
-------

Input

.. code-block:: RestructuredText

    seller
    -----------------
    :company: Two Scoops Press / Cartwheel Web
    :address1: 4607 Lakeview Cyn Rd
    :address2: #285
    :address3: Westlake Village, CA 91361
    :country: United States
    
    Customer
    --------
    :person: John Doe
    :company: Megacorp
    :address1: 1234 Corporate Way
    :address2: 
    :address3: Corpolis, CO
    :country: Corpornation


    :Products:
    ----------
    :item1: 1 | 17 | uyqN | Two Scoops of Django: Best Practices for Django 1.5
    :item2: 1 | 29.95 | 1481879707 | Two Scoops of Django: Best Practices for Django 1.5

    
Usage
------

.. code-block:: bash

    $ receiptify receipts.rst
    4 receipts generated