import requests

url = 'wp-admin'
credential_info = {'email': 'admin', 'password': '123456aA'}

wp_login = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
wp_admin = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
username = 'admin'
password = '123456aA'

with requests.Session() as s:
    headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
    datas={ 
        'log':username, 'pwd':password, 'wp-submit':'Log In', 
        'redirect_to':wp_admin, 'testcookie':'1'  
    }
    s.post(wp_login, headers=headers1, data=datas)
    resp = s.get(wp_admin)

    user_name = resp.content.decode('utf-8').split('<span class="display-name">')[1].split(r'</span>')[0]
    print(user_name)

