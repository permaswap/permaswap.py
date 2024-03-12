# permaswap.py
python sdk for permaswap

# install

```python
pip install permaswap
```

# usage

1. perpare everpay account

```python
import everpay
api_server = 'https://api-dev.everpay.io'

# eth account
pk = ''
signer = everpay.ETHSigner(pk)

# or ar account
#signer = everpay.ARSigner('arweave-keyfile-xxx.json')
account = everpay.Account(api_server, signer)
```

2. init permaswap

testnet: 'wss://router-dev.permaswap.network/'
mainnet: 'wss://router.permaswap.network/'

```python
router_host = 'wss://router-dev.permaswap.network/'
swap = permaswap.Swap(router_host, account)
```

3. query order

```python
import permaswap
# get_order('token_in', 'token_out', 'amount_in')
# sell 1 tar for tusdc
order = swap.get_order('tAR', 'tUSDC', 10**12)
print(order)
```

4. place order

```python
result = swap.place_order(order)
print(result)
```
