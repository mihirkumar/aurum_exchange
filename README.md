# Aurum
My concept non-custodial crpytocurrency exchange.
Read more about it here: https://medium.com/@mihir.kumar/aurum-ecf9f5e645b9

Here is the `pip freeze` output to see the dependencies for this project on a Windows 10 64 bit machine:

```
attrdict==2.0.1
base58==1.0.3
certifi==2019.6.16
chardet==3.0.4
cytoolz==0.10.0
eth-abi==2.0.0
eth-account==0.4.0
eth-hash==0.2.0
eth-keyfile==0.5.1
eth-keys==0.2.4
eth-rlp==0.1.2
eth-typing==2.1.0
eth-utils==1.6.2
hexbytes==0.2.0
idna==2.8
ipfshttpclient==0.4.12
jsonschema==2.6.0
lru-dict==1.1.6
multiaddr==0.0.8
netaddr==0.7.19
parsimonious==0.8.1
protobuf==3.9.0
pycryptodome==3.8.2
pypiwin32==223
pywin32==224
requests==2.22.0
rlp==1.1.0
six==1.12.0
toolz==0.10.0
urllib3==1.25.3
varint==1.0.2
web3==5.0.0
websockets==7.0
```

To run Aurum: run `python aurum.py`

The sample_output.png image can be used as a reference for what a successful trade execution would look like. It consists of statements reflecting the balance of the two parties before and after the trade which can be used to quickly verify that the trade occurred. If you follow the steps in the Medium article linked above, you would also be able to see the parties' token balances to ensure that a trade  took place.
