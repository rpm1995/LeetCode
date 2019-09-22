class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        links = {}
        ans = []

        for link in cpdomains:
            placeholder = link.split()
            number = int(placeholder[0])
            site = str(placeholder[1])

            split_domains = site.split(".")
            domains = []

            for split in reversed(split_domains):
                if domains:
                    domains.append(split + "." + domains[-1])
                else:
                    domains.append(split)

            for domain in domains:
                if domain not in links:
                    links[domain] = 0
                links[domain] += number

        for name, count in links.items():
            ans.append(str(count) + " " + name)

        return ans
