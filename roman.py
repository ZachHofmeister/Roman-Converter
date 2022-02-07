di_roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
            'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
di_arabic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L',
             40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
# arabic_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#
# # OPTIONAL :  TODO:  you do NOT have to deal with illegal combinations -- but you may do so
# illegal_combinations = ['IIV', 'IIX', 'IIL', 'IIC', 'IID', 'IIM',     # illegal combinations
#                         'XXL', 'XXC', 'XXD', 'XXM',
#                         'CCD', 'CCM', 'VVV', 'LLL', 'DDD',
#                         'IIV', 'IIX', 'XXL', 'XXC', 'CCD', 'CCM']


def to_arabic(roman):
    # TODO: FILL IN THIS CODE
    arabic = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and (twoR := roman[i:i+2]) in di_roman:
            arabic += di_roman[twoR]
            i += 2
            # elif twoR[0] in di_roman:
            #     arabic += di_roman[twoR[0]]
            #     i += 1
            # else:
            #     print("to_arabic error")
        else:  # last char in string
            arabic += di_roman[roman[i]]
            i += 1
    return arabic


def to_roman(arabic):
    # TODO: FILL IN THIS CODE
    roman = ''
    while arabic > 0:
        for k, v in di_arabic.items():
            if arabic >= k:
                arabic -= k
                roman += v
                break
    return roman


def print_spaced(li_tuples, field_width=0):
    i = 0
    for el, v in li_tuples:
        print(f'{el :{field_width}} is {v}')
        i += 1
        if i % 5 == 0:
            print()


def run_to_roman_to_arabic_tests(begin=1, end=100, step=1):
    romans = []
    arabics = []
    for el in range(begin, end, step):
        romans.append((el, to_roman(el)))
    print_spaced(romans)
#
    for k, v in romans:
        arabics.append((v, to_arabic(v)))
    print_spaced(arabics, field_width=10)

