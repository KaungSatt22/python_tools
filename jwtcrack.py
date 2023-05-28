import jwt
import textwrap
import argparse

class JwtCrack:
    def __init__(self,token,wordlist,algo_type):
        self.token = token
        self.wordlist = wordlist
        self.algo_type = algo_type
    def crack(self):
        print('\033[1m' + "---------------Cracking -------------")
        with open(self.wordlist , 'rb') as wl:
            for password in wl:
                password = password.strip().decode()
                try:
                    jwt.decode(self.token,password,algorithms=[self.algo_type])
                    print('\033[92m' +f'[*] Successed! Token decode Secrect {password} ')
                    break
                except jwt.InvalidSignatureError:
                    print('\033[91m' + f'[-]Invalid Token {password}')
                except jwt.ExpiredSignatureError:
                    print('\033[91m' + f'[-]Expired Token {password}')
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="JWT Secrect Signature Crack",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example : 
            python3 jwtcrack.py -t jwt_token -w wordlist -a algorithm
        ''')
    )
    parser.add_argument("-t" , "--token" , help="JWT TOKEN" ,required=True)
    parser.add_argument("-w" , "--wordlist" , help="wordlist" ,required=True)
    parser.add_argument("-a" , "--algorithm" , help="Provide Algorithm" ,required=True)
    args = parser.parse_args()
    crack = JwtCrack(args.token,args.wordlist,args.algorithm)
    crack.crack()