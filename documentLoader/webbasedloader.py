from langchain_community.document_loaders import WebBaseLoader

url='https://www.amazon.in/Kreo-Wireless-Mechanical-Pre-lubed-Absorption/dp/B0D83GYW8N/ref=sr_1_1_sspa?sr=8-1-spons&aref=k6Jb8Hl6ka&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY'

loader= WebBaseLoader(url)

docs=loader.load()

print(docs)