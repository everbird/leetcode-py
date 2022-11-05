#!/usr/bin/eni python
# encoding: utf-8

import copy

from collections import defaultdict


class Solution(object):

    def maxProduct(self, words):
        max_v = 0

        _words = list(set(words))
        d = defaultdict(set)
        for i, w in enumerate(_words):
            for ch in set(w):
                d[ch].add(w)

            conflicts = reduce(lambda x,y: x|y, (d[ch] for ch in set(w)), set())
            rest = set(_words[:i+1]) - conflicts

            if rest:
                v = len(w) * max(map(len, rest))
                max_v = max(max_v, v)

        return max_v


if __name__ == '__main__':
    s = Solution()

    tests = [
        (
            ["abcw","baz","foo","bar","xtfn","abcdef"],
            16
        ),
        (
            ["a","ab","abc","d","cd","bcd","abcd"],
            4
        ),
        (
            ["a","aa","aaa","aaaa"],
            0
        ),
        (
            ["jfkpfpcdkebilaeidhnlogoeilhikhacecnhicnkebkabe","ahijogepongpaeanckbalpmo","accdgaa","kielhbinkhkckdhhhfhjbbpmceligojghojeo","iopahocipcibi","edofelbiopgpepchcahedelhgfpgcjffnci","aleblaiddencgigakbkfmlbenojagap","dnfcoljeo","nnpibbgcanigagohmpppncmlcopopfipbmkaoblglco","jddjefccka","gplcmphekiichiigfmjaioldabnpjmbblkpi","npbfbbfcdkjleehfhm","nhipnapnlapkkhnompjjihihm","gleigkjnbnhcneeplodbdm","cdhfmlmedfjchacbeokoolbcblnhliffoeikejlmpmpnbaehmm","nknohom","cgdiifjgmmoihbmaode","dl","igdjknfofnibgnjekhbnma","fhgh","fbelljjfdbofcijkcjfdibpokgnjhcm","acblagjghogphabjcmhmce","logjpgobjeolajbjoeheimkbopfomefcnpcnmf","hkiegbbokbaiacmak","dnfgfdjlcnhlknlkafmlhenbhilop","egpnkmbengi","haockebeknfhkjbnhkmhpgjgjlfkddegdgohejegmmcgo","mmanegaencnfmakmfheigihni","ofbefemlggdebkhpkiajalombbodnccdnpadakiacapognmnhdb","gacidjkhmlbcomlkgnghdianmefpnbfofhfoipbfmpja","kbkcbolgmfbeeaaajj","akomemkgegehjghghjkkcleepaidhoibeaemkelmpip","papchohenlgdcbaljknmakagdpnlillkajekao","iahocnejnmecpahmkdehfhppmkhnmghcbhkmnn","kcdfjmadbikaapplahohoaghdjdgiejajeahopldjfpb","cjfdjccajihgagabcadkhnp","hl","kegfclkcgonjfnmofpjhplbkmmne","hgolcmclfofaogopkobdbanbaf","idlfpkmeko","babpcboacmnkefmakpdafgmegahdaeflahmimnbd","lbjpdgnonifkjkdkckhalelbcojbbbfpnmkpjhmhlmebbcfcmb","liljpmhpllipfdogachkeni","dadiggeapkbbmcm","khjfijkapokngoifbnoeoehocchgfflonmcgcfcac","japfojh","joinpnanbkiconcinpocphdcjhnhnfoc","gdgdfakikjaoemfemllgfeggfljjmalopadgofpb","plmaiiiempdochobakhpfhndfeoecjlbhpinoeaepbgnhoeegip","khalgofbdichplpgneobognlpdljhbioflfkcodoja","kcichhaihappiofnkcaoedocnbgfocnemdgmbgih","coepfnbeempfcgkihhkomgpiblmjmnladegpagdgflelecahbp","phhioagkaibjhojahfdgafhmmn","ngnbgpcmkmlpmljfddjgjhgmp","ijjmfejdnckiimihfakhm","jojlkdiogkpeibapeikkij","jhnlmieanhngiolbdmfejenocnmnekkneg","ogapbocfcmcbffphhemajgefmgbn","pl","eblakpdbfcckbnodpofjhmfdjijnbcdhloban","nohhgnpdnc","nlicahkipcolliikflahbdddmlffpgiejjfnpolklnkgegjoeo","cblihebmbeocjmnlfjpkdhhcg","icejcljipkndode","cbcjhdkpaefalhcjhkjooljmkakpjbahbi","olaiacok","hhimmhjmahaidifjmaopfganogfhgbgamnkcefceffaghnllkh","nicpanepogjoaoildmhkikpkppacp","bihdkdplgb","aloffedaneolpkocghnpibagnakmh","jiccilejnmpk","mcdgnifdeelcnohjinpcahaeoaamegc","jcdgkcioccmdjipbbmlnlgnkomkjmephdanpgdlfadgadnhihhm","leldpcndblihbencdnaneldlgfhhmpmclfoamhhbhdcjhfded","poojfhdbecognfloaackccpfcifobfbanii","agihjjdcbofpoejjakplpkkjclmmkj","acmgpojlmbodgglpklhmoldjpdgamcopoehaoopjao","dicilcjjnnbhib","fpigmme","ljdbngghpfmobaecdhhglmimmfopbgeojmc","paobomiigaodad","nngohffjnlhigo","adjlglollhhgmmifecgdfgggikoi","pmmknldejblmgkbhfaamili","eobdkfdegjihbgacmekokccgpcd","mmjolkoobmgikcbg","gfefajndbajbjlhlfocmai","iaaalpifgemlaagegiedlnibncfomeegmkpjjclmnnci","dkeilincklaeboohpadopamfpmbbddpdml","fcmoolajaeoiicnadhek","dnjhgpcjmdadociikpnkhknmljepde","jekabacmpgfbbeohjkmkkfmgfjjhpdcpanc","mnkecmmdhphnb","ncnleimlfibl","epnjigmeijmikplokfcafiefifeijbfbfoccmfmclhiojle","alkoicmgdflolgoklnaacgbkjaanioimiplgnpe","miikl","fjeglgdedmgmfnbipmddb","aghfhmg","gj","dkfpjealelpkodigicbncneggbfkc","ppfgpodnb","enljbkekagf","bchjplojdjomndpmfiolcndbdfjbcgiofjpkogdicoec","ngnajcgkhflejbkdcp","edmpfbmbfenadeoogpchhmknp","kakkhoalnekoofidnicdppehfhlaimfjdcahhbjefnpkol","mfonfmjobjpmpabhlajkmeibhpciokclppg","imjbkn","hhgbpigagaihaiaianfkgamcdnoicigpcfphmanokeci","hcjilgljhocfjjonchgccdfohafpefhhb","afnpkfbcpffhflhkgmgoeao","hpbegbdafkdbkgghmijjpfik","ochiifkndigbjjlioaicknfdnipceoimcdfibobbbocbhdhl","bcockohmml","oeihjodjellohdgglkgibkkaikilkndpjihkngpncbphllid","dcffmdcgcenhlnpakgloljpiemilljjfdjidhgbpbgfgadkd","iglmoopeakfhlgmnejogdajllceikcpodekhnnpkilnbcnknjo","dlenjobobjneagl","cabnhmhhabojbkmofgonohogdjllhjfdgpnkgioecbk","cjpgnhkpoobf","adoadfloncgljcfjcefkcffdhihfhepalcggldjpia","lldiapakibgaffhoffihnaapnocdlecfaohf","lmpbbgkdgjfholipjpkkbh","kpbilaaclhkdjknaen","biienn","bifippkndbhbknonhedofllgiabfjfehoflkfkagloi"],
            105
        ),
    ]
    f = s.maxProduct
    for input_args, expected in tests:

        if isinstance(input_args, tuple):
            r = f(*input_args)
        else:
            r = f(input_args)
        print 'Result:{}\tInput:{}\tOutput:{}\tExpected:{}'.format(r == expected, input_args, r, expected)
