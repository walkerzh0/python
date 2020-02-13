from bs4 import BeautifulSoup

html_doc = "F:/Workspaces/python/PycharmProjects/pachong/data/download/000004.html"
html_file = open(html_doc, 'r')
html_handle = html_file.read()
soup = BeautifulSoup(html_handle, "html.parser")

#print(soup)
print(soup.meta)