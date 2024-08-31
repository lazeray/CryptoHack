import base64
hexcode = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytecode = bytes.fromhex(hexcode)
print(base64.b64encode(bytecode))
