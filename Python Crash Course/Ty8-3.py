def make_shirt(size='large', message='I love python'):
    """ prints the size of the t-shirt, and the message on the t-shirt """
    print("\nSize of your t-shirt is :" + size)
    print("Message that will be printed on t-shit : " + message)


make_shirt("medium", "Hello World!")  # positional arguments
make_shirt(message='StackOverFloww!!', size="XL")  # keyword arguments
make_shirt('large')
make_shirt('medium')
make_shirt('Extra Small', 'I love C++')
