import Image, ImageDraw, ImageFont, ImageFilter
import random
# Ëæ»ú×ÖÄ¸:
def rndChar():
 x=random.randint(0, 1)
 if x==0:
  return str(chr(random.randint(65, 90)))
 else:
  return str(random.randint(0, 9))
def rndList():
 x=0
 list=[]
 while x<200:
  y=rndChar()+rndChar()+rndChar()+rndChar()
  if y not in list:
   list.append(y)
   x=x+1
  else:
   print y,'is has in'
 return list
 
def main():
 print rndList()
if __name__ == '__main__':
    main()