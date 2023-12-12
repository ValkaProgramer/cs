from random import randint
import hashlib

def generate_diffie_hellman_parameters():
    p = 3231700607131100730015351347782516336248805713348907517458843413926980683413621000279205636264016468545855635793533081692882902308057347262527355474246124574102620252791657297286270630032526342821314576693141422365422094111134862999165747826803423055308634905063555771221918789033272956969612974385624174123623722519734640269185579776797682301462539793305801522685873076119753243646747585546071504389684494036610497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
    g = 2
    private_a = randint(1, p - 1)
    private_b = randint(1, p - 1)
    public_a = pow(g, private_a, p)
    public_b = pow(g, private_b, p)
    common_secret_a = pow(public_b, private_a, p)
    common_secret_b = pow(public_a, private_b, p)

    return p, g, private_a, public_a, private_b, public_b, common_secret_a, common_secret_b

def derive_key(common_secret, salt):
    common_secret_bytes = common_secret.to_bytes((common_secret.bit_length() + 7) // 8, byteorder='big')
    key = hashlib.sha256(common_secret_bytes + salt).digest()
    return int.from_bytes(key, byteorder='big')


p, g, private_a, public_a, private_b, public_b, common_secret_a, common_secret_b = generate_diffie_hellman_parameters()

print("Alice Private Key:", private_a)
print("Bob Private Key:", private_b)
print("\nAlice Public Key:", public_a)
print("Bob Public Key:", public_b)
print("\nShared Secret Key (Alice):", common_secret_a)
print("Shared Secret Key (Bob):", common_secret_b)  