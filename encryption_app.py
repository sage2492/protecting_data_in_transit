import streamlit as st
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from sympy import randprime
import os
import random
import math

st.set_page_config(
    page_title="Protecting Data in Transit",
    page_icon="🔐",
    layout="centered"
)


# ---------------- AES ----------------
def run_aes_demo(message):
    # Generate AES-256 secret key
    key = AESGCM.generate_key(bit_length=256)
    aes = AESGCM(key)

    # Convert message to bytes
    plaintext = message.encode()

    # Generate random 12-byte nonce
    nonce = os.urandom(12)

    # Encrypt the message
    ciphertext = aes.encrypt(nonce, plaintext, None)

    # Decrypt with the correct key
    decrypted = aes.decrypt(nonce, ciphertext, None)
    decrypted_text = decrypted.decode()

    # Demonstrate what happens with the wrong key
    wrong_key = AESGCM.generate_key(bit_length=256)
    wrong_aes = AESGCM(wrong_key)

    try:
        wrong_aes.decrypt(nonce, ciphertext, None)
        wrong_key_result = "Unexpectedly decrypted."
    except Exception:
        wrong_key_result = (
            "Decryption FAILED. The ciphertext cannot be decrypted "
            "without the correct secret key."
        )

    return {
        "key": key.hex(),
        "nonce": nonce.hex(),
        "ciphertext": ciphertext.hex(),
        "decrypted": decrypted_text,
        "wrong_key_result": wrong_key_result
    }


# ---------------- RSA ----------------
def gen_rsa_keys():
    p = randprime(1000, 10000)
    q = randprime(1000, 10000)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    return e, d, n


def rsa_encrypt(text, e, n):
    data = text.encode("utf-8")
    return [pow(byte, e, n) for byte in data]


def rsa_decrypt(encrypted, d, n):
    decrypted = bytes(pow(number, d, n) for number in encrypted)
    return decrypted.decode("utf-8")


# ---------------- WEB APP ----------------
st.title("Protecting Data in Transit")
st.subheader("Interactive Comparison of Symmetric and Asymmetric Encryption")

st.write(
    "Enter a message below and select an encryption method to see "
    "how AES and RSA transform plaintext into encrypted data and "
    "decrypt it back into its original form."
)

st.info(
    "How to use this demo: "
    "1) Choose AES or RSA  •  "
    "2) Enter a message  •  "
    "3) Click Encrypt & Decrypt  •  "
    "4) Compare the encrypted and decrypted results"
)

encryption_type = st.radio(
    "Choose an encryption method:",
    ["AES (Symmetric Encryption)", "RSA (Asymmetric Encryption)"]
)

message = st.text_input(
    "Enter text to encrypt:",
    placeholder="Confidential financial information"
)

if st.button("Encrypt & Decrypt"):

    if not message:
        st.warning("Please enter a message first.")

    elif encryption_type == "AES (Symmetric Encryption)":

        result = run_aes_demo(message)

        st.header("AES-256 Symmetric Encryption")

        st.write("**Original Text:**")
        st.code(message)

        st.write("**AES-256 Secret Key:**")
        st.code(result["key"])

        st.write("**Nonce:**")
        st.code(result["nonce"])

        st.write("**Encrypted Text:**")
        st.code(result["ciphertext"])

        st.write("**Decrypted Text:**")
        st.success(result["decrypted"])

        st.info(
            "Encryption Type: Symmetric — the same secret key is "
            "used for encryption and decryption."
        )

        st.subheader("Wrong Key Test")
        st.write("Attempting to decrypt with a different AES key...")
        st.error(result["wrong_key_result"])

    else:

        e, d, n = gen_rsa_keys()

        encrypted = rsa_encrypt(message, e, n)
        decrypted = rsa_decrypt(encrypted, d, n)

        st.header("RSA Asymmetric Encryption")

        st.write("**Original Message:**")
        st.code(message)

        st.write("**Public Key (e, n):**")
        st.code(f"({e}, {n})")

        st.write("**Private Key (d, n):**")
        st.code(f"({d}, {n})")

        st.write("**Encrypted Message:**")
        st.code(" ".join(map(str, encrypted)))

        st.write("**Decrypted Message:**")
        st.success(decrypted)

        st.info(
            "Encryption Type: Asymmetric — RSA uses a public key "
            "for encryption and a private key for decryption."
        )

        # ---------------- COMPARISON SECTION ----------------
st.divider()

st.header("AES vs. RSA: Key Differences")

st.write(
    "AES and RSA both protect data, but they use different approaches. "
    "AES uses one shared secret key, while RSA uses a public and private key pair."
)

comparison_data = {
    "Feature": [
        "Encryption Type",
        "Keys Used",
        "Speed",
        "Best Used For",
        "Primary Advantage",
        "Primary Limitation"
    ],
    "AES": [
        "Symmetric",
        "One shared secret key",
        "Faster",
        "Encrypting large amounts of data",
        "Fast and efficient",
        "The secret key must be shared securely"
    ],
    "RSA": [
        "Asymmetric",
        "Public and private key pair",
        "Slower",
        "Secure key exchange and authentication",
        "Does not require sharing a private key",
        "Slower and more computationally intensive"
    ]
}

st.table(comparison_data)

# ---------------- HYBRID ENCRYPTION SECTION ----------------
st.divider()

st.header("How AES and RSA Work Together")

st.write(
    "Modern communication systems often combine symmetric and asymmetric "
    "encryption instead of choosing only one method."
)

st.markdown("""
**1. RSA helps establish trust and exchange key information securely.**

The public key can be shared openly, while the private key remains protected.

**2. AES encrypts the actual data.**

Once a secure session is established, a symmetric key can be used to encrypt
larger amounts of information quickly and efficiently.

**3. The result combines the advantages of both methods.**

RSA provides secure key exchange, while AES provides fast encryption for the
data being transmitted.
""")

st.info(
    "This hybrid approach allows modern network communications to benefit "
    "from the security advantages of asymmetric encryption and the speed "
    "of symmetric encryption."
)

# ---------------- PROJECT INFORMATION ----------------
st.divider()

st.header("About This Project")

st.write(
    "This interactive application was developed for the Applied Data "
    "Communication project, Protecting Data in Transit: An Interactive "
    "Comparison of Symmetric and Asymmetric Encryption."
)

st.write(
    "The goal is to demonstrate how encryption protects information "
    "while it is transmitted across networks and to provide a hands-on "
    "comparison of AES symmetric encryption and RSA asymmetric encryption."
)

st.markdown("""
**Project Team**
- Sage Bruner
- Justin Thayer
""")

st.caption(
    "Applied Data Communication | West Virginia University"
)