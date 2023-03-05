from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.metrics import structural_similarity as ssim

from serpapi import GoogleSearch



def interface(url):
    params = {
        "engine": "google_lens",
        "url": url,
        "hl": "en",
        "api_key": "4ce1e368f5f44ba69e675f986f22b3df728f823045d26dd12548144f0aa6c71e"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    print(results)

    if "visual_matches" not in results.keys():
        return 0
    visual_matches = results["visual_matches"]

    # print(visual_matches)

    sims = []
    img = resize(rgb2gray(io.imread(url)), (256, 256))
    for match in visual_matches[:5]:
        match_img = resize(rgb2gray(io.imread(match["thumbnail"])), (256, 256))
        sims.append(ssim(img, match_img, data_range=max(
            img.max(), match_img.max()) - min(img.min(), match_img.min())))

    print(sims)

    return sum(sims)
