import numpy as np
import matplotlib.pyplot as plt
NUM_ROLLS=1000
NUM_DICE=1
if NUM_DICE == 1:
    rolls=np.random.randint(1,7,size=NUM_ROLLS)
else:
    diec1=np.random.randint(1,7,size=NUM_ROLLS)
    diec2=np.random.randint(1,7,size=NUM_ROLLS)
    rolls=diec1+diec2
unique,counts=np.unique(rolls,return_counts=True)
probabilities=counts/NUM_ROLLS
print("="*40)
print(f"       DICE ROLL SIMULATOR ({NUM_ROLLS} rolls)")
print("="*40)
print(f"Mean        : {np.mean(rolls):.4f}")
print(f"Median      : {np.median(rolls):.4f}")
print(f"Std Dev     : {np.std(rolls):.4f}")
print(f"Min / Max   : {np.min(rolls)} / {np.max(rolls)}")
print("="*40)
print(f"{'Face':<10} {'Count':<10} {'Probability'}")
print("-" * 40)
for face,count,prob in zip(unique,counts,probabilities):
    bar="█"*int(prob*100)
    print(f"{face:<10} {count:<10} {prob:.4f}  {bar}")
print("-" * 40)
if NUM_DICE==1:
    exp_prob=1/6
else:
    None
plt.figure(figsize=(10,6))
bars=plt.bar(unique,probabilities,color='steelblue',alpha=0.8,edgecolor='black')
max_idx=np.argmax(probabilities)
bars[max_idx].set_color('tomato')
if NUM_DICE == 1:
    plt.axhline(y=1/6, color='green', linestyle='--', linewidth=1.5, label='Expected (1/6 ≈ 16.67%)')
    plt.legend()
plt.title(f"Dice Roll Distribution ({'1 Die' if NUM_DICE == 1 else '2 Dice - Sum'}) — {NUM_ROLLS} Rolls", fontsize=14)
plt.xlabel("Outcome", fontsize=12)
plt.ylabel("Probability", fontsize=12)
plt.xticks(unique)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
