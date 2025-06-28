from imagededup.methods import PHash
from imagededup.utils import plot_duplicates
import os
import shutil

def remove_duplicates():
    # Folder containing the frames
    image_dir = 'data/images/train'

    # Create backup folder (optional)
    backup_dir = 'data/images/train_backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Initialize
    phasher = PHash()

    print("✅ Calculating image hashes...")
    encodings = phasher.encode_images(image_dir=image_dir)

    print("✅ Finding duplicates...")
    duplicates = phasher.find_duplicates(encoding_map=encodings, min_similarity_threshold=0.90)

    print("✅ Removing duplicates...")
    for dup_list in duplicates.values():
        for dup in dup_list[1:]:  # Keep the first, remove the rest
            src = os.path.join(image_dir, dup)
            dst = os.path.join(backup_dir, dup)
            if os.path.exists(src):
                shutil.move(src, dst)

    print("✅ Done! Duplicate frames moved to 'train_backup'.")

if __name__ == '__main__':
    remove_duplicates()
