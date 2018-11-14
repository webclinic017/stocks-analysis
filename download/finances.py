#!/usr/bin/env python3

import os
import requests
import time

from colorama import init, Fore, Back, Style

class cFinances:
	def __init__( self ):
		pass
	
	def Download( self, iBrowser, iCompany ):
		print( '	Finances ...' )

		if not iCompany.mFinances.Name():
			print( Fore.CYAN + '	skipping ... (no id)' )
			return
			
		if not iBrowser.Options().ForceDownload() and os.path.exists( iCompany.DataFileHTML( iCompany.mFinances.FileName() ) ):
			print( Fore.CYAN + '	skipping ... (existing file)' )
			return

		r = requests.get( iCompany.mFinances.Url() )
		with open( iCompany.DataFileHTML( iCompany.mFinances.FileName() ), 'w' ) as output:
			output.write( r.text )
			
		time.sleep( 1 )
	