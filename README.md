# 3bit Trinary Alphabet

Upon recieving a programmable 3 key keyboard I decided that I would like to be able to turn it into a full keyboard. With a binary counting system I knew that I could use Morse Code or which would be 6bit and at the very minimum I would need to have at least 5bit giving a maxiumum or 31. As I had 3 keys, I decided that making an unconventional trinary system with 0, 1 and 2 would be my route. Having a trinary counting system increased my options maximum differences greatly. Making the system 3 bit meant that the total number of options would be 27, as there are 26 letter in the basic latin alphabet, this left 1 option left to add a SPACE. I decided to set 000 to be the space and then count from 001, 002, , 010, 011..etc assigning the letters of the alphabet to each number in order. Below is what I came up with:

| 3bit |  Latin |
|------|:-------|
| 000  |  SPACE | 
| 001  |  a     |
| 002  |  b     |
| 010  |  c     |
| 011  |  d     |
| 012  |  e     |
| 020  |  f     |
| 021  |  g     |
| 022  |  h     |
| 100  |  i     |
| 101  |  j     |
| 102  |  k     |
| 110  |  l     |
| 111  |  m     |
| 112  |  n     |
| 120  |  o     |
| 121  |  p     |
| 122  |  q     |
| 200  |  r     |
| 201  |  s     |
| 202  |  t     |
| 210  |  u     | 
| 211  |  v     |
| 212  |  w     |
| 220  |  x     |
| 221  |  y     |
| 222  |  z     |

Writing a short Python script I could input any of the three numbers three times and it would output a letter. Doing this multiple time allowed me to create words and with the use of 000 = SPACE I could create sentances. 
