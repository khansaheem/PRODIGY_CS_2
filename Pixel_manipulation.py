from PIL import Image
import os

def encrypt_decrypt_image(image_path, key, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r_enc = r ^ key
                g_enc = g ^ key
                b_enc = b ^ key
                pixels[x, y] = (r_enc, g_enc, b_enc)

        img.save(output_path)
        print(f"Image saved successfully at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    image_path = r"C:\Users\khans\OneDrive\Desktop\download.jfif"

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path)

    output_path_encrypted = os.path.join(desktop_path, "encrypted_image.jpg")
    output_path_decrypted = os.path.join(desktop_path, "decrypted_image.jpg")

    key = 150  

    print("Encrypting the image...")
    encrypt_decrypt_image(image_path, key, output_path_encrypted)

    print("Decrypting the image...")
    encrypt_decrypt_image(output_path_encrypted, key, output_path_decrypted)

if __name__ == "__main__":
    main()
