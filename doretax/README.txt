"""
Dore' and Company's django website project.

dev site: doretax.decode72.com
current site: doretax.com

last modified: 2011.09.28
"""

Notable dependencies:
    pyyaml
    gondor (if you want to deploy)
    * for a full list, look at requirements.txt

To install users and business info locally:
    $ python manage.py syncdb --noinput
    this will make a Decode72 and Lloyd user. Lloyd's password is 'password'

To load old site data locally:
    $ python manage.py loaddata biz/fixtures/old_site_data.yaml

If you don't know what Gondor instance label to use:
    primary
    
If you don't know what revision to use:
    default

To deploy to gondor without touching database:
    $ gondor deploy <instance_label> <hg_revision>
    e.g. $ gondor deploy primary default

To deploy to gondor and wipe database and install fixtures:
    $ gondor manage <instance_label> database:clear
    $ gondor deploy <instance_label> <hg_revision>
    $ gondor run <instance_label> loaddata biz/fixtures/old_site_data.yaml

