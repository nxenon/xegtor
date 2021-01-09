# Xegtor Web Interface

Xegtor has a web interface to perform `scans` and `attacks` easily in your browser ,you can check the results in web interface.

GUI Usage
----

    1) sudo python3 xegtor.py --gui
    2) then open http://127.0.0.1:8484/ in your web browser
    3) default username and password is root
    3) go to scripts page from menu
    4) select a script and set the desired arguments
    5) start the attack
    
    finally read results in web interface 
    
Screenshots
----

![Screenshot](https://user-images.githubusercontent.com/61124903/101089818-f2511c80-35ca-11eb-83bd-30b1c17e3fab.png)

![Screenshot](https://user-images.githubusercontent.com/61124903/103424684-ec972880-4bc2-11eb-8838-6b2bfb47c09c.png)

![Screenshot](https://user-images.githubusercontent.com/61124903/103485772-07a9a880-4e0e-11eb-8e7b-0abf29dc0bfd.png)

Notes
----

- Default port number is **8484**
- Default username and password is **root**

Config File
----

The main configurations for web interface are in `GUI/config.json` file.

- Listening IP to connect
- Port number
- Credential to login

and ...

Documents
----

- [Docs Directory](https://github.com/xegtor/xegtor/tree/master/docs)