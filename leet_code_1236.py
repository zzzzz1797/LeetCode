"""
    给定一个链接 startUrl 和一个接口 HtmlParser，请你实现一个网络爬虫，以实现爬取同startUrl拥有相同域名标签的全部链接。该爬虫得到的全部链
接可以任何顺序 返回结果。

    你的网络爬虫应当按照如下模式工作：
        自链接 startUrl 开始爬取
        调用 HtmlParser.getUrls(url) 来获得链接url页面中的全部链接
        同一个链接最多只爬取一次
        只输出 域名 与 startUrl 相同 的链接集合


    HtmlParser 接口定义如下：
        interface HtmlParser {
            // 返回给定 url 对应的页面中的全部 url 。
            public List<String> getUrls(String url);
        }
        下面是两个实例，用以解释该问题的设计功能，对于自定义测试，你可以使用三个变量  urls, edges 和 startUrl。注意在代码实现中，你只可
    访问 startUrl ，而 urls 和 edges 不可以在你的代码中被直接访问。

"""
from typing import List


class HtmlParser(object):
    def getUrls(self, url):
        """
        :type url: str
        :rtype List[str]
        """
        pass


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host_name = "http://" + startUrl.split("/")[2]

        result = []
        flag = set()

        def _dfs(url):
            if not url.startswith(host_name):
                return
            if url in flag:
                return
            flag.add(url)
            result.append(url)
            for relation_url in htmlParser.getUrls(url):
                _dfs(relation_url)

        _dfs(startUrl)
        return result
