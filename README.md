# Django examples

Django example projects for learning and exploring

- Django history
- Django overview with features

## Creating First project

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install django
```
Once Django is insatlled, you can use `django-admin` to create the first project.

```shell
django-admin startproject riff_mates
```

This creates a directory structure like this.

```
riff_mates/
├── manage.py
└── riff_mates
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

You can start the development server with the following command.

```shell
python manage.py runserver
```

## Django Apps

Django apps are directories that contain Python modules, templates, and static files.  You can use `manage.py` to create new apps.

```shell
python manage.py startapp home
```

This creates a directory structure like this.

```
home
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
``` 

There will be unapplied migrations which you can apply using `python manage.py migrate`.

## Templates

- Tags and filters
- Templates are configured in `settings.py`

## ORM

- Define Model
- Create Migrations

```shell
python manage.py makemigrations bands
python manage.py migrate
python manage.py dbshell
```

If you check table names, they are usually named as `app_name_modelname`.

```shell
.tables
.help
.schema bands_musician
.quit
```

### Creating and Querying Data with ORM

```shell
python manage.py shell
```

- `create` and `save`
- `get`, `all`, `filter`, `count`, `exists`
- `update`, `delete`

### Field lookups

- `exact`, `iexact`, `contains`, `icontains`, `in`, `gt`, `gte`, `lt`, `lte`, `startswith`, `endswith`, `istartswith`, `iendswith`. These are specified with the `filter()` method where they are prefixed with `__`. For example, `Musician.objects.filter(birth__get=date(1990, 1, 1))`.

- Using separate `urls.py` file for each app
- Create listing page
- Popular field options
- Common fields for models `EmailField`, `URLField`, `SlugField`, `TextField`, `IntegerField`

### Pagination

- How to implement pagination

## Fixtures

```shell
python manage.py dumpdata > fixtures.json
python manage.py loaddata fixtures.json
```

## Django Admin

- Create admin user

```shell
python manage.py createsuperuser
```

- Modifying display of the listings
- Adding search functionality
- Adding filters
- Facets
- Cross-linking related objects
- Model Meta properties (ordering, indexes, permissions, etc.)
- Uniqueness (unique_together)
- Modifying object names in Django Admin (verbose_name, verbose_name_plural)

## User Management

- Authentication and Authorization
- Middleware (comes between route and the view)
- User Profiles
- Restricting access to views (`@login_required`)
- Adding logout link
- Creating User Profiles using signals


