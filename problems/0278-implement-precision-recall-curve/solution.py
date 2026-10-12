import numpy as np

def precision_recall_curve(y_true: list, y_scores: list) -> tuple:
    """
    Compute precision-recall pairs for different probability thresholds.
    
    Args:
        y_true: List of true binary labels (0 or 1)
        y_scores: List of predicted probabilities or confidence scores
    
    Returns:
        Tuple of (precisions, recalls, thresholds) where each is a list
    """
    # Your code here
    y_true = np.array(y_true)
    y_scores = np.array(y_scores)
    precs=[]
    recs=[]
    ths=[]
    for i in range(len(y_scores)):
        ths.append(y_scores[i].item())
        precs.append((np.sum((y_true==1)&(y_scores>=y_scores[i]))/np.sum(y_scores>=y_scores[i])).item())
        if np.sum(y_true==1)!=0:
            recs.append((np.sum((y_true==1)&(y_scores>=y_scores[i]))/np.sum(y_true==1)).item())
        else:
            recs.append(0.0)
    return precs, recs, ths