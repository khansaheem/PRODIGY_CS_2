📷 Image Encryption Using Pixel Manipulation 🔒
Overview
This repository contains a Python-based tool for encrypting and decrypting images using pixel manipulation techniques.
Developed during my cybersecurity internship at Prodigy InfoTech,
this project demonstrates the application of cryptographic principles to secure images by altering their pixel values.

Features
Image Encryption: Uses XOR operations on each pixel's RGB values to encrypt the image.
Image Decryption: Reverts the encrypted image to its original state using the same XOR key.
Custom Key Input: Users can provide a custom key for encryption and decryption, ensuring flexibility and security.
Flexible I/O: Easily input images and save the encrypted/decrypted versions to specified paths.
User-Friendly: Simple and intuitive process to encrypt and decrypt images.

How It Works
Image Input: The program accepts an image file and a user-defined key.
Encryption: Each pixel’s RGB values are XORed with the provided key, transforming the image.
Decryption: Using the same key, the XOR operation is reversed to restore the original image.
Output: The encrypted and decrypted images are saved to specified directories.
