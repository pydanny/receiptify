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

    
Usage
------

1. Shell fun (TODO - make this one command)

.. code-block:: bash

    $ simplicity receipts.rst > input/receipts.json
    $ python receiptify.py receipts.rst
    $ complexity

2. Point your browser at http://127.0.0.1:9090/receipts/

3. Save as PDF

4. Email

5. Profit