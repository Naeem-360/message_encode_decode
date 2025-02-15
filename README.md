# my message_encode_decode program🥴
This script allows you to encode and decode messages by slightly modifying word structures.
It enhances security by making messages harder to understand without decoding.

Encoding Rules:
1.If a word has fewer than 3 letters, it is simply reversed.
2.For longer words:
   The first and last letters are swapped.
   Three random letters are added at the beginning and end of the word.
   The modified word is then returned.    
Example:
Input: hello world
Encoded Output: abcoollehxyz defwrlxyz (Random letters will vary)

Decoding Rules:
1.If a word has fewer than 3 letters, it is simply reversed back.
2.For longer words:
  The first 3 and last 3 letters are removed.
  The first and last letters of the remaining word are swapped back.
  The original word is restored.
Example:
Encoded Input: abcoollehxyz defwrlxyz
Decoded Output: hello world

Usage:
1.Run the script, and select:
 1 for encoding
 2 for decoding
2.Enter your message.
3.The script will display the encoded or decoded message accordingly.
4.You can choose to continue or exit.
