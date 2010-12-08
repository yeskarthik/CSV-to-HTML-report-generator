import csv

fileReader=csv.reader(open('/home/karthik/Desktop/NEN First Dot Nomination Form Section 2 .csv'))

fname='/home/karthik/Desktop/StartupFiles/'

i=1

for row in fileReader:
  print '\n'
  print 'Processing next row..'
  print '\n'
  a=row
  if i==1: 
    b=row
  j=0
  fn=fname+a[1]+'.txt'
  f=open(fn,'w')
  for each in a:
    print each
    f.write(b[j]+':')
    f.write(each)
    f.write('\n')
    print '\n'
    print '\n'
    j+=1
  f.close()
  i+=1
print 'Matter close!'

