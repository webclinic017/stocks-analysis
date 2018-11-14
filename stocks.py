#!/usr/bin/python3

import os
import sys
import json
import argparse
from datetime import datetime

from colorama import init, Fore, Back, Style
init( autoreset=True )

from process.company import *
from process.extract.extract import *

from download.options import cOptions
from download.browser import cBrowser

# https://graphseobourse.fr/classement-des-entreprises-les-plus-innovantes-du-monde/

#---

# https://www.suredividend.com/warren-buffett-stocks/

#PATCH: to remove 'pseudo' comments
data = ''
with open( 'companies.json' ) as file:
	for line in file:
		if '#' not in line:
			data += line
#PATCH
			
data_groups = json.loads( data )
	
#---
		
parser = argparse.ArgumentParser( description='Process group(s).' )
parser.add_argument( 'groups', metavar='Group', nargs='*', help='One (or multiple) group(s) name (may also be company name)')
parser.add_argument( '--download', choices=['no', 'yes', 'force'], default='yes', help='Download source' )
parser.add_argument( '--suffix', help='Set suffix of output folder', required=True )
args = parser.parse_args()

if not os.path.exists( 'geckodriver' ):
	print( Back.RED + 'You need to download "geckodriver" file and move it next to this file' )
	sys.exit()

#---

# root_path = os.path.abspath( '.' )

# Create input (data) directory (_data/xxx)
# data_path = os.path.join( root_path, '_data', args.suffix )
# os.makedirs( data_path, exist_ok=True )

# Create output directories (_output/xxx and _output/xxx/img)
# output_path = os.path.join( root_path, '_output', args.suffix )
# os.makedirs( output_path, exist_ok=True )

# image_name = 'img'
# output_path_img = os.path.join( output_path, image_name )
# os.makedirs( output_path_img, exist_ok=True )

# Create output directories (_output-xxx and _output-xxx/img)
output_name = f'_output-{args.suffix}'
os.makedirs( output_name, exist_ok=True )
image_name = 'img'
output_image_name = f'{output_name}/{image_name}'
os.makedirs( output_image_name, exist_ok=True )

# Create input (data) directory (_data-xxx)
data_name = f'_data-{args.suffix}'
os.makedirs( data_name, exist_ok=True )

#---

companies = []

# Create a list of all companies
for data_group_name in data_groups:
	for data in data_groups[data_group_name]:
		company = cCompany( data[0], data[1], data[2], data[3], 
							data[4], data[5], 
							data[6], 
							data[7], data[8], data[9], 
							data[10], data[11] )
		company.Group( data_group_name )
		company.DataDir( data_name )
		company.ImageDir( image_name )
		
		companies.append( company )

#---

# If no group as argument, take them all
if not args.groups:
	for data_group_name in data_groups:
		args.groups.append( data_group_name )

#---

options = cOptions()
options.ForceDownload( args.download == 'force' )
options.TempDirectory( '' )

browser = cBrowser( options )

#---

for group in args.groups:
	companies_of_current_group = list( filter( lambda v: v.mGroup == group, companies ) )
	if not companies_of_current_group:
		companies_of_current_group = list( filter( lambda v: v.mName == group, companies ) )
	if not companies_of_current_group:
		continue
	
	print( 'Group: {} ({})'.format( group, len( companies_of_current_group ) ) )
	
	if args.download in ['yes', 'force']:
		browser.Init()

		for company in companies_of_current_group:
			company.Download( browser )
		
	Fill( companies_of_current_group )
	
	companies_sorted_by_yield = sorted( companies_of_current_group, key=lambda company: company.mYieldCurrent, reverse=True )

	content_html = Extract( companies_sorted_by_yield )

	print( 'Write html ...' )
	with open( '{}/{}-[{}].html'.format( output_name, group, len( companies_sorted_by_yield ) ), 'w' ) as output:
		output.write( content_html )
		
	WriteImages( companies_sorted_by_yield, output_name )
	
	print( '' )
	
#---

if browser is not None:
	browser.Quit()
