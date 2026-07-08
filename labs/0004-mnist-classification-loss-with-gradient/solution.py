import numpy as np

def loss_function(preds: np.ndarray, target: np.ndarray, reduction: str = "mean", **kwargs):
    """
    preds:     [N, C] softmax probabilities (rows sum to 1)
    target:    [N]    class indices (int64)
    reduction: how to aggregate per-sample losses:
               "mean" → average over batch (gradient scaled by 1/N)
               "sum"  → sum over batch (gradient unscaled)
               "none" → return per-sample loss vector (no aggregation)
    **kwargs:  absorbs any extra arguments from the training harness

    Returns: (loss, grad) where grad has the same shape as preds
    """
    # Your implementation here
    assert preds.ndim == 2
    n,c = preds.shape
    assert target.shape==(n,)
    assert np.issubdtype(target.dtype, np.integer)
    assert np.all(target >= 0) and np.all(target < c)

    y=np.zeros_like(preds)
    y[np.arange(n), target] = 1.0

    eps=1e-12
    p=np.clip(preds, eps, 1.0)

    per_sample = -np.sum(y*np.log(p), axis = 1)

    grad = (-(y/p))

    if reduction=="mean":
        loss = float(per_sample.mean()); scale = 1.0/n
    elif reduction=="sum":
        loss = float(per_sample.sum()); scale = 1.0
    else:
        loss = per_sample; scale = 1.0

    return loss, grad