import os
import sys
import base64

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
    encrypted_bytes = bytes([image_byte ^ key for image_byte in image_bytes])
    encrypted_image_path = os.path.splitext(image_path)[0] + '_encrypted.png'
    with open(encrypted_image_path, 'wb') as f:
        f.write(encrypted_bytes)
    return encrypted_image_path

if __name__ == '__main__':
    image_path = sys.argv[1]
    key = int(sys.argv[2])
    encrypted_image_path = encrypt_image(image_path, key)
    print(f'Encrypted image saved to {encrypted_image_path}')
