# Dorking with python 
Hanya SC sederhana untuk dorking google di termux
# Usage:
<pre><code>
python dorking.py --query <DORK> --page <JUMLAH> --time <WAKTU> --save <FILE>
</code></pre>
# Keterangan: 
  --query = Dorknya\n
  --page = Jumlah url\n
  --time = Waktu jeda (pause)\n
  --save = nama file untuk menyimpan url
# Examples:
<pre><code>
python dorking.py inurl:/page.php?id= --page 5 --time 5 --save examples.txt
</code></pre>
