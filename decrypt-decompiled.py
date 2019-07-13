# uncompyle6 version 3.3.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 11:21:56) 
# [Clang 8.0.2 (https://android.googlesource.com/toolchain/clang 40173bab62ec7462
# Embedded file name: <ZBL>
# Compiled at: 2018-02-25 13:25:47

#!/data/data/com.termux/files/usr/bin/python2.7
#-*- coding: utf-8 -*-
#MASUKKAN KODE MARSHAL DI "TULISAN KODE MARSHAL/MARSHAL CODE"
#SETELAH ITU SAVE DAN JALANKAN

kode = "KODE MARSHAL/MARSHAL CODE"

#YANG INI JANGAN DIUBAH YA 😊
m = '\x1b[1;91m'
h = '\x1b[1;92m'
p = '\x1b[0m'
print '%s        /)   /) %s=======. %s=======' % (m, h, p)
print '%s       //   // %s// // //    %s//' % (m, h, p)
print '%s      //   // %s// // //    %s//' % (m, h, p)
print '%s     //===// %s(/ (/ (/    %s(/' % (m, h, p)
print '%s         Un%sMarshal %sTools' % (m, h, p)
print '%sCoded by: %sAnonyMass AKA Zhu Bai Lee' % (h, p)
print '\n\n\n'
try:
    kode = kode.replace('"exec(marshal.loads(""', '') and kode.replace('"exec(marshal.loads(\'"', '')
except:
    print '\x1b[1;91mOooops Terjadi error:\'(\nTampaknya anda lupa mengisi kode marshal divariabel kode = ""'
    print 'isi dulu variabelnya dengan kode marshal\ncontoh: kode = "c\\x00\\x00\x00..." <--Isi dengan kode yang lengkap\x1b[0m'
    exit()
else:
    import os, random, time, sys

    def run(x):
        pt = '\x1b[0m'
        rd = '\x1b[91m'
        try:
            num = 0
            while num < 1:
                for i, char in enumerate(x):
                    if i == 0:
                        print '\r%s%s%s%s' % (pt, char.lower(), rd, x[1:]),
                        sys.stdout.flush()
                    else:
                        if i == 1:
                            zbl = x[0].lower()
                            print '\r%s%s%s%s%s%s' % (rd, zbl, pt, char.lower(), pt, x[2:]),
                            sys.stdout.flush()
                        else:
                            if i == i:
                                zbl = x[0:i].lower()
                                print '\r%s%s%s%s%s%s' % (rd, zbl, pt, char.lower(), pt, x[i + 1:]),
                                sys.stdout.flush()
                        time.sleep(0.02)

                num += 1

        except:
            exit()


    try:
        with open('um.pyc', 'wb') as (f):
            f.write('\x03\r\n+[' + kode)
    except:
        print '\x1b[1;91mOooops Terjadi error:\'(\nTampaknya anda lupa mengisi kode marshal di variabel marshal = ""'
        print 'isi dulu variabelnya dengan kode marshal\ncontoh: kode = "c\\x00\\x00\x00..." <--Isi dengan kode yang lengkap\x1b[0m'
        exit()
    else:
        try:
            a = open('/data/data/com.termux/files/usr/lib/python2.7/site-packages/uncompyle6/disas.py', 'r').read()
        except:
            run('tunggu sebentar sedang menginstall bahan ')
            print '\x1b[0;30m'
            os.system('pip2 install uncompyle6 && clear')

    print '\x1b[30;0m'
    os.system('uncompyle6 um.pyc > um.py && rm um.pyc')
    import datetime, sys, string
    from uncompyle6.version import VERSION
    ver = sys.version.split('\n')
    asw = string.find(sys.version, ' ')
    vrs = sys.version[:asw]
    pf = sys.platform
    tm = datetime.datetime.now()
    tm = tm.strftime('%d-%m-%Y  %H:%M:%S')

    def clr():
        os.system('clear')


    print '\x1b[0m'
    d = open('um.py', 'r').read()
    x = d.replace('# Decompiled from: Python %s' % ver[0], '# Didecrypt dengan: python %s di platform %s' % (vrs, pf))
    x = x.replace('# Compiled at: 2018-11-18 03:55:07', '')
    x = x.replace('# %s' % ver[1], '# Decrypt by: AnonyMass AKA Zhu Bai Lee')
    x = x.replace('# uncompyle6 version %s' % VERSION, '# Didecrypt pada: %s' % tm)
    x = x.replace('# okay decompiling um.pyc', '')
    n = ('').join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(3))
    n = n + '.py'
    try:
        c = open(n, 'w').write(x)
    except:
        print '\x1b[0m'
        print "\x1b[1;91mOoops terjadi error :'(\x1b[0m"
        exit()

os.system('rm um.py')
run('file berhasil disimpan dengan nama %s ' % n)
