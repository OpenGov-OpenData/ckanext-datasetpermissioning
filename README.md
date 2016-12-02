# ckanext-datasetpermissioning

Requires ckanext-scheming

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
