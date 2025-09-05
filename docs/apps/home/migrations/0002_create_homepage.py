from django.db import migrations


def create_home(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    Page = apps.get_model("wagtailcore.Page")
    Site = apps.get_model("wagtailcore.Site")
    Home = apps.get_model("home.Home")

    # Delete the default home
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create content type for home model
    home_content_type, __ = ContentType.objects.get_or_create(
        model="home", app_label="home"
    )

    # Create a new home
    home = Home.objects.create(
        title="Home",
        draft_title="Home",
        slug="home",
        content_type=home_content_type,
        path="00010001",
        depth=2,
        numchild=0,
        url_path="/home/",
    )

    # Create a site with the new home set as the root
    Site.objects.create(hostname="localhost", root_page=home, is_default_site=True)


def remove_home(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    Home = apps.get_model("home.Home")

    # Delete the default home
    # Page and Site objects CASCADE
    Home.objects.filter(slug="home", depth=2).delete()

    # Delete content type for home model
    ContentType.objects.filter(model="home", app_label="home").delete()


class Migration(migrations.Migration):
    run_before = [
        ("wagtailcore", "0053_locale_model"),
    ]

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_home, remove_home),
    ]
