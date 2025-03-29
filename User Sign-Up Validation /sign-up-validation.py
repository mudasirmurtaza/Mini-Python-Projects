op_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]
#Function to validate the username
def validate_name(name):
    if (type(name)) == str and  (len(name) > 2):
        return True
    else:
        return False

validate_name("Mudasir")

#Function to validate the email
def validate_email(email):
    tlds = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]
    if "@" not in email:
        return False
    if not any (email.endswith(tlds) for tlds in top_level_domains ):
            return False
    else:
        return True

validate_email("mudasir@gmail")
