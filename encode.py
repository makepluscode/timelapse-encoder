import cv2
import os
import argparse

def resize_image(image, target_width):
    """
    Resize an image to a specified width while maintaining its aspect ratio.

    Args:
    image (numpy.ndarray): The image to be resized.
    target_width (int): The desired width of the image.

    Returns:
    numpy.ndarray: The resized image.
    """
    # Calculate the target height to maintain the aspect ratio
    target_height = int(image.shape[0] * (target_width / image.shape[1]))
    # Resize and return the image
    return cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)

def encode_images_to_video(image_folder, video_name, fps, width=1920):
    """
    Encode images from a folder into a video.

    Args:
    image_folder (str): The folder containing JPEG images.
    video_name (str): The name of the output video file.
    fps (int): Frames per second of the output video.
    width (int): The width to which images will be resized.
    """
    # Retrieve image file names and sort them
    images = sorted(img for img in os.listdir(image_folder) if img.lower().endswith((".jpg", ".jpeg")))

    if not images:
        print(f"No JPG or JPEG files found in folder {image_folder}.")
        return

    # Read and resize the first image to determine video dimensions
    first_image_path = os.path.join(image_folder, images[0])
    first_image = cv2.imread(first_image_path)
    resized_first_image = resize_image(first_image, width)
    video_height, _, _ = resized_first_image.shape

    # Initialize the video writer
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, video_height))

    # Process each image, resize it, and write to the video
    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)
        resized_img = resize_image(img, width)
        video.write(resized_img)

    # Release resources
    cv2.destroyAllWindows()
    video.release()

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Encode JPEG images into a video.')
    parser.add_argument('image_folder', type=str, help='Folder containing JPEG images')
    parser.add_argument('video_name', type=str, help='Name of the output video file')
    parser.add_argument('fps', type=int, help='Frames per second for the video')

    args = parser.parse_args()

    # Check if the image folder exists
    if not os.path.exists(args.image_folder):
        print(f"The folder {args.image_folder} does not exist.")
        return

    # Encode images to video
    encode_images_to_video(args.image_folder, args.video_name, args.fps)

if __name__ == "__main__":
    main()
