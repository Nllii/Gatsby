

#login ___________________________________________________________
def login_url():
    return('https://prod.gatsbyapp.org/api/v1/auth')


# to avoid the multiple logins:
def sessiontoken_url():
    return('https://prod.gatsbyapp.org/api/v1/auth/sessionToken')




# account ___________________________________________________________
def self_account_url():
    return('https://prod.gatsbyapp.org/api/v1/profile/self')


def portfolio_url(ApexAccount):

    return('https://prod.gatsby.financial/v2/accounts/{0}/portfolio/'.format(ApexAccount))



# stocks ___________________________________________________________
def quotes_url():
    return('https://prod.gatsbyapp.org/api/v1/stock/search')



def marketData(ticker):

    return('https://prod.gatsbyapp.org/api/v1/stock/{0}/marketData'.format(ticker))











# orders
def orders_url(ApexAccount):
    
    return('https://prod.gatsby.financial/v2/accounts/{0}/orders/'.format(ApexAccount))
    
def tradePaper(ApexAccount):
    return('https://prod.gatsby.financial/v2/accounts/{0}/tradePaper/'.format(ApexAccount))


def cancel_paperOrders(ApexAccount,order_id):
    return('https://prod.gatsby.financial/v2/accounts/{0}/tradePaper/{1}'.format(ApexAccount,order_id))



    # 'https://prod.gatsby.financial/v2/tradePaper/'
    
    
    # else:
    #     return('https://api.robinhood.com/orders/')
