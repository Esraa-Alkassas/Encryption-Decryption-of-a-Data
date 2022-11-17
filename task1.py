#x = bytearray (b'code = .code    //    demomain: //  REPEAT 20 //  switch rv(nrandom, 9) ; generate a number between 0 and 8  //  mov ecx, 7    //   case 0    //   print "case 0"   //case ecx ; in contrast to most other programming languages,      //   print "case 7" ; the Masm32 switch allows "variable cases"         //   case 1 .. 3    //   .if eax==1      //   print "case 1"     //   .elseif eax==2       //    print "case 2"          //    .else      //   print "cases 1 to 3: other"     //     .endif     //      case 4, 6, 8     //   print "cases 4, 6 or 8"      //    default     //    mov ebx, 19     ; print 20 stars        //   .Repeat         //     print "*"      //     dec ebx               //          .Until Sign? ; loop until the sign flag is set      //    endsw     //     print chr$(13, 10)             ///        ENDM    //exit')
#print (x)

#y= bytearray (b'2457')
#print (y)


print ("original code")
x = bytearray (b'''code = .code
demomain:
  REPEAT 20
switch rv(nrandom, 9) ; generate a number between 0 and 8
mov ecx, 7
case 0
print "case 0"
case ecx ; in contrast to most other programming languages,
print "case 7" ; the Masm32 switch allows "variable cases"
case 1 .. 3
.if eax==1
print "case 1"
.elseif eax==2
print "case 2"
.else
print "cases 1 to 3: other"
.endif
case 4, 6, 8
print "cases 4, 6 or 8"
default
mov ebx, 19     ; print 20 stars
.Repeat
print "*"
dec ebx
.Until Sign? ; loop until the sign flag is set
endsw
print chr$(13, 10)
  ENDM
  exit''')
  
#print (x)

#y = str (x[1])
#y= str(x[1])+'e'
#print (y)    out is asci of 'o' letter as a simbol and the letter of 'e' is attached to it

#print (x)
#x[1]= x[1]+1
#print ("\n\n")
#print (x)

print ("\n\n")
print ("********************************")
print ("\n\n")
#print (x[510])


print ("after encription")
x[1]= x[1]+2+1
x[9]= x[9]+2+1
x[16]= x[16]+2+1
x[27] = x[27]+2+1
x[50] = x[50]+2+1
x[70] = x[70]+2+1
x[90] = x[90]+2+1
x[100] = x[100]+2+1
x[120] = x[120]+2+1
x[140] = x[140]+2+1
x[160] = x[160]+2+1
x[180] = x[180]+2+1
x[200] = x[200]+2+1
x[220] = x[220]+2+1
x[240] = x[240]+2+1
x[260] = x[260]+2+1
x[280] = x[280]+2+1
x[300] = x[300]+2+1
x[320] = x[320]+2+1
x[340] = x[340]+2+1
x[360] = x[360]+2+1
x[400] = x[400]+2+1
x[380] = x[380]+2+1
x[420] = x[420]+2+1
x[440] = x[440]+2+1
x[460] = x[460]+2+1
x[480] = x[480]+2+1
x[500] = x[500]+2+1
x[505] = x[505]+2+1
x[510] = x[510]+2+1
x[60] = x[60]+5
x[80] = x[80]+5
x[110] = x[110]+5
x[130] = x[130]+5
x[150] = x[150]+5
x[170] = x[170]+5
x[190] = x[190]+5
x[210] = x[210]+5
x[230] = x[230]+5
x[250] = x[250]+5
x[270] = x[270]+5
x[290] = x[290]+5
x[310] = x[310]+5
x[330] = x[330]+5
x[350] = x[350]+5
x[370] = x[370]+5
x[390] = x[390]+5
x[410] = x[410]+5
x[430] = x[430]+5
x[450] = x[450]+5
x[470] = x[470]+5
x[490] = x[490]+5
#x = x.append (b'edgjbjk')
#bytesTosend = 'esraa'+bytesTosend[5]   عايزة اسال ع الميثودز دي

print (x.decode('ASCII'))


print ("\n\n")
print ("after decription(real code)")
print ("\n\n")

x[1]= x[1]-3
x[9]= x[9]-3
x[16]= x[16]-3
x[27] = x[27]-3
x[50] = x[50]-3
x[70] = x[70]-3
x[90] = x[90]-3
x[100] = x[100]-3
x[120] = x[120]-3
x[140] = x[140]-3
x[160] = x[160]-3
x[180] = x[180]-3
x[200] = x[200]-3
x[220] = x[220]-3
x[240] = x[240]-3
x[260] = x[260]-3
x[280] = x[280]-3
x[300] = x[300]-3
x[320] = x[320]-3
x[340] = x[340]-3
x[360] = x[360]-3
x[400] = x[400]-3
x[380] = x[380]-3
x[420] = x[420]-3
x[440] = x[440]-3
x[460] = x[460]-3
x[480] = x[480]-3
x[500] = x[500]-3
x[505] = x[505]-3
x[510] = x[510]-3
x[60] = x[60]-5
x[80] = x[80]-5
x[110] = x[110]-5
x[130] = x[130]-5
x[150] = x[150]-5
x[170] = x[170]-5
x[190] = x[190]-5
x[210] = x[210]-5
x[230] = x[230]-5
x[250] = x[250]-5
x[270] = x[270]-5
x[290] = x[290]-5
x[310] = x[310]-5
x[330] = x[330]-5
x[350] = x[350]-5
x[370] = x[370]-5
x[390] = x[390]-5
x[410] = x[410]-5
x[430] = x[430]-5
x[450] = x[450]-5
x[470] = x[470]-5
x[490] = x[490]-5


print (x.decode('ASCII'))






