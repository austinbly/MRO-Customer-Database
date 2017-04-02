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
# import sys
# (0, '/MRO/"Data Analysis"/"Customer Database Reference Data"')
import OrdersInfoScript # pulls in other python script
from glob import glob # allows for wildcard file calling
import os
import pandas as pd

# start: get path of currently executing file
#import inspect, os

# b=os.listdir(/MRO/'Data Analysis'/'Customer Database')
# print b

# print "current file location is",inspect.getfile(inspect.currentframe()) # prints current file location
# print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # prints path to currently executing file

# path = "User/austinbly/MRO/'Data Analysis'/'Customer Database'/OrdersInfoScript.py"

# ### start: define function for pulling customer order info based on customer ID

# #def custOrderInfo(customerid):

# ### end: define function for pulling customer order info based on customer ID


# #fileOpened=(Customer*.csv)
# print glob.glob(path)
# print type(glob.glob(path))


### start: Go to Customer CSV Repository

InputFilesPath='/Users/austinbly/MRO/Data Analysis/Customer Database Reference Data'

os.chdir(InputFilesPath)

### end: Go to Customer CSV Repository

# use glob to wildcard grab the Customers file with unknown trailing characters
# note: glob returns a list of all entries in the directory matching requirements

fhandle_Customers=glob("Customers*")[0] # assign file handle for customers CSV
fhandle_Orders=glob("Orders*")[0] # assign file handle for orders CSV
fhandle_OrderDetails=glob("OrderDetails*")[0] # assign file handle for order details CSV

with open(fhandle_Customers) as customerCSV:

	custRowNum=0

	for custRow in customerCSV:
		
		if custRowNum==0:
			
			# use list index method to find location of column
			customeridIndex=custRow.index('customerid')
			firstnameIndex=custRow.index('firstname')
			lastnameIndex=custRow.index('lastname')
			companynameIndex=custRow.index('companyname')
			stateIndex=custRow.index('state')
			phonenumberIndex=custRow.index('phonenumber')
			emailaddressIndex=custRow.index('emailaddress')

		else:

			 # do nothing
			 a=0

		# assign columns values for each customer

		customerid=custRow[customeridIndex]
		firstname=custRow[firstnameIndex]
		lastname=custRow[lastnameIndex]
		companyname=custRow[companynameIndex]
		state=custRow[stateIndex]
		phonenumber=custRow[phonenumberIndex]
		emailaddress=custRow[emailaddressIndex]

		if custRowNum <5:
			print custRow

		custRowNum=custRowNum+1
		

		# call script to pull customer order info based on order ID

		#custOrders=OrdersInfoScript.OrderInfoPuller(customerid)
		
		# custOrdersOutput=[{'ordernum1':[orderDate,['product1','product2']]},{'ordernum2':[orderDate,['product1','product2']]},...]
		# custOrdersTemp=custOrderInfo(customerid)

		




