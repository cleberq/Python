import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
with urllib.request.urlopen("https://www.fundamentus.com.br/detalhes.php?papel=") as url:
    page = url.read()
soup = BeautifulSoup(page, "html.parser")
tb = soup.find_all("table")
print(tb)
df = pd.read_html(str(tb))
print(df)
