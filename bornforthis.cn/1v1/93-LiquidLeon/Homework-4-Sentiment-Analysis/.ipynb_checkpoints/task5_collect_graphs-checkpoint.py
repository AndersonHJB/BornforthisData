
# -*- coding: utf-8 -*-
# Task 5: Collect and show 9 graphs
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os

# Update these paths after running tasks 2–4.
nb_imgs = [
    "Naive_Bayes_multinomial_run1.png",
    "Naive_Bayes_multinomial_run2.png",
    "Naive_Bayes_multinomial_run3.png",
]
lr_imgs = [
    # Will depend on which LR setting won; adjust basename accordingly if needed
    "LogReg_custom-multinomial_run1.png".replace(" ", "_"),
    "LogReg_custom-multinomial_run2.png".replace(" ", "_"),
    "LogReg_custom-multinomial_run3.png".replace(" ", "_"),
]
nn_imgs = [
    "NeuralNet_cv_multi_run1.png",
    "NeuralNet_cv_multi_run2.png",
    "NeuralNet_cv_multi_run3.png",
]

all_imgs = nb_imgs + lr_imgs + nn_imgs

fig, axs = plt.subplots(3, 3, figsize=(12, 10))
for i, ax in enumerate(axs.flat):
    p = all_imgs[i]
    if os.path.exists(p):
        img = mpimg.imread(p)
        ax.imshow(img)
        ax.set_title(os.path.basename(p), fontsize=9)
        ax.axis('off')
    else:
        ax.text(0.5, 0.5, f"Missing Image\n{p}", ha='center', va='center', fontsize=11, color='red')
        ax.set_facecolor('lightgray')
        ax.set_title(os.path.basename(p), fontsize=9)
        ax.axis('off')
plt.tight_layout()
plt.savefig("All_9_Graphs_ContactSheet.png", bbox_inches='tight', dpi=140)
plt.close()
print("Saved contact sheet to All_9_Graphs_ContactSheet.png")
