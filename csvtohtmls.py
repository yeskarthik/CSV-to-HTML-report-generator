import csv

fileReader=csv.reader(open('/home/karthik/Desktop/NEN First Dot Nomination Form Section 2 .csv'))

fname='/home/karthik/Desktop/StartupFilesHTML/'

i=1

for row in fileReader:
  print '\n'
  print 'Processing next row..'
  print '\n'
  a=row
  if i==1: 
    b=row
  j=0
  fn=fname+a[1]+'.html'
  f=open(fn,'w')
  f.write('<html><head>'+a[1]+'</head><body><table>')
  for each in a:
    print each
    f.write('<tr><td><b>')
    f.write(b[j]+':')
    f.write('</b></td><td>')
    f.write(each)
    f.write('</td></tr>')
    f.write('\n')
    print '\n'
    print '\n'
    j+=1
  f.write('</table></body><html>')
  f.close()
  i+=1
print 'Matter close!'

