Auto DCF
========
.. image:: https://github.com/jackmoody11/autodcf/workflows/Tests/badge.svg
    :target: https://github.com/jackmoody11/autodcf/actions

.. image:: https://badge.fury.io/py/autodcf.svg
    :target: https://badge.fury.io/py/autodcf

The autodcf package aims to make it extremely simple to create DCF models, simple and complex alike.
If you are tired of running sensitivity tests to see how your model will behave with different sales growth patterns, this package is for you.

Getting Started
---------------
You can clone the repo from GitHub using

.. code::

   git clone https://github.com/jackmoody11/autodcf

Setup the project by navigating to the project root directory and running

.. code::

   python setup.py

Basic Usage
-----------
There are a few important classes which will help you build your DCF.
The ``Company`` class encapsulates three classes: ``BalanceSheet``, ``CashFlows``,
and ``IncomeStatement``. Once a ``Company`` object is created using the 3
financial statements, this can be passed to one of the DCF models (currently either ``SimpleDCF``
or ``DCF``).

.. code:: python

   from autodcf.company import BalanceSheet, CashFlows, Company, IncomeStatement
   from autodcf.models import SimpleDCF

   balance_sheet = BalanceSheet(assets=100, liabilities=50)
   cash_flows = CashFlows(capex=3)
   income_statement = IncomeStatement(sales=100,
                                      cogs=50,
                                      sga=25,
                                      rd=0,
                                      depreciation=4,
                                      amortization=2,
                                      interest=0,
                                      nonrecurring_cost=3,
                                      tax=4)
   company = Company(balance_sheet=balance_sheet,
                     cash_flows=cash_flows,
                     income_statement=income_statement,
                     price_per_share=2.00,
                     fully_diluted_shares=100)
   simple_dcf = SimpleDCF(change_in_nwc_to_change_in_sales=0.1,
                          company=company,
                          discount_rate=0.14,
                          sales_growth=0.03,
                          tax_rate=0.21,
                          terminal_growth_rate=0.03,
                          window=5)
   forecast = simple_dcf.forecast()

The code above will provide a filled out pandas DataFrame with estimated growth of different
line items from the income statement.


Future Enhancements
-------------------
- ``io``: Allow for DCF model to be exported to Excel
- ``data``: Allow users to specify what company and data source
  to use and fetch necessary data for B/S, CF, and I/S behind the scenes
- ``company``: Allow for integration with financial data APIs
- ``models``: Add different types of models (with/without synergies)