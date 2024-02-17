from bs4 import BeautifulSoup
import markdown

def html_to_markdown(html_content):
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Convert HTML to Markdown
    markdown_content = markdown.markdown(str(soup))
    return markdown_content

with open('Icon HTML.html', 'r') as file:
    html_content = file.read()

markdown_content = html_to_markdown(html_content)

# Write the Markdown content to a file
with open('Icon Markdown.md', 'w') as file:
    file.write(markdown_content)
