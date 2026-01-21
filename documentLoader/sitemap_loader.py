from langchain_community.document_loaders import SitemapLoader

url='https://api.python.langchain.com/sitemap.xml'

loader= SitemapLoader(web_path=url)

docs=loader.load()

print(docs)