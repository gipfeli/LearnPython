#create a mapping of state to abbreviation

canton = {
	'Zurich': 'ZH',
	'Bern': 'BE',
	'Luzern': 'LU',
	'Schwyz': 'SZ',
	'Obwalden': 'OW',
	'Nidwalden': 'NW',
	'Glarus': 'GL',
	'Zug': 'ZG',
	'Freiburg': 'FR',
	'Solothurn': 'SO',
	'Basel-Stadt': 'BS',
	'Basel-Landschaft': 'BL',
	'Schaffhausen': 'SH', 
	'Appenzell A. Rh.': 'AR',
	'Appenzell I. Rh.': 'AI',
	'St. Gallen': 'SG',
	'Graubunden': 'GR',
	'Aargau': 'AG',
	'Thurgau': 'TG',
	'Tessin': 'TI',
	'Waadt': 'VD',
	'Wallis': 'VS',
	'Neuenburg': 'NE',
	'Genf': 'GE',
	'Jura': 'JU'
}

#create a basic set of states and gemeinde
gemeinde = {
	'LU': 'Littau',
	'ZH': 'Winterthur',
	'SO': 'Olten'
}

#add some more gemeinde
gemeinde['Uri'] = 'Altdorf'
gemeinde['Obwalden'] = 'Sarnen'
gemeinde['Nidwalden'] = 'Stans'

# print some gemeinde
print '-' * 10
print "Luzern's abbreviation is: ", canton['Luzern']
print "Zurich's abbreviation is: ", canton['Zurich']

# 
print '-' * 10
print "Luzern has: ", gemeinde[canton['Luzern']]
print "Zurich has: ", gemeinde[canton['Zurich']]

#print all out
print '-' * 10
for kanton, abbrev in canton.items():
	print "%s is abbreviated %s" %(kanton, abbrev)

#print all gemeinde 
print '-' * 10 
for abbrev, gemein in gemeinde.items():
	print "%s has the gemeinde %s" % (abbrev, gemein)

#doing both
print '-' * 10
for kanton, abbrev in canton.items():
	print "%s canton is abbreviated %s and has gemeinde %s" % (kanton, abbrev, gemeinde[abbrev])

print '-' * 10
kanton = canton.get('Uri')

if not kanton:
	print "Sorry, not canton named %s" % kanton

gemein = gemeinde.get('SG', 'Does not exist')
print "The gemeinde for canton 'SG' is: %s" % gemein	
