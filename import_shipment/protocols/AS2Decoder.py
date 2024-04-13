class As2Decoder:

    fake_edi = """ISA*00*          *00*          *ZZ*SENDERID       *ZZ*RECEIVERID      *221115*1025*U*00401*000000123*0*P*>~
GS*PO*SENDERID*RECEIVERID*20221115*1025*12345*X*004010~
ST*850*0001~
BEG*00*SA*ACME123**20221115~
N1*ST*Widgets Inc.*92*12345~
IT1**10*EA*25.50**UP*01234567890123*IN*Widget Deluxe~
IT1**5*EA*12.00**UP*98765432109876*IN*Super Widget~
CTT*2*35.50~
SE*10*0001~
GE*1*12345~
IEA*1*000000123~
    """
    def __init__(self, cert, key):
        self.cert = cert
        self.key = key

    def decode(self, header, data):
        # use your cert, key to decode the encrypted data

        return self.fake_edi
