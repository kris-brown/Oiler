################################################################################
def P017() -> int:
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
        then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
        in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
        forty-two) contains 23 letters and 115 (one hundred and fifteen)
        contains 20 letters. The use of "and" when writing out numbers is in
        compliance with British usage.

    """
    return sum(map(let,range(1,1000)))+len('onethousand')

onemap = {'1':len('one'),'2':len('two'),'3':len('three'),'4':len('four'),
          '5':len('five'),'6':len('six'),'7':len('seven'),
          '8':len('eight'),'9':len('nine'),'0':0}
tenmap = {'1':3,'2':len('twenty'),'3':len('thirty'),'4':len('forty'),
          '5':len('fifty'),'6':len('sixty'),'7':len('seventy'),
          '8':len('eighty'),'9':len('ninety'),'0':0}
hundmap  = {'0':0,**{k:v+len('hundredand') for k,v in onemap.items() if k!='0'}}
teendigs = '4679'

def let(n:int)->int:
    digs = dict(zip([3,2,1],reversed(str(n))))
    print(digs)
    corr = 1 if digs.get(2)=='1' and digs[3] in teendigs else 0            # cases in which 1X adds 4 letter to X
    corr -= 3 if (digs.get(1,'0')!='0' and digs.get(2)=='0' and digs[3]=='0') else 0 # no "and" if an even hundred
    return hundmap[digs.get(1,'0')]+tenmap[digs.get(2,'0')]+onemap[digs[3]]+corr

if __name__=="__main__":
    print(P017())
