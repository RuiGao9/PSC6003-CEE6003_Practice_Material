def gfit(true,pred,type_statistic='1',residual='Yes'):
    import numpy as np
    import pylab
    import matplotlib.pyplot as plt
    '''
    true: it supposed to be the observations
    pred: it supposed to be the estimations from (ML) models
    type_statistic: folow the information below to see which one you need
    residual: if "Yes", the residual plot will be provided, otherwise, no residual plot
    type_statistic='1': Root Mean Square Error - RMSE (default)
    type_statistic='2': Relative Root Mean Square Error - RRMSE
    type_statistic='3': Mean Absolute Error - MAE
    type_statistic='4': Correlation Coefficient - r
    type_statistic='5': Coefficient of Determination - R2
    type_statistic='6': Coefficient of Efficiency - E
    type_statistic='7': Mean Squared Error - MSE
    '''
    # Size of two vectors should be the same
    # error will come up if the size does not match
    if true.shape == pred.shape:
        pass
    else:
        print("\nError! The size of vector 1 does not match vector 2!\n")
        
    # Basic information about inputs
    num_element = len(true)
    diff = true - pred
    mean_true = true.mean()
    mean_pred = pred.mean()
    
    # residual plot (optional)
    if residual=='Yes':
        plt.figure(figsize=(5, 2.5))
        plt.scatter(range(1, 1+len(true)),diff)
        plt.plot(range(1, 1+len(true)),[0]*len(true),'r--')
        plt.xlim(0, len(true)+1)
        plt.ylabel("Residual")
        plt.show()
    else:
        pass

    # Calculate the goodness-of-fit statistics
    # RMSE (root mean square error)
    if type_statistic == '1':
        out = np.sqrt((diff**2).mean())
    # RRMSE (relative root mean square error)
    elif type_statistic == '2':  
        out = np.sqrt((diff**2).mean())
        out = out/mean_true*100
    # MAE (mean absolute error)
    elif type_statistic == '3':
        out = (abs(diff)).mean()
    # r (correlation coefficient)
    elif type_statistic == '4': 
        tmp = np.corrcoef(true,pred)
        out = tmp[0,1]
    # R2 (coefficient of determination)
    elif type_statistic == '5': 
        tmp = np.corrcoef(true,pred)
        tmp = tmp[0,1]
        out = tmp**2    
    # E (coefficient of efficiency)
    elif type_statistic == '6':
        out = 1 - (diff**2).sum()/((true - mean_true)**2).sum()
    # MSE (mean squared error)
    elif type_statistic == '7':
        out = diff**2
        out = out.mean()
        
    return(out)  