import numpy as np

def engram_context_gating(h: np.ndarray, e: np.ndarray, W_K: np.ndarray, W_V: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Implement Engram context-aware gating mechanism.
    
    Args:
        h: Hidden states of shape (T, d)
        e: Retrieved memory embeddings of shape (T, d_mem)
        W_K: Key projection matrix of shape (d_mem, d)
        W_V: Value projection matrix of shape (d_mem, d)
        eps: Small constant for numerical stability in RMSNorm
    
    Returns:
        Gated output of shape (T, d)
    """
    d=h.shape[-1]
    k=e@W_K
    v=e@W_V

    def rms_norm(x):
        rms = np.sqrt(np.mean(x**2, axis=-1, keepdims=True) + eps)
        return x/rms
    
    h_norm=rms_norm(h)
    k_norm=rms_norm(k)

    def sigmoid(x):
        x=np.clip(x, -500, 500)
        return 1/(1+np.exp(-x))
    
    dot_product=np.sum(h_norm*k_norm, axis=-1, keepdims=True)

    a_t=sigmoid(dot_product/np.sqrt(d))
    
    return a_t*v