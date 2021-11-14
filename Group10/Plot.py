import matplotlib.pyplot as plt

def plot(x, y):

    l1=range(0,x)
    l2=range(0,y)
    plt.plot(x=l1, y=l2)
    plt.save("./")
