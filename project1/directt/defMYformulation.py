def ok(a,b):
    c=666
    return c

print(ok(10,20))
print('---------------------------------')
n1=2208
n2=2205
def marr(aplus,bplus):
    aplus=100
    print('%s plus %s'% (aplus,bplus))
    bplus+=100
    #return aplus#You run the formulation,find that if you use return ,it will change the argument of the real variables
print(n1,n2)
#The head environment is that the input variable can't be change like int or string
#Although in the formulation,the aplus is changing into 100 and bplus is refined to 2305,it doesn't change the n1 n2 anymore
'''
meanwhile ,if you don't add the line writing 'return',if won't change the aplus into 100 ,
instead ,it will remain the argument of input variables
'''
