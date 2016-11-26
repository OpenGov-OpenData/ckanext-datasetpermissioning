from ckanext.datasetpermissioning import helpers

from ckan.plugins import SingletonPlugin, implements, ITemplateHelpers

class DatasetPermissioning(SingletonPlugin):
    implements(ITemplateHelpers)

    def get_helpers(self):
        return {'nonsysadmin_user_choices': helpers.nonsysadmin_user_choices}
