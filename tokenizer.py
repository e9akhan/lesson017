import requests

def tokenizer(target, prefix, suffix):
    return [url[url.index(prefix):url.index(suffix, url.index(prefix)+1)+len(suffix)] for url in target.split()]

def get_request(url):
    response = requests.get(url, timeout=10)
    return response.text

def get_url_list(url):
    url_list = []

    webpage_source = get_request(url=url)

    for target in webpage_source.split():
        if 'href' in target and 'http' in target:
            url = tokenizer(target=target, prefix='http', suffix='"')
            for link in url:
                url_list.append(link[:-1])

    return url_list


if __name__ == '__main__':
    # print(tokenizer('url="http://yahoo.com"', 'http', ''))
    print(get_url_list('https://httpbin.org'))