"""
Output of run_to_roman_to_arabic_tests(1, 4000, 37):

1 is I
38 is XXXVIII
75 is LXXV
112 is CXII
149 is CXLIX

186 is CLXXXVI
223 is CCXXIII
260 is CCLX
297 is CCXCVII
334 is CCCXXXIV

371 is CCCLXXI
408 is CDVIII
445 is CDXLV
482 is CDLXXXII
519 is DXIX

556 is DLVI
593 is DXCIII
630 is DCXXX
667 is DCLXVII
704 is DCCIV

741 is DCCXLI
778 is DCCLXXVIII
815 is DCCCXV
852 is DCCCLII
889 is DCCCLXXXIX

926 is CMXXVI
963 is CMLXIII
1000 is M
1037 is MXXXVII
1074 is MLXXIV

1111 is MCXI
1148 is MCXLVIII
1185 is MCLXXXV
1222 is MCCXXII
1259 is MCCLIX

1296 is MCCXCVI
1333 is MCCCXXXIII
1370 is MCCCLXX
1407 is MCDVII
1444 is MCDXLIV

1481 is MCDLXXXI
1518 is MDXVIII
1555 is MDLV
1592 is MDXCII
1629 is MDCXXIX

1666 is MDCLXVI
1703 is MDCCIII
1740 is MDCCXL
1777 is MDCCLXXVII
1814 is MDCCCXIV

1851 is MDCCCLI
1888 is MDCCCLXXXVIII
1925 is MCMXXV
1962 is MCMLXII
1999 is MCMXCIX

2036 is MMXXXVI
2073 is MMLXXIII
2110 is MMCX
2147 is MMCXLVII
2184 is MMCLXXXIV

2221 is MMCCXXI
2258 is MMCCLVIII
2295 is MMCCXCV
2332 is MMCCCXXXII
2369 is MMCCCLXIX

2406 is MMCDVI
2443 is MMCDXLIII
2480 is MMCDLXXX
2517 is MMDXVII
2554 is MMDLIV

2591 is MMDXCI
2628 is MMDCXXVIII
2665 is MMDCLXV
2702 is MMDCCII
2739 is MMDCCXXXIX

2776 is MMDCCLXXVI
2813 is MMDCCCXIII
2850 is MMDCCCL
2887 is MMDCCCLXXXVII
2924 is MMCMXXIV

2961 is MMCMLXI
2998 is MMCMXCVIII
3035 is MMMXXXV
3072 is MMMLXXII
3109 is MMMCIX

3146 is MMMCXLVI
3183 is MMMCLXXXIII
3220 is MMMCCXX
3257 is MMMCCLVII
3294 is MMMCCXCIV

3331 is MMMCCCXXXI
3368 is MMMCCCLXVIII
3405 is MMMCDV
3442 is MMMCDXLII
3479 is MMMCDLXXIX

3516 is MMMDXVI
3553 is MMMDLIII
3590 is MMMDXC
3627 is MMMDCXXVII
3664 is MMMDCLXIV

3701 is MMMDCCI
3738 is MMMDCCXXXVIII
3775 is MMMDCCLXXV
3812 is MMMDCCCXII
3849 is MMMDCCCXLIX

3886 is MMMDCCCLXXXVI
3923 is MMMCMXXIII
3960 is MMMCMLX
3997 is MMMCMXCVII
I          is 1
XXXVIII    is 38
LXXV       is 75
CXII       is 112
CXLIX      is 149

CLXXXVI    is 186
CCXXIII    is 223
CCLX       is 260
CCXCVII    is 297
CCCXXXIV   is 334

CCCLXXI    is 371
CDVIII     is 408
CDXLV      is 445
CDLXXXII   is 482
DXIX       is 519

DLVI       is 556
DXCIII     is 593
DCXXX      is 630
DCLXVII    is 667
DCCIV      is 704

DCCXLI     is 741
DCCLXXVIII is 778
DCCCXV     is 815
DCCCLII    is 852
DCCCLXXXIX is 889

CMXXVI     is 926
CMLXIII    is 963
M          is 1000
MXXXVII    is 1037
MLXXIV     is 1074

MCXI       is 1111
MCXLVIII   is 1148
MCLXXXV    is 1185
MCCXXII    is 1222
MCCLIX     is 1259

MCCXCVI    is 1296
MCCCXXXIII is 1333
MCCCLXX    is 1370
MCDVII     is 1407
MCDXLIV    is 1444

MCDLXXXI   is 1481
MDXVIII    is 1518
MDLV       is 1555
MDXCII     is 1592
MDCXXIX    is 1629

MDCLXVI    is 1666
MDCCIII    is 1703
MDCCXL     is 1740
MDCCLXXVII is 1777
MDCCCXIV   is 1814

MDCCCLI    is 1851
MDCCCLXXXVIII is 1888
MCMXXV     is 1925
MCMLXII    is 1962
MCMXCIX    is 1999

MMXXXVI    is 2036
MMLXXIII   is 2073
MMCX       is 2110
MMCXLVII   is 2147
MMCLXXXIV  is 2184

MMCCXXI    is 2221
MMCCLVIII  is 2258
MMCCXCV    is 2295
MMCCCXXXII is 2332
MMCCCLXIX  is 2369

MMCDVI     is 2406
MMCDXLIII  is 2443
MMCDLXXX   is 2480
MMDXVII    is 2517
MMDLIV     is 2554

MMDXCI     is 2591
MMDCXXVIII is 2628
MMDCLXV    is 2665
MMDCCII    is 2702
MMDCCXXXIX is 2739

MMDCCLXXVI is 2776
MMDCCCXIII is 2813
MMDCCCL    is 2850
MMDCCCLXXXVII is 2887
MMCMXXIV   is 2924

MMCMLXI    is 2961
MMCMXCVIII is 2998
MMMXXXV    is 3035
MMMLXXII   is 3072
MMMCIX     is 3109

MMMCXLVI   is 3146
MMMCLXXXIII is 3183
MMMCCXX    is 3220
MMMCCLVII  is 3257
MMMCCXCIV  is 3294

MMMCCCXXXI is 3331
MMMCCCLXVIII is 3368
MMMCDV     is 3405
MMMCDXLII  is 3442
MMMCDLXXIX is 3479

MMMDXVI    is 3516
MMMDLIII   is 3553
MMMDXC     is 3590
MMMDCXXVII is 3627
MMMDCLXIV  is 3664

MMMDCCI    is 3701
MMMDCCXXXVIII is 3738
MMMDCCLXXV is 3775
MMMDCCCXII is 3812
MMMDCCCXLIX is 3849

MMMDCCCLXXXVI is 3886
MMMCMXXIII is 3923
MMMCMLX    is 3960
MMMCMXCVII is 3997

Process finished with exit code 0
"""