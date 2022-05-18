#!/usr/bin/env python
# coding: utf-8

# In[2]:


def optimization_function(param):
    global X, save_data, save_input, save_array, control
    ti = save_time[-1]
    tf = save_time[-1] + 1/om
    save_time.append(tf)
    def f(x, t):
        return Harvest(x,t,param) 
    x= odeint(f, X, np.linspace(ti,tf,num=5000))
    X=x[-1]
    clear_output(wait=True)
    save_data.append(X[3])
    save_input.append(param)
    new_points = [[a[0], a[1]] for a in x]
    save_array += new_points
    print(save_array)
    plt.plot([x[0] for x in save_array], [x[1] for x in save_array])
    plt.title(f'{(X[3])}, {param, R}')
    plt.show()
    return (X[3])


# In[ ]:




