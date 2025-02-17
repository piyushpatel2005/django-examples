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


## Configurations

In order to be able to send email, you need to configure `.env` file in the project directory. An example of `.env` file is provided in the root directory as `env.example`. This is configured with Gmail as email provider in `settings.py` file and configurations might vary depending on your email provider.

In order to get `EMAIL_HOST_PASSWORD`, you need 2-step verification enabled and you need to create [App Password](https://myaccount.google.com/apppasswords) by creating new app.


- Adding comments (Displaying form as p, table, fieldset, etc., Using pluralize filter, Displaying form errors)
- Adding tagging for blog posts
- Recommend similar posts by matching tags, number of matched tags order by publish date descending limiting to 4
- Custom template tags and filters (simple_tag, inclusion_tag)
