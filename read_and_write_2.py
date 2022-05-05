def sort_and_save (txt1, txt2, txt3):
    with open(txt1, encoding='utf-8') as file1, \
            open(txt2, encoding='utf-8') as file2, \
            open(txt3, encoding='utf-8') as file3:

        catalog = {txt1: file1.readlines(), txt2: file2.readlines(), txt3: file3.readlines()}
        sorted_catalog = {}
        for value in sorted(catalog.values(), key=len):
            for key in catalog.keys():
                if catalog[key] == value:
                    sorted_catalog[key] = value

        with open('result.txt', 'w', encoding='utf-8') as file_result:
            for file_name, file in sorted_catalog.items():
                file_result.write(f'{file_name}\n{str(len(file))}\n')
                for stroka in file:
                    file_result.write(stroka)
                file_result.write('\n')

sort_and_save('1.txt', '2.txt', '3.txt')