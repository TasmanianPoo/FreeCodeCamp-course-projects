test_settings = {'theme': 'light'}


def add_setting(settings, new_setting):
    key = new_setting[0].lower()
    value = new_setting[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_2, new_setting_2):
    key_2 = new_setting_2[0].lower()
    value_2 = new_setting_2[1].lower()

    if key_2 in settings_2:
        settings_2[key_2] = value_2
        return f"Setting '{key_2}' updated to '{value_2}' successfully!"
    else:
        return f"Setting '{key_2}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings_3, del_setting):
    del_lower = del_setting.lower()
    key_3 = del_lower

    if key_3 in settings_3:
        del settings_3[key_3]
        return f"Setting '{key_3}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings_4):
    if not settings_4:
        return f"No settings available."

    results = f"Current User Settings:\n"


    for key, value in settings_4.items():
        key_capital = key.capitalize()
        results += f"{key_capital}: {value}\n"

    return results


print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(update_setting({'theme':'light'},('theme','dark')))
print(update_setting({'volume':'high'},('theme','dark')))
print(delete_setting({'theme': 'light'}, ('theme')))
print(delete_setting({'theme':'light'},('brightness')))
print(view_settings({'theme':'dark','notifications':'enabled','volume':'high'}))



