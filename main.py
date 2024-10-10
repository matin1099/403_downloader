"""Target:
    an ipython app to use in Google colab and save in google drive.
"""
from  persepolis_lib.persepolis_lib import Download
 
def ez(link,out = None,download_path = '/home/matin-uni/codes/123',ip = None,
       port = None,proxy_user = None,proxy_passwd = None,proxy_type = None,
       download_user = None,download_passwd = None,header = None,
         user_agent = None, load_cookies = None,referer = None,
         segments = 64,):


    #importat Arguman to DICT
    dl_dict={'link': link,
             'out': out,
             'download_path':download_path,
             'ip': ip, 
             'port': port,
             'proxy_user': proxy_user, 
             'proxy_passwd': proxy_passwd,
             'proxy_type': proxy_type, 
             'download_user': download_user, 
             'download_passwd': download_passwd,
             'header': header, 
             'user_agent': user_agent, 
             'load_cookies': load_cookies, 
             'referer': referer}
    #Initate Download session
    ds = Download(add_link_dictionary=dl_dict,number_of_threads=segments,
                    timeout=5, retry=5,progress_bar=True,
                    threads_progress_bar=True)
    print("SO FAR SO GOOD!!!")
    ds.start()
ez('https://cdn.isna.ir/d/2024/10/10/3/63205667.jpg?ts=1728583090352')

    