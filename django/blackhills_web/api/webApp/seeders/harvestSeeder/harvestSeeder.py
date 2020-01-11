import os, csv
from api.webApp.models import DeerHarvest, HarvestTitles


def handleXRow(row, section_title, HarvestTitles):
	pass


def handleImport(row, section_title, HarvestTitles, DeerHarvest):
	if section_title:
		title_obj, created = HarvestTitles.objects.get_or_create(title=section_title)
	else:
		title_obj = 0

	print(row)
	record, created = DeerHarvest.objects.get_or_create(
		unit_number = int(row[0].replace(',','')),
		bucks = int(row[1].replace(',','')),
		does = int(row[2].replace(',','')),
		total_harvest = int(row[4].replace(',','')),
		total_hunters = int(row[5].replace(',','')),
		total_rec_days = int(row[6].replace(',','')),
		percent_sucess = int(row[7].replace(',','')),
		section_title = int(title_obj.id if isinstance(title_obj, HarvestTitles) else title_obj),
		)
	print("%i - %i is imported"%(record.unit_number, record.section_title))

data_dir = 'api/webApp/seeders/harvestSeeder/geoData'
# for filename in os.listdir(data_dir):
curent_file = data_dir + '/' + '2018StatewideDeerHarvest.csv'
section_title = 0
with open(curent_file, 'r') as file:
	data = csv.reader(file)
	for row in data:
		if "D-" in row[0] or "DAU" in row[0] or "Total" in row[0] or "Unit" in row[0] or not row[0]:
			continue
		elif "2018 Deer" in row[0]:
			section_title = row[0]
			continue
		elif len(row) < 8:
			# handleXRow(row, section_title, HarvestTitles)
			continue
		else:
			handleImport(row, section_title, HarvestTitles, DeerHarvest)
		# possible_title = processRowData(row, section_title)		
		# if possible_title:
		# 	section_title = possible_title


# 	# curent_file = data_dir + '/' + filename
# curent_file = data_dir + '/' + '2018StatewideDeerHarvest.csv'
# with open(curent_file, 'r') as file:
# 	data = csv.reader(file)
# 	print(data)
# 	next(data)
# 	for row in data:
# 		print(row)
