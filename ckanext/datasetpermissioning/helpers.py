import ckan.logic as logic

def nonsysadmin_user_choices(field):
    """
    Return the non-sysadmin users as a choice list
    """
    user_list = logic.get_action('user_list')({},{})
    return [
        {'value': u['id'], 'label': u['display_name']+' ('+u['name']+')' }
        for u in user_list if not u['sysadmin']]
