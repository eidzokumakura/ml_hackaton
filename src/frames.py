import cv2
import argparse
parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('video_path', type=str, help="Path to your video")
parser.add_argument('output_path', type=str, help="Output dir for your images")
parser.add_argument('name_prefix', type=str, help='Example: "frame_" gives "frame_000000.jpg"')
args = parser.parse_args()

video_path = args.video_path
cap = cv2.VideoCapture(video_path)

success, frame = cap.read()
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for index in range(length):
    ret, frame = cap.read()
    need_index = "0" * (6 - len(str(index))) + str(index)
    name = args.output_path + args.name_prefix + need_index + ".jpg"
    print(name)
    cv2.imwrite(name, frame)
    index += 1

cap.release()

# cd src
# example: python frames.py video1_content/cam1_30fps.avi video1_content\\dataset\\images\\ frame_