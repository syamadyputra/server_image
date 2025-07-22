from PIL import Image
import os
import subprocess

def convert_png_to_webp(input_png, output_webp, quality=80):
    """
    Converts a single PNG image to WebP format using cwebp.

    Args:
        input_png: Path to the input PNG file.
        output_webp: Path to the output WebP file.
        quality:  Quality setting for WebP (0-100).  Lower values mean more compression but potentially lower quality, {Link: according to Infotechys.com https://infotechys.com/convert-png-images-to-webp/} [7, 13].
    """
    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_webp), exist_ok=True)

        # Construct the cwebp command
        command = [
            "cwebp",
            input_png,
            "-o",
            output_webp,
            "-q",
            str(quality),
        ]

        # Execute the command
        subprocess.run(command, check=True, capture_output=True)

        print(f"Successfully converted {input_png} to {output_webp}")

    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_png}: {e.stderr.decode()}")
    except FileNotFoundError:
        print("cwebp not found. Make sure it's in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def batch_convert_pngs(input_folder, output_folder, quality=80):
    """
    Converts all PNG files in a folder to WebP format.

    Args:
        input_folder: Path to the folder containing PNG files.
        output_folder: Path to the folder where WebP files will be saved.
        quality: Quality setting for WebP (0-100).
    """
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            input_png = os.path.join(input_folder, filename)
            # Create the output filename (replace extension with .webp)
            output_filename = os.path.splitext(filename)[0] + ".webp"
            output_webp = os.path.join(output_folder, output_filename)
            convert_png_to_webp(input_png, output_webp, quality)

if __name__ == "__main__":
    input_folder = "./clothing/before/glove"  # Replace with your input folder
    output_folder = "./clothing/glove" # Replace with your output folder
    conversion_quality = 80  # Adjust as needed

    batch_convert_pngs(input_folder, output_folder, conversion_quality)