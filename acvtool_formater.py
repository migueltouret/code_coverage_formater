from bs4 import BeautifulSoup
import re


with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    package_name = soup.body.ul.li.a.contents[0].replace(".","\.")
    print(package_name)
    values = soup.select("tr:has(> td:has(> a:contains(" + package_name + ")))")

    soup.body.table.tbody.contents = values

    table = soup.body.tbody
    table_values = soup.body.table.tbody.find_all("tr")

    lines_missed_sum = 0
    lines_total_sum = 0
    methods_missed_sum = 0
    methods_total_sum = 0
    classes_missed_sum = 0
    classes_total_sum = 0


    for i in table_values:
        actual_values = i.find_all("td")
        lines_missed = actual_values[3].contents[0]
        lines_total = actual_values[4].contents[0]
        methods_missed = actual_values[5].contents[0]
        methods_total = actual_values[6].contents[0]
        classes_missed = actual_values[7].contents[0]
        classes_total = actual_values[8].contents[0]

        lines_missed_sum += int(lines_missed)
        lines_total_sum += int(lines_total)
        methods_missed_sum += int(methods_missed)
        methods_total_sum += int(methods_total)
        classes_missed_sum += int(classes_missed)
        classes_total_sum += int(classes_total)

    print(lines_missed_sum)
    print(lines_total_sum)
    # print(methods_missed_sum)
    # print(methods_total_sum)
    # print(classes_missed_sum)
    # print(classes_total_sum)

    total = soup.body.table.tfoot.tr.find_all("td")

    lines_covered = lines_total_sum - lines_missed_sum
    coverage_percentage = round(lines_covered / lines_total_sum  * 100, 5)
    total[1].string = str(lines_covered) + " of " + str(lines_total_sum)
    total[2].string = str(coverage_percentage) + "%"
    total[3].string = str(lines_missed_sum)
    total[4].string = str(lines_total_sum)
    total[5].string = str(methods_missed_sum)
    total[6].string = str(methods_total_sum)
    total[7].string = str(classes_missed_sum)
    total[8].string = str(classes_total_sum)


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