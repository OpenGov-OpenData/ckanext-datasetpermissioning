# ckanext-datasetpermissioning

This CKAN extension allows private datasets to be viewed by an extra
set of users that may be selected when creating the dataset.

It provides a scheming choices helper that returns a list of
non-syadmin users (sysadmin users can see all private datasets anyway)
to give read access.

Requires ckanext-scheming and the IPermissionLabels feature in recent
version of CKAN.

Config settings:

```ini
ckan.plugins = datasetpermissioning
```


Add a this field to your dataset schema:

```yaml
#  extra view-only permission on this dataset for users selected here
- field_name: view_users
  label: View Permissions
  preset: multiple_select
  choices_helper: nonsysadmin_user_choices
  display_snippet: null
```
