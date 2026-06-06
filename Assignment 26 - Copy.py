''' Assignment (06/04/2026) '''
import cv2

image_path = r"C:\Users\Nithya Shree G.M\Desktop\desk\Internship\image.jpg"

image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Image not found. Check the path!")
else:
    print("✅ Image Loaded Successfully!\n")

    print("📏 Image Shape:", image.shape)

    print("\n🎯 Pixel Value at (0,0):", image[0, 0])

    print("\n🔢 First 5x5 Pixel Values:\n", image[0:5, 0:5])

    print("\n🔵 Blue Channel (5x5):\n", image[0:5, 0:5, 0])
    print("\n🟢 Green Channel (5x5):\n", image[0:5, 0:5, 1])
    print("\n🔴 Red Channel (5x5):\n", image[0:5, 0:5, 2])