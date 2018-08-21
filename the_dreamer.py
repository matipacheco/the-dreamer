from urllib.request import urlopen
from bs4 import BeautifulSoup

class TheDreamer:
	def __init__(self):
		site      = urlopen("https://careers.blizzard.com/es-mx/openings/engineering,information-technology/all/all/all/1")
		self.soup = BeautifulSoup(site, "html.parser")

	def look_for_jobs(self):
		job_oppening = self.soup.find("div", attrs = { "Table-container" })
		
		for job in job_oppening:
			link          = job.get('href')
			position      = job.contents[0].get_text()
			area          = job.contents[1].get_text()
			location      = job.contents[2].get_text()
			position_type = job.contents[3].get_text()

			print(link, position, area, location, position_type)
