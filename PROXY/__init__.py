from ProxyChecking import ProxyChecker

checker = ProxyChecker()
print('Enter Your Proxy Information: ')
ip = input("IP: ")
port = input("PORT: ")
r = checker.check_proxy(f'{ip}:{port}')
print(r)