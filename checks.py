# long_url = "http://www.example.com"

# long_url_wt_https = (
#     long_url
#     if long_url.startswith("https://")
#     else "https://" + long_url.split("//")[1]
#     if long_url.startswith("http://")
#     else "https://" + long_url
# )

# long_url_wt_http = (
#     long_url
#     if long_url.startswith("http://")
#     else "http://" + long_url.split("//")[1]
#     if long_url.startswith("https://")
#     else "http://" + long_url
# )

# long_url_wo_http = (
#     long_url.split("//")[1]
#     if (long_url.startswith("http://") or long_url.startswith("https://"))
#     else long_url
# )

# print(long_url_wt_https)
# print(long_url_wt_http)
# print(long_url_wo_http)

import os 
base_dir = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(base_dir, "urls.db")

# path = os.path.normpath(os.path.realpath(__file__))
# print(path)

print(base_dir)
print(file)
