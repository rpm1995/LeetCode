# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def getDomain(url):
            return url.split("http://")[1].split("/")[0]

        main_domain = getDomain(startUrl)
        hosts = [startUrl]
        ans = []
        visited = set()

        while hosts:

            host = hosts.pop()
            domain = getDomain(host)

            if domain == main_domain:
                if host not in visited:
                    ans.append(host)
                    hosts.extend(htmlParser.getUrls(host))

                    visited.add(host)

        return ans
