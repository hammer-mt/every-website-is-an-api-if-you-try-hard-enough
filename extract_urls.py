# load the ril_export.html file
with open('ril_export.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# extract the urls
import re
urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/?[\w./%]*', html_content)
print(len(urls), " urls extracted")
print()

# print a few random examples in a loop
for i in range(5):
    print(urls[i])
print()

# deduplicate the urls
unique_urls = list(set(urls))
print(len(unique_urls), " unique urls")

# save the urls to a file
with open('extracted_urls.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(urls))
