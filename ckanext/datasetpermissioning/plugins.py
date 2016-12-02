from ckanext.datasetpermissioning import helpers

from ckan.plugins import (SingletonPlugin, implements, ITemplateHelpers,
    IPermissionLabels)
from ckan.lib.plugins import DefaultPermissionLabels

class DatasetPermissioning(SingletonPlugin, DefaultPermissionLabels):
    implements(ITemplateHelpers)
    implements(IPermissionLabels)

    def get_helpers(self):
        return {'nonsysadmin_user_choices': helpers.nonsysadmin_user_choices}

    def get_dataset_labels(self, dataset_obj):
        view_users = json.loads(dataset_obj.extras.get('view_users', '[]'))
        labels = super(DatasetPermissioning, self).get_dataset_labels(dataset_obj)
        return labels + [u'view-%s' % u for u in view_users]

    def get_user_dataset_labels(self, user_obj):
        labels = super(DatasetPermissioning, self).get_user_dataset_labels(user_obj)
        if user_obj:
            labels.append(u'view-%s' % user_obj.id)
        return labels
