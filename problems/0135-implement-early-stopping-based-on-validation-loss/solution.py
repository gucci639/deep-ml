from typing import Tuple

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    # Your code here
    best_loss = val_losses[0]
    best_epoch = 0
    wait = 0
    for epoch in range(1, len(val_losses)):
        if val_losses[epoch] < best_loss - min_delta:
            best_loss = val_losses[epoch]
            best_epoch = epoch
            wait = 0 
        else:
            wait+=1
        if wait >= patience:
            return epoch, best_epoch
    return len(val_losses)-1, best_epoch
    