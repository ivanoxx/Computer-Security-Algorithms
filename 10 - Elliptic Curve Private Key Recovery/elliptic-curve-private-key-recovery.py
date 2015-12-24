# Elliptic Curve Private Key Recovery
# https://id0-rsa.pub/problem/10/

# Resources
# https://id0-rsa.pub/forum/problem/10/
# http://wstein.org/edu/2007/spring/ent/ent-html/node89.html
# http://crypto.stackexchange.com/questions/3907/how-does-one-calculate-the-scalar-multiplication-on-elliptic-curves
# https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/


class Elliptic_Curve():

    @property
    def G(self):
        return (self.G_0, self.G_1)

    @property
    def Q(self):
        return (self.Q_0, self.Q_1)


if __name__ == '__main__':
    A = Elliptic_Curve()
    # ELliptic curve parameters
    A.p = int(
        '0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff', 16)
    A.a = int('-0x3', 16)
    A.b = int(
        '0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b', 16)
    A.G_0 = int(
        '0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296', 16)
    A.G_1 = int(
        '0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5', 16)
    A.Q_0 = int(
        '0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe', 16)
    A.Q_1 = int(
        '0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562', 16)

    # Steps:
    # To compute the public key from the private key requires elliptic curve
    # arithmetic, namely multiplying a base point G by the scalar d, which
    # yields the point Q. Finding d given Q and G reduces to the discrete log
    # problem. Luckily, in this problem d was chosen to be a small value.

    # Given the elliptic curve parameters (NIST curve P-256) and public key
    # find the value of the private key
    pass
