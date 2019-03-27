import requests, re, random, sys, logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class CrawlerProxy:
    def getProxy(self, url):
        url = url
        # Use Elite > Anonymous > Transparent Proxy
        proxy_req = requests.get("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list")

        pattern = r'{.*?}'
        mSuccess = False
        prxList = re.findall(pattern, proxy_req.text)
        while mSuccess == False:
            prx = random.choice(prxList)
            typeHead = re.search(r'"type":.*?"(.*?)"', prx)
            host = re.search(r'\"host\"\:.*?\"(.*?)\"', prx)
            port = re.search(r'"port":.*?(\d+)', prx)

            typeHead = (typeHead.group(1))
            host = (host.group(1))
            port = (port.group(1))

            uAgent = self.getUserAgent()

            headers = {
                'User-Agent': str(uAgent),
            }
            proxies = {
              str(typeHead): str(host) + ":" + str(port),
            }
            try:
                req = requests.get(url, proxies=proxies, headers=headers)
                if req.status_code == 200:
                    mSuccess = True
                else:
                    logging.info("Proxy unavailable : " + str(proxies))
                    mSuccess = False
            except Exception as e:
                logging.info("Proxy unavailable : " + str(proxies))
                pass

        return(proxies)


    def getUserAgent(self):
        userAgent_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
            "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        ]
        ua = random.choice(userAgent_list)

        return ua

