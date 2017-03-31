#!/usr/bin/env Python

"""Customer database master script"""

# Description: Assembles full customer database and performs analysis

# Script overview:
# 1. Open Customer csv file containing customer data
# 2. Loop through customers by customer ID
# 3. For each customer ID, call Orders script with following details:
#	a. Purpose: pull all order info for given customer
#	b. Inputs: Order Details and Orders overview CSV's
#	c. Outputs: Returns list of dictionary entries for each order in the following format:
#	custOrdersOutput=[{'ordernum1':[orderDate,['product1','product2']]},{'ordernum2':[orderDate,['product1','product2']]},...]
# 4. Assemble dictionary entry for each customer in the following format:
#	customerOrderDict={'customername':customerordersoutput, 'customername2':customerordersoutput2}
# 5. Perform analysis on outputted customer order dictionary
# 6. Render data into graphs and tables
#Open customer database function that pulls info from csv


import csv # import the csv module
import OrderInfoScript.py # pulls in other python script

### start: define function for pulling customer order info based on customer ID

#def custOrderInfo(customerid):

### end: define function for pulling customer order info based on customer ID


fileOpened=(csvfile)

with open('Customers*.csv','wb') as customerCSV:

	custRow=0

	for custRow in customerCSV:

		if custRow=0:
			
			# use list index method to find location of column
			customeridIndex=custRow.index('customerid')
			firstnameIndex=custRow.index('firstname')
			lastnameIndex=custRow.index('lastname')
			companynameIndex=custRow.index('companyname')
			stateIndex=custRow.index('state')
			phonenumberIndex=custRow.index('phonenumber')
			emailaddressIndex=custRow.index('emailaddress')

			custRow=custRow+1

		else:

			 # do nothing

		# assign columns values for each customer

		customerid=custRow[customeridIndex]
		firstname=custRow[firstnameIndex]
		lastname=custRow[lastnameIndex]
		companyname=custRow[companynameIndex]
		state=custRow[stateIndex]
		phonenumber=custRow[phonenumberIndex]
		emailaddress=custRow[emailaddressIndex]

		
		# call script to pull customer order info based on order ID

		#custOrdersTemp=custOrderInfo(customerid)

		




