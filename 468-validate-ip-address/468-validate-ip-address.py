class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s): # smart way of checking leading zeros
            #  If there is a character in s, 
            # then int(s) would throw an exception which would be caught by the except block. The function will return False in this case
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False
        
        def isIPv6(s): # int(string, base), covert to 16-base
            try: return len(s) <= 4 and int(s, 16) >= 0
            except: return False        
            
        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"
        return "Neither"



    # # Internet Protocol version 4
# # Note that the code below validates the real-life IPv4, and real-life IPv6. 
# # It will not work for this problem because the problem validates not real-life but "simplified" versions of IPv4 and IPv6.
# from ipaddress import ip_address, IPv6Address
# class Solution:
#     def validIPAddress(self, IP: str) -> str:
#         try:
#             return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
#         except ValueError:
#             return "Neither"        