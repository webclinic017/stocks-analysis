#!/usr/bin/python3

#---

def Extract( iCompany, iSoup ):
	div_data = iSoup.new_tag( 'div' )
	div_data['class'] = 'clear last10'
	
	if not iCompany.mBoerse.mYears:
		return div_data
	
	tbody = iSoup.new_tag( 'tbody' )
	
	#---
	
	td = iSoup.new_tag( 'th' )
	td.string = ''
	tr = iSoup.new_tag( 'tr' )
	tr.append( td )
	for year in iCompany.mBoerse.mYears:
		td = iSoup.new_tag( 'th' )
		td.string = year
		tr.append( td )
	td = iSoup.new_tag( 'th' )
	td.string = 'Last 5 Years'
	tr.append( td )
	tbody.append( tr )
	
	#---
	
	td = iSoup.new_tag( 'th' )
	td.string = 'PER'
	tr = iSoup.new_tag( 'tr' )
	tr.append( td )
	for value in iCompany.mBoerse.mPER:
		td = iSoup.new_tag( 'td' )
		td.string = '{}'.format( value )
		tr.append( td )
	td = iSoup.new_tag( 'td' )
	tr.append( td )
	tbody.append( tr )
	
	#---
	
	td = iSoup.new_tag( 'th' )
	td.string = 'BNA'
	tr = iSoup.new_tag( 'tr' )
	tr['class'] = 'imp'
	tr.append( td )
	for value in iCompany.mBoerse.mBNA:
		td = iSoup.new_tag( 'td' )
		td.string = '{}'.format( value )
		tr.append( td )
	td = iSoup.new_tag( 'td' )
	tr.append( td )
	tbody.append( tr )
	
	td = iSoup.new_tag( 'th' )
	td.string = 'Croissance BNA'
	tr = iSoup.new_tag( 'tr' )
	tr.append( td )
	td = iSoup.new_tag( 'td' )	# empty first td
	tr.append( td )
	for value in iCompany.mBoerse.mBNAGrowth:
		td = iSoup.new_tag( 'td' )
		td.string = '{:.2f}%'.format( value * 100 )
		td['class'] = 'plus' if value >= 0 else 'minus'
		tr.append( td )
	td = iSoup.new_tag( 'td' )
	td.string = '~{:.2f}%'.format( iCompany.mBoerse.mBNAGrowthAverageLast5Y * 100 )
	td['class'] = 'plus' if iCompany.mBoerse.mBNAGrowthAverageLast5Y >= 0 else 'minus'
	tr.append( td )
	tbody.append( tr )
	
	#---
	
	td = iSoup.new_tag( 'th' )
	td.string = 'Dividende'
	tr = iSoup.new_tag( 'tr' )
	tr['class'] = 'imp'
	tr.append( td )
	for value in iCompany.mBoerse.mDividend:
		td = iSoup.new_tag( 'td' )
		td.string = '{}'.format( value )
		tr.append( td )
	td = iSoup.new_tag( 'td' )
	tr.append( td )
	tbody.append( tr )
	
	td = iSoup.new_tag( 'th' )
	td.string = 'Croissance Dividende'
	tr = iSoup.new_tag( 'tr' )
	tr.append( td )
	td = iSoup.new_tag( 'td' )	# empty first td
	tr.append( td )
	for value in iCompany.mBoerse.mDividendGrowth:
		td = iSoup.new_tag( 'td' )
		td.string = '{:.2f}%'.format( value * 100 )
		td['class'] = 'plus' if value >= 0 else 'minus'
		tr.append( td )
	td = iSoup.new_tag( 'td' )
	td.string = '~{:.2f}%'.format( iCompany.mBoerse.mDividendGrowthAverageLast5Y * 100 )
	td['class'] = 'plus' if iCompany.mBoerse.mDividendGrowthAverageLast5Y >= 0 else 'minus'
	tr.append( td )
	tbody.append( tr )
	
	#---
	
	td = iSoup.new_tag( 'th' )
	td.string = 'Rendement'
	tr = iSoup.new_tag( 'tr' )
	tr['class'] = 'imp'
	tr.append( td )
	for value in iCompany.mBoerse.mDividendYield:
		td = iSoup.new_tag( 'td' )
		td.string = value
		tr.append( td )
	td = iSoup.new_tag( 'td' )
	tr.append( td )
	tbody.append( tr )
	
	#---
	
	table = iSoup.new_tag( 'table' )
	table.append( tbody )
	
	div_data.append( table )
	
	return div_data;

