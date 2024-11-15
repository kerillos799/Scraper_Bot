Base_url = "https://www.studypool.com/"
import hashlib
# driver path
driver_path = r"C:\Program Files\Google\Chrome\Application"

#Your mail and Pass
gmail = ""
pas = ""

#bot API and username
API = ""
Username = "@"

#bot Pass
bot_password = ""
hashed_pass = hashlib.md5(bot_password.encode())
hashed_pass = hashed_pass.digest()

initial = set()
active_users = set()
waiting_pass_users = set()
last_upd_id = None

cur_noti = 0
