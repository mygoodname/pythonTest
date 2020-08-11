import ahttp

urls = [ f"https://movie.douban.com/top250?start={i*25}" for i in range(10) ]
reqs = [ahttp.get(url) for url in urls]
resps = ahttp.run(reqs)
print(resps)
print(resps[0].text)