# -*- encoding: utf-8 -*-
# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

from collections import OrderedDict

s = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(",", "")
s = s.replace(".", "")
s = s.split()

l = [len(x) for x in s]

print(l)