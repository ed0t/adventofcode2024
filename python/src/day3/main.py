import re, functools


def collect(filename):
    total = 0
    with open(filename, 'r', encoding='UTF-8') as file:
        lines = ""
        while line := file.readline():
            lines += line.strip()
    total += sum_all(chunkify(lines))

    return total


def parse(input):
    total = []
    prog = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    match = prog.findall(input)
    for element in match:
        v = functools.reduce(lambda a, b: int(a) * int(b), re.findall(r'\d{1,3}', element))
        total.append(v)

    return total


def sum_all(inputs):
    if len(inputs) > 0:
        return functools.reduce(lambda a, b: a + b, inputs)
    else:
        return 0


def validate():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    l = parse(input)
    print(l)
    assert sum_all(l) == 161
    input2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def chunkify(input):
    q = [input]
    result = []
    while len(q) > 0:
        input = q.pop(0).strip()
        print("INPUT", input)
        if "do()" in input:
            print('DO()')
            i = input.index("do()")
            if len(input[0:i]) > 0:
                q.append(input[0:i])
            if len(input[i + len("do()"):]) > 0:
                q.append(input[i + len("do()"):])
        elif "don't()" in input:
            print('DONT()')
            i = input.index("don't()")
            if len(input[0:i]) > 0:
                q.append(input[0:i])
        else:
            print("ADD", input)
            result.append(sum_all(parse(input)))
    print(result)
    return result


def validate2():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    input = "why()}''(!how()$~mul(420,484) ]}}mul(218,461),]/select()mul(93,56)';$-;*#$mul(162,415)mul(556,374)when()~when()<[select()^<(@mul(561,946);mul(97,699)select()+%when()~who():mul(387,15)>mul(927,207)~>~when()*who()'do()mul(454,740)when()%from(),~@%]from()mul(54,688)mul(338,694)what()select()~!< <;+<mul(127,722)'how()#~%*^mul(337,149)!,!mul(11,87)'<who()* where(671,579)-mul(596,125)who(){@,,-;+from()how(148,934)mul(452,741) ~}mul(513,343)mul(45,508),where()what()mul(758,167)$@''where()!*from()?mul(3,372)$@mul(491,647)]':%why()mul(459,967)(#(mul(369,467)):mul(662,431))<]:from()select()@mul(172,72)why()+,who()#from()+what()@#mul(394,721)what(){why()'!mul(69,419)when(300,372)%where()mul(135,896)who()who()when()}(?&%when()^mul(692,658)@~!$*when()+!mul(586,546)?#$select()from()~/mul(609,19)from()where():who()~*}mul(54,319);what()<what()when()when()@^<:mul(962,480)[%how(133,773)what()'^!:#]mul(419,406)@}#!)'mul(524,802)!%mul(938,46)$~{#mul(443,398)~where()*}&{]&>/mul(373,536)&+mul(505,931)why()[mul(457,381) >/ mul(800,67)why()~what()[mul(807,815)&$who()mul(667,529)&how(843,372)what()mul(636,823)<mul(363,915)$ +mul(162,118)($/{when()'^what()mul(461,357)^{mul(303,284)how()?why()mul(31,429)$who()-do()what()[}#mul(471,260)!,^(?,- why()!mul(706,849)(mul(845,857)@;?mul(417,923)~from()%how()who()where()&mul(731,874){![]+mul(433,314)what()>?*who()mul(960,331)where()?mul(648,668)how()/<!why()>who()why()!'mul(649,819)[~:how()&what()]{mul(857,238)%-mul(603,559)mul(511,89):mul(888,328)*how()$/}]mul(177,966)who(777,724)why();:;mul(211,756)]:}+mul(297,394)>^how();$[mul(603,264)mul(794,883)when()why()~&select()from())mul(446,859) & ;:>?*what()/mul(388,763);},?when()do()where())<->what()mul(974,397)+why()select()#@mul(137,814)@when()why()when(697,786)mul(897,431)^}}&mul(74,810)?<&~] '&$]mul(49,565)(>where())]/mul(926,812)mul(842,573) how()-mul(126,526) @mul(818,934)?select()}^what()who()from()}mul(240,118)!from()^@?what()mul(77,983)+$what()mul(736,950)$&%?why()select();mul(213,409)where()*&*what():>~when()<mul(581,188)%]where()-?[why(308,248)>when()mul(87,245)$^ what()]&#select()mul(558,637)why()!mul(695,929[;*)+??mul(896,494)when())who()select()^>+how(641,113)mul(374,932);^?:where()>mul(780,265)^#;+when()}}mul(218,272)@$#mul(892,55)[what()?~{'when()}mul(527,984) {>?-'+-:-don't()select()#;/?]''!mul(56,714)/<select()*)>why()>mul(819,178)*~[+}],mul(793,717)from(75,849)~-,+($/,mul(719,587)where()#:@;*$+#?mul(919,859)who()+what(),  @;>mul(89,488)where()?from()#$mul(680,657)mul(619,642)?[+don't()$:]{select()$what()@mul(619,164)}!select()mul(528,754)mul(199,830)how()where()+from()/~$who()(mul(49,273(mul(32,974)do()*select()]mul(42,960)%@?:[##::mul(802,384)]{##where())what()[mul(610,271)how()#@>what()where()don't()'&)>mul%?mul(449,76)when()%[<{^mul(944,356)what()(*;<{$<~mul(476,918){who(){-mul(124,698);?who()who(610,775)what()'&mul(579,336)why()<{'mul(953,943)<from()mul(222,14)?don't()'why(){mul(986,323)$who()mul(476,802)-<(from(577,504)when(377,110)%mul(160,849)why()when()what()mul(239,985);<who()%!mul(356,867)why(87,771)-mul(486,916)"
    l = chunkify(input)
    assert sum_all(l) == 48

if __name__ == '__main__':
    # validate()
    # validate2()
    # print(parse("'@$from():"))
    # print(sum_all([]))
    total = collect("input.txt")
    print(total)
