

#login
def login_url():
    return('https://prod.gatsbyapp.org/api/v1/auth')


# to avoid the multiple logins:
def sessiontoken_url():
    return('https://prod.gatsbyapp.org/api/v1/auth/sessionToken')









#stocks
def quotes_url():

    return('https://prod.gatsbyapp.org/api/v1/stock/search')


