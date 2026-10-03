# Protecting Data in Transit

## An Interactive Comparison of Symmetric and Asymmetric Encryption

This project was developed for **Applied Data Communication at West Virginia University**. It demonstrates how symmetric and asymmetric encryption can be used to protect information transmitted across networks through an interactive comparison of **AES (Advanced Encryption Standard)** and **RSA (Rivest-Shamir-Adleman)**.

## Live Interactive Application

**Try the application here:**

https://protecting-data-in-transit.streamlit.app

The application allows users to enter their own message, select an encryption method, and observe the message as it moves from plaintext to encrypted data and back to decrypted plaintext.

## AES Symmetric Encryption

The AES demonstration shows how symmetric encryption uses a shared secret key.

Users can observe:

- Original plaintext
- AES-256 secret key
- Nonce
- Encrypted ciphertext
- Decrypted plaintext
- A wrong-key test demonstrating what happens when decryption is attempted without the correct secret key

## RSA Asymmetric Encryption

The RSA demonstration shows how asymmetric encryption uses a public and private key pair.

Users can observe:

- Original plaintext
- Public key
- Private key
- Encrypted message
- Decrypted plaintext

## AES vs. RSA

The application also compares the two encryption approaches, including their key structures, relative speed, advantages, limitations, and common uses.

AES is well suited for efficiently encrypting larger amounts of data, while RSA demonstrates how public-key cryptography can support secure key exchange and authentication.

## How They Work Together

Modern communication systems can combine symmetric and asymmetric encryption rather than relying exclusively on one approach.

Asymmetric cryptography can help establish trust and securely exchange key information, while symmetric encryption can efficiently protect the larger amounts of data transmitted during a communication session.

This hybrid approach combines the advantages of both encryption methods.

## How to Use the Application

1. Open the live application.
2. Choose **AES** or **RSA**.
3. Enter a message.
4. Select **Encrypt & Decrypt**.
5. Review the plaintext, encrypted output, keys, and decrypted result.
6. Switch encryption methods to compare the results.

## Project Team

**Sage Bruner**  
**Justin Thayer**

Applied Data Communication  
West Virginia University
