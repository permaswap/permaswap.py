import requests
    
class LPClient:
    def __init__(self, lp_url='http://127.0.0.1:8081') -> None:
        self.lp_url = lp_url
        info = self.get_info()
        self.tokens = info['tokens']
        self.pools = info['pools']
    
    def get_info(self):
        return requests.get(f'{self.lp_url}/info').json()
    
    def get_lps(self):
        return requests.get(f'{self.lp_url}/info').json()['lps']

    def remove_lp(self, lpid):
        return requests.post(f'{self.lp_url}/remove_lp', json={'lpid': lpid}).json()
    
    def add_lp(self, lp):
        return requests.post(f'{self.lp_url}/add_lp', json=lp).json()