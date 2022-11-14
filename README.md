# permaswap.py
python sdk for permaswap

# usage

1. perpare everpay account

```python
api_server = 'https://api-dev.everpay.io'

# eth account
pk = ''
signer = everpay.ETHSigner(pk)

# or ar account
#signer = everpay.ARSigner('arweave-keyfile-xxx.json')
account = everpay.Account(api_server, signer)
```

2. permaswap

```python
router_host = 'wss://router0-dev.permaswap.network/'
swap = permaswap.Permaswap(router_host, account)
```

3. Query order

```python
# get_order('token_in', 'token_out', 'amount_in')
order = swap.get_order('tAR', 'tUSDC', 10**12)
print(order)
```

4. Place order

```python
result = swap.place_order(order)
print(result)
```
