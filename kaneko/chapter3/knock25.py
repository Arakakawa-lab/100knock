# -*- encoding: utf-8 -*-
import re
from prettyprint import pp
from knock20 import load_json_file, get_record

if __name__ == "__main__":
    data = load_json_file("jawiki-country.json")
    text = get_record(data, "イギリス")
    r = re.compile(u"\{\{基礎情報 国([\s\S]+)\}\}")
    pp(r.findall(text))
    field_dic = {}

    field_flag = False
    for row in text:
        if row.find("{{基礎情報") != -1:
            field_flag = True
            continue
        if field_flag:
            data = row.split(" = ")
            field_dic[data.replace("|", "")] = data[1]
        if row == "{{"


