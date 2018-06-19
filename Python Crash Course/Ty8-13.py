def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('kirushan', 'rasendran', level='beginner',\
     course='python', finished=False)

print(user_profile)
