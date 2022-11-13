import argparse
from ast import Try
from distutils.log import error
from cryptography.fernet import Fernet

def encrypt_string(args):
    try:
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt(bytes(args.text[0],'utf-8'))
        
        print("###############################")
        print("###__+^ Token Encrypted ^+__###")
        print("###############################\n")
        print(f"Key: {key.decode()}")
        print(f"Token: {token.decode()}\n")
        print(f"Text: {f.decrypt(token).decode()}\n")
        print("*Note: Keep 'Key' and 'Token' somewhere secret")
        
    except Exception:
        print("Error: Invalid text or key!\n")
    

def decrypt_token(args):
    
    try:
        key = bytes(args.key,'utf-8')
        f = Fernet(key)
        decrypt_txt = f.decrypt(bytes(args.text[0],'utf-8'))

        print("###############################")
        print("###__+^ Token Decrypted ^+__###")
        print("###############################\n")
        print(f"Text: {decrypt_txt.decode()} \n")

    except Exception:
        print("Error: Invalid token or key!\n")

def main():
    startuptxt = """
   ___          _____                 __                               __          _____ __    ____
  / _ \ __ __  / ___/____ __ __ ___  / /_ ___  ___ _ ____ ___ _ ___   / /  __ __  / ___// /   /  _/
 / ___// // / / /__ / __// // // _ \/ __// _ \/ _ `// __// _ `// _ \ / _ \/ // / / /__ / /__ _/ /  
/_/    \_, /  \___//_/   \_, // .__/\__/ \___/\_, //_/   \_,_// .__//_//_/\_, /  \___//____//___/  
      /___/             /___//_/             /___/           /_/         /___/                     
      
Desc: encrypt & decrypt string using cryptography.io (Keep your secret forever!)
Author: afif-dev https://github.com/afif-dev
    """
    print(startuptxt)

    parser = argparse.ArgumentParser(prog='py-cryptography-cli', description='Encrypt & decrypt string.')
    parser.add_argument('text', metavar='text', type=str, nargs=1, help="encrypt/decrypt string")
    parser.add_argument('-k', '--key', metavar='xxxx', type=str, nargs='?', default = None, help='set key for cryptography')

    args = parser.parse_args()
    if args.key != None and args.text != None:
        decrypt_token(args)
    elif args.text != None:
        encrypt_string(args)

if __name__ == "__main__":
    main()
