def page1(soup):
    content = soup.select('.entry-content p')[1:]
    for i in range(len(content)):
        if content[i].text == 'Tabla de contenidos':
            return content[i+1].text

def page2(soup):
    print('2')
    content = soup.select('div p')
    for i in range(len(content)):
        if content[i].text == 'Índice del nombre':
            return content[i+1].text
PARSERS={
    'page1':page1,
    'page2':page2
}