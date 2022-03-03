# 3bit Trinary Alphabet

Upon recieving a programmable 3 key keyboard I decided that I would like to be able to turn it into a full keyboard. With a binary counting system I knew that I could use Morse Code or which would be 6bit and at the very minimum I would need to have at least 5bit giving a maxiumum or 31. As I had 3 keys, I decided that making an unconventional trinary system with 0, 1 and 2 would be my route. Having a trinary counting system increased my options maximum differences greatly. Making the system 3 bit meant that the total number of options would be 27, as there are 26 letter in the basic latin alphabet, this left 1 option left to add a SPACE. I decided to set 000 to be the space and then count from 001, 002, 010, 011..etc assigning the letters of the alphabet to each number in order. Below is what I came up with:

| 3bit |  Latin |
|------|:-------|
| 000  |  SPACE | 
| 001  |  A     |
| 002  |  B     |
| 010  |  C     |
| 011  |  D     |
| 012  |  E     |
| 020  |  F     |
| 021  |  G     |
| 022  |  H     |
| 100  |  I     |
| 101  |  J     |
| 102  |  K     |
| 110  |  L     |
| 111  |  M     |
| 112  |  N     |
| 120  |  O     |
| 121  |  P     |
| 122  |  Q     |
| 200  |  R     |
| 201  |  S     |
| 202  |  T     |
| 210  |  U     | 
| 211  |  V     |
| 212  |  W     |
| 220  |  X     |
| 221  |  Y     |
| 222  |  Z     |

Writing a short Python script I could input any of the three numbers three times and it would output a letter. Doing this multiple time allowed me to create words and with the use of 000 = SPACE I could create sentances. 
