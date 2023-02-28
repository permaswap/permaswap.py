import permaswap
import everpay
api_server = 'https://api-dev.everpay.io'
router_host = 'wss://router0-dev.permaswap.network/'

#put your private key of eth account
pk = ''
signer = everpay.ETHSigner(pk)

#ar account
#signer = everpay.ARSigner('arweave-keyfile-xxx.json')
account = everpay.Account(api_server, signer)

swap = permaswap.Swap(router_host, account)

# sell 1 tar to get tusdc
order = swap.get_order('tAR', 'tUSDC', 10**12)
print(order)

result = swap.place_order(order)
print(result)