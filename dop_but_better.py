from functools import lru_cache
singles = ('',"один","два","три","четыре","пять","шесть","семь","восемь","девять")
hungreds = ('',"сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот")
tens = ('',"десять","двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто")
ten_and_singles = ("",'одиннадцать', "двенадцать","тринадцать",'четырнадцать',
'пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать')
thou_singles = ('','одна','две')
layer = 0

def num_to_str(num):
    razr_list = list(str(num))
    #f = globals["razr_"+ str(razr)]
    str_num = ''
    if razr_list==['0']:
        str_num = 'ноль'
    elif len(razr_list) ==1:
        str_num = razr_1(razr_list[-1])
    elif len(razr_list)==2:
        str_num = ten_and_single(razr_list, str_num)
    elif len(razr_list)==3:
        str_num = razr_3(razr_list[-3]) +" "+ ten_and_single(razr_list, str_num)
    elif len(razr_list)==4:
        str_num = thousands(razr_list) + " " + razr_3(razr_list[-3]) +" "+ ten_and_single(razr_list, str_num)
        str_num = " ".join(str_num.split())
    elif len(razr_list)==5:
        global layer; layer = 1
        #TODO layer must work
        if not(razr_list[-5]=='1') and (razr_list[-4]=='1'): layer = 2
        #print(layer)
        str_num = ten_and_single(razr_list[-5:-3],str_num) +" "+ num_to_str(int(''.join(razr_list[-4:])))
    elif len(razr_list)==6:
        layer = 1
        #TODO layer must work
        if not(razr_list[-5]=='1') and (razr_list[-4]=='1'): layer = 2
        #print(layer)
        str_num = razr_3(razr_list[-6])+" "+ ten_and_single(razr_list[-5:-3],str_num) +" "+ num_to_str(int(''.join(razr_list[-4:])))
    if len(str_num)>4 and 'ноль'in str_num:
        pass
    return zaplatka(str_num)
def zaplatka(str_num):
    if len(str_num)>4 and 'ноль' in str_num: return ' '.join(c if c != 'ноль' else 'тысяч' for c in str_num.split())
    return str_num

def ten_and_single(razr_list, str_num):
    #print(razr_list)
    if razr_list[-2]=='1' and razr_list[-1]!='0':
        str_num = razr_1x(razr_list[-1])
    elif layer!=2:
        str_num = razr_2(razr_list[-2]) + ' ' + razr_1(razr_list[-1])
    else:
        str_num = razr_2(razr_list[-2]) + ' ' + thou_singles[int(razr_list[-1])]
    return str_num

def thousands(razr_list):
    global layer
    if layer ==1: layer = 0 ;return "тысяч"
    if layer ==2: layer=0; return "тысяча"
    if razr_list[-4]=='1': layer=0; return "тысяча"
    if razr_list[-4]=='2': layer=0;return "две тысячи"
    if razr_list[-4]=='3': layer=0;return "три тысячи"
    if razr_list[-4]=='4': layer=0;return "четыре тысячи"
    if razr_list[-4]=='0': layer=0;return ''
    else:
        return singles[int(razr_list[-4])] + " тысяч"

def razr_1(a):
    return singles[int(a)]
def razr_2(a):
    return tens[int(a)]
def razr_3(a):
    return hungreds[int(a)]
def razr_4(a):
    pass
def razr_1x(a):
    return ten_and_singles[int(a)]


def int_to_str_dict(num_tuple):
    int_to_str_dict = {i: num_to_str(i) for i in num_tuple}
    return int_to_str_dict

#di = [i for i in range(90000)]
#TODO 90000
#print(int_to_str_dict(di))
print(num_to_str(9000))