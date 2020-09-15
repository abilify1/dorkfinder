try:
 import os,sys,argparse
 from googlesearch import search
except ModuleNotFoundError:os.system("pip install google")
def Dorking(query,page,time,save):
    tmbh = 0
    for src in search(query, tld="com", lang="en", num=int(page), start=0, stop=None, pause=int(time)):
     with open(save,'a') as simpan:
      simpan.write(src+'\n')
     tmbh += 1
     print ("["+str(tmbh)+"]. "+src)
     if tmbh >= int(page):
      break;
    print ("\nTersimpan ke : "+save)


parse = argparse.ArgumentParser(description='Google dorking with python termux')
parse.add_argument('--query',type=str,metavar='<Dork>',help='Dork yang mau dicari')
parse.add_argument('--page',type=int,metavar='<Jumlah>',help='Jumlah url yang mau dicari')
parse.add_argument('--time',type=int,metavar='<Waktu>',help='Waktu berhenti (Pause)')
parse.add_argument('--save',type=str,metavar='<NamaFile>',help='Nama file untuk menyimpan url dork')

args = parse.parse_args()
query = args.query
page = args.page
time = args.time
save = args.save
if __name__ == '__main__':
 try:
  import urllib
  if not query or not page or not time or not save:
   parse.print_help()
   sys.exit(1)
  else:
   Dorking(query,page,time,save)
 except urllib.error.URLError:print ('No internet!!')
