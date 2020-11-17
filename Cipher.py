inp = open("input.txt", 'r', encoding="utf-8")
out = open("code_rus.txt", 'r', encoding="utf-8")
out_text = open("out.txt", 'w', encoding="utf-8")

txt = inp.readlines()
text = ""
for el in txt:
    text += str(el)


dic = {}
def write_dic(file):
    t = file.readlines()
    for el in t:
        dic[el.split()[0]] = str(el.split()[1].split("\n")[0])
    return dic


def rewrite_words_02(text, code_dic: dict):
    text_x = text.replace(' ', '')
    fin = ""
    lst = 0
    m_text = list(map(str, text.split()))
    print(m_text)
    for k in range(len(m_text)):
        ls = ''
        ss = ''
        coding_word = ''
        if m_text[k][0] in ',.?!:;':
            fin += m_text[k]
            lst += 1
            print(fin)
        elif not m_text[k][0].isdigit():
            for i in range(len(m_text[k])):
                if m_text[k][i] in ',.?!:;':
                    ls = m_text[k][i]
                    j = i
                # if m_text[k][i] in ',.?!:;' and not i == len(m_text[k])+1:
                #     ls = m_text[k][i]
                #     j = i
                else:
                    coding_word += str(code_dic[text_x[i+lst]]) + ';'
                    j = i
            fin += '{' + coding_word + '}'
            lst += j+1
            fin = fin[0:-2]
            if len(ls) > 0:
                fin += '}' + ls + ' '
            else:
                fin += '}' + ' '
            print(fin)
        else:
            for i in range(len(m_text[k])):
                if m_text[k][i] in ',.?!:;':
                    ls = m_text[k][i]
                    j = i
                else:
                    coding_word += m_text[k][i]
                    j = i
            fin += '(' + coding_word + ')'
            lst += j+1
            if len(ls) > 0:
                fin += ls + ' '
            else:
                fin += ' '
            print(fin)
    return fin


print(rewrite_words_02(text, write_dic(out)), file=out_text)