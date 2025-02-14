# Blog Application

Super user: admin
Password: Admin@123!

- Customize admin site
- working with QuerySet
- Customize model manager
- Using namespace in templates
- Create get_absolute_url method
- Adding SEO friendly URLs
- Share a post using Email
- Adding comments


## Configurations

In order to be able to send email, you need to configure `.env` file in the project directory. An example of `.env` file is provided in the root directory as `env.example`. This is configured with Gmail as email provider in `settings.py` file and configurations might vary depending on your email provider.

In order to get `EMAIL_HOST_PASSWORD`, you need 2-step verification enabled and you need to create [App Password](https://myaccount.google.com/apppasswords) by creating new app.