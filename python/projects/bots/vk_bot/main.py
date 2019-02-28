from data import data_get
def main():
    data_get(URL = 'https://api.vk.com/'    ,\
            method = 'method/'              ,\
            function = 'users.get?'         ,\
            user_ids = 'user_ids=id496481135&'         ,\
            access_token = 'access_token=550b576a3be3cdadb493177dd3ff4cef4450abf8d11634f7a50e7763fd5391caf794e31e6585c0931d13b&',\
            version = 'v=5.92')
if __name__ == '__main__': main()
https://api.vk.com/method/message.send?user_ids=id496481135&message=hello&title=lol&access_token=550b576a3be3cdadb493177dd3ff4cef4450abf8d11634f7a50e7763fd5391caf794e31e6585c0931d13b
https://api.vkontakte.ru/method/messages.send?user_id={receiver_vk_id}&message={vk_msg}&title={vk_msg_title}&access_token={received_access_token}
