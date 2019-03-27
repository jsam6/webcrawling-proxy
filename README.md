# Project Title 

WebCrawling-proxy is a Python script that is used together with python request module.

## Objective

To implement proxies with request module.



## Getting Started

```python
import requests
from proxy import CrawlerProxy
from requests.exceptions import ProxyError

link = "insert url"

mCrawlerProxy = CrawlerProxy()

mProxy = mCrawlerProxy.getProxy(link)

mUserAgent = mCrawlerProxy.getUserAgent()

print(mProxy)

print(mUserAgent)

headers = {
    'User-Agent': str(mUserAgent),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# proxies and useragent generated will be used when requests are made.
respond = requests.get(url=link, proxies=mProxy, headers=headers)

print(respond)

while True
	try:
		# DO something
	except ProxyError:
        mProxy = mCrawlerProxy.getProxy(link) # Get new proxy if fail
        continue


```

### Prerequisites

Things to have before running script:

1. Python 2.7 and above
1. Python Requests module

```
pip install requests
import requests
```
