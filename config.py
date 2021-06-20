ROUTER_IP = '192.168.0.1'
ROUTER_PASS = "admin"
ON_WIFI = False
TOTAL_BW = 100/8 * 1024  # KBps
MAX_BLOCKS = 32
WAIT_BEFORE_UPDATE = 1 # seconds

# REQ_COOKIE only used if stats dont work (use your own cookie)
REQ_COOKIE = None
# REQ_COOKIE = "language=en; ecos_pw=YWRtaW4=1qw:language=en" #100
# REQ_COOKIE = "language=en; ecos_pw=YWRtaW4=cvb:language=en" #101
# REQ_COOKIE = "language=en; ecos_pw=YWRtaW4=mji:language=en" #103
# REQ_COOKIE = "language=en; ecos_pw=YWRtaW4=5gk:language=en" #104

# salts differ based on the local ip 
SALTS = {
	100:"1qw",
	101:"cvb",
	102:"tgb",
	103:"mji",
	104:"5gk",
}