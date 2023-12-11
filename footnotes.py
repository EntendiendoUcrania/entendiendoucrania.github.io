import os
from bs4 import BeautifulSoup

def modify_footnotes(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Modify footnote numbers
    footnotes = soup.find_all('sup')
    for i, footnote in enumerate(footnotes, start=1):
        a_tag = footnote.find('a')
        if a_tag:
            a_tag.string = str(i)
            a_tag['href'] = f'#fn{i}'
            a_tag['id'] = f'ref{i}'

    # Add footnote section at the end
    footnote_section = soup.new_tag('div', **{'class': 'footnotes'})
    h4 = soup.new_tag('h4')
    h4.string = 'Notas'
    footnote_section.append(h4)

    for i in range(1, len(footnotes) + 1):
        p = soup.new_tag('p', **{'id': f'fn{i}'})
        p.string = f'{i}. '
        a = soup.new_tag('a', **{'href': f'#ref{i}', 'title': f'Vuelve a la nota {i} del texto.'})
        a.string = '↩'
        p.append(a)
        footnote_section.append(p)

        # Add an empty line after each <p> element
        footnote_section.append('\n')

    # Append the footnote section to the end of the document
    soup.append(footnote_section)

    # Create the modified file path
    base_path, file_name = os.path.split(html_file)
    modified_file_path = os.path.join(base_path, 'modified_' + file_name)

    # Save the modified HTML content with formatting preserved
    with open(modified_file_path, 'w', encoding='utf-8') as modified_file:
        modified_file.write(str(soup))

if __name__ == '__main__':
    html_file = r'C:\Users\juanm\Dropbox\entendiendoucrania_jekyll\_posts\2023\2023-12-11-bojcun_1.html'
    modify_footnotes(html_file)