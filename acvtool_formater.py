from bs4 import BeautifulSoup
import re


with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    package_name = soup.body.ul.li.a.contents[0].replace(".","\.")
    print(package_name)
    values = soup.select("tr:has(> td:has(> a:contains(" + package_name + ")))")
    print(values)

    soup.body.table.tbody.contents = values

    print(soup.body.table.tbody.contents) 

    newfile = open("new.html", "w")
    newfile.write(str(soup))
    newfile.close()
















    # table = soup.body.tbody
    # table_children = table.contents
    # print(table)


        # for i in table:
    #     print(i.find_all("a" , text=re.compile('^' + package_name)))
    # aaa = [x.parent.parent for x in package_columns]
    # for tag in package_columns:
    #     tag.decompose()
        #.decompose()