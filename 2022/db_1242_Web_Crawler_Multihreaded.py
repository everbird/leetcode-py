#!/usr/bin/env python3

from collections import deque
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = {startUrl}
        hostname = get_hostname(startUrl)

        with ThreadPoolExecutor(max_workers=16) as e:
            tasks = deque([e.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url in visited or get_hostname(url) != hostname:
                        continue

                    visited.add(url)
                    tasks.append(e.submit(htmlParser.getUrls, url))

        return list(visited)


def get_hostname(url):
    url_obj = urlparse(url)
    return url_obj.hostname
