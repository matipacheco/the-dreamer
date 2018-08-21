from urllib.request import urlopen
from bs4 import BeautifulSoup
from prettytable import PrettyTable

class TheDreamer:
	def __init__(self):
		site      = urlopen("https://careers.blizzard.com/es-mx/openings/engineering,information-technology/all/all/all/1")
		self.soup = BeautifulSoup(site, "html.parser")

	def look_for_jobs(self):
		job_oppening = self.soup.findAll(attrs = { "Table-item" })
		
		table = PrettyTable(["URL", "Position", "Project", "Location", "Position type"])

		for job in job_oppening:
			link          = job.get('href')
			position      = job.contents[0].get_text()
			area          = job.contents[1].get_text()
			location      = job.contents[2].get_text()
			position_type = job.contents[3].get_text()

			table.add_row([link, position, area, location, position_type])

		print(table)
