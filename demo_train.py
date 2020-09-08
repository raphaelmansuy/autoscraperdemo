

from autoscraper import AutoScraper

# Parameters
url = "https://www.quora.com/search?q=deep%20learning&time=year"
model_name = "model_quora"

wanted_list = ["When will deep learning finally die out?"]

# We instanciate the AutoScraper
scraper = AutoScraper()

# We train the Scraper
# Here we can also pass html content via the html parameter instead of the url (html=html_content)
result = scraper.build(url, wanted_list)

# We display the results if any
if(result):
  print("🚀 Great a query has been inferred !! Great gob.")
  print(result)

# If no result we leave with an error code
if(result == None):
  print("Sorry no query can be inferred ... 😿")
  exit(-1)

# We save the model for future use
print(f"💿 > Save the model {model_name}")
scraper.save(model_name)

