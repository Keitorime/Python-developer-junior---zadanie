# Python-developer-junior---zadanie
Parsovanie dát zo stránky prospektmaschine.de

Solution explanation

	This Python script scrapes brochure data from Prospektmaschine, extracting relevant details 
	such as title, shop name, validity dates, and thumbnails. The parsed data is then saved as a JSON file.


	This code performs the following actions:

	Fetches the HTML content of the website using requests.

	Parses brochure details using BeautifulSoup.

	Extracts:

		- Title

		- Thumbnail URL

		- Shop Name

		- Validity Period

		- Parsing Timestamp

		- Saves extracted data into a JSON file.

	All the necessary libraries are already in venv, you just need to download and run the code in your virtual environment.
	
	Unit tests:
		
		This project includes unit tests in test_parsing.py. 
		Run tests with: 
			
		python -m unittest test_parsing.py  

