import numpy as np

def gradient_descent(x,y):
  m_curr = c_curr = 0   # Linear equation --> y = mx + c
  learning_rate = 0.08
  n = len(x)        # Number of terms in dependent variable set
  iterations = 1000;         #Maximum number of steps
  
  plt.scatter(x, y, color='red', marker='+', lindeWidth='5')

  for i in range(iterations):
      y_predicted = c_curr + m_curr * x
      cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
      m_curr_d = -(2/n)*sum(x*(y-y_predicted))
      c_curr_d = -(2/n)*sum(y-y_predicted)
      m_curr = m_curr - (learning_rate * m_curr_d)
      c_curr = c_curr - (learning_rate * c_curr_d)
      print ("m {}, b {}, cost {} iteration {}".format(m_curr,c_curr,cost, i))


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])    

gradient_descent(x,y)