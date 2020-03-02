import pickle
import matplotlib.pyplot as plt

import numpy as np


def _plot_score(title, gov_art, vec, pred_text, xticks, chunk_unit):
    heat_max = np.max(vec)
    heat_min = np.min(vec)

    _axis_fontsize = 7

    chunks = len(xticks) // chunk_unit + 1

    num_rows = 10
    pages = chunks // num_rows + 1
    page_chunk = num_rows * chunk_unit

    for page in range(pages):
        fig, axes = plt.subplots(nrows=num_rows, ncols=1, figsize=(14, 10))

        # fig.suptitle('pred_text', fontsize=16)
        start = 0

        for row_idx in range(num_rows):
            ax = axes[row_idx]
            ax.set_yticks([])
            ax.set_xticks(range(0, chunk_unit))

            starts = page_chunk * page + start
            ends = page_chunk * page + (row_idx + 1) * 17

            ax.set_xticklabels(
                xticks[starts:ends], fontsize=_axis_fontsize,
            )
            ax.imshow([vec[starts:ends]])
            start += chunk_unit

        fig.tight_layout(pad=1.0)

        plt.savefig(title + "_" + gov_art + "_" + str(page) + ".png")

        # close
        plt.clf()
        plt.cla()
        plt.close()

    # plt.show()


if __name__ == "__main__":
    pkl_path = "/Users/zachary/deepwto/deepwto-draft/models/cite_wa/OneLabelTextCNN/139_[Article III:4]_grad_cams.pkl"

    with open(pkl_path, "rb") as handle:
        grad_cam = pickle.load(handle)

    _plot_score(
        title=grad_cam["x_val_testid"][0],
        gov_art="gov_measure",
        vec=grad_cam["grad_cam_c_gov"],
        pred_text="POSITIVE",
        xticks=grad_cam["raw_gov_tokens"],
        chunk_unit=17,
    )

    _plot_score(
        title=grad_cam["x_val_testid"][0],
        vec=grad_cam["grad_cam_c_art"],
        gov_art="article",
        pred_text="POSITIVE",
        xticks=grad_cam["raw_art_tokens"],
        chunk_unit=17,
    )
