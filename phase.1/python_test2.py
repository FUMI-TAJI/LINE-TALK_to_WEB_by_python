#coding:utf-8
with open("[LINE] A-antennaのトーク.txt") as zax:

    lline = zax.readlines()#zaxとして[LINE] A-antennaのトーク.txtの全文章をリスト化

lline_replace = [q.replace('http', ' http') for q in lline]#全てのhttpと名のつく文字列の前にスペース挿入

with open("test-talk.txt", mode='w') as zaxx:
    zaxx.writelines('\n'.join(lline_replace))#スペース挿入後のファイルを別ファイルとして書き出し

#ここまでhtmlだけ抽出する準備
############################################################################

with open("test-talk.txt") as fff:
    lines = fff.read().split()#fffとしてtest-talk.txtの全文章を、スペースがあればそこで改行・別の文字列としてリスト化

l_XXX_start = [line.strip() for line in lines if 'http' in line.strip()]#"http"から始まる文字列だけ抽出

l_replace = [s.replace('"', '') for s in l_XXX_start]#無駄に表示される " を削除

sin1 = [s for s in l_replace if 'lin' and 'docs' not in s]#LINEのイベントURLとword文書リンクを除外

with open("tyuushutu.txt", mode='w') as g:
    g.writelines('\n'.join(sin1))#別ファイルとして書き出し
