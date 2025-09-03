class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = {}

        for i in cpdomains:
            visits, site = i.split(" ")
            visits = int(visits)

            ## com, leetcode, discuss
            domain = site.split(".")[::-1]
            curr_domain = ""
            for d in domain:
                if len(curr_domain) == 0:
                    curr_domain = d
                else:
                    curr_domain = d + "." + curr_domain
                
                if curr_domain in domains:
                    domains[curr_domain] += visits
                else:
                    domains[curr_domain] = visits
        
        res = []
        for i in domains:
            res.append(str(domains[i]) + " " + i)
        return res


        