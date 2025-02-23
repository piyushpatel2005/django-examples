# Social Media Application

- Create authentication and login system
- Create super user

```plaintext
Username: admin
Password: Admin@123!

Username: testuser
Email: testuser@example.com
Password: PassUser123
```

- Class based authentication views
- Use Login logout views
- Create dashboard for the user and add logout links
- Create password change
- Create password reset
- Add Email backend. This uses console email backend
- Add User profile update feature
- Add ability to display quick session messages using Django messages framework
- Add custom Email backend to authenticate using email address
- Prevent users from using an existing email address
- Update your `/etc/hosts` file to serve the traffic to `mysite.com` domain. Some hosts need valid hosts to work propertly for OAuth2. Use the command below to run local server. Django extensions will generate a key and certificate automatically.

```bash
python manage.py runserver_plus --cert-file cert.crt
```

- Add social authentication using Google
- Add ability to create profile when using social authentication and add it to the social auth pipeline in `settings.py`