from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)
"""

splitter =RecursiveCharacterTextSplitter.from_language(
language=Language.PYTHON,
chunk_size=50,
chunk_overlap=0
)

result = splitter.split_text(text)
# * first check for python syntax like class,def,etc then from paragraph -> line -> space -> letters
# ? after breaking it merges while the merged text is not exceeding max chunk size
print(result)
print(len (result))