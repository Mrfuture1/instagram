#coding=utf-8
import urllib
def callbackfunc(blocknum, blocksize, totalsize):
    '''�ص�����
    @blocknum: �Ѿ����ص����ݿ�
    @blocksize: ���ݿ�Ĵ�С
    @totalsize: Զ���ļ��Ĵ�С
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent
url = 'https://www.baidu.com/'
local = 'd:\\sina.html'
urllib.urlretrieve(url, local, callbackfunc)