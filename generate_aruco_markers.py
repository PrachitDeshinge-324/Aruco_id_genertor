import cv2
import os
import argparse

def generate_aruco_markers(
    output_folder="aruco_markers",
    size=200,
    border=1,
    dictionary_id=cv2.aruco.DICT_5X5_1000,
    start_id=0,
    end_id=None  # None means all markers in the dictionary
):
    """
    Generate ArUco markers with customizable parameters.
    
    Args:
        output_folder (str): Folder to save markers
        size (int): Marker image size (pixels)
        border (int): Border thickness (bits)
        dictionary_id (int): ArUco dictionary type
        start_id (int): First marker ID to generate
        end_id (int): Last marker ID to generate (None = all IDs)
    """
    # Create output directory
    os.makedirs(output_folder, exist_ok=True)

    # Get ArUco dictionary
    aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary_id)
    
    # Determine ID range
    if end_id is None:
        end_id = aruco_dict.nMarkers  # All possible IDs
    total_ids = end_id - start_id

    # Generate markers
    for marker_id in range(start_id, end_id):
        # Create marker image
        marker_image = cv2.aruco.generateImageMarker(
            aruco_dict,
            marker_id,
            size,
            borderBits=border
        )
        
        # Save marker with padded filename
        filename = os.path.join(
            output_folder,
            f"marker_{dictionary_id}_{marker_id:04d}.png"
        )
        cv2.imwrite(filename, marker_image)
        print(f"Saved: {filename} ({marker_id - start_id + 1}/{total_ids})")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate ArUco markers.")
    parser.add_argument(
        '--output_folder', type=str, default="aruco_markers", 
        help="Folder to save the generated ArUco markers"
    )
    parser.add_argument(
        '--size', type=int, default=200, 
        help="Size of the ArUco markers in pixels"
    )
    parser.add_argument(
        '--border', type=int, default=1, 
        help="Border thickness of the ArUco markers (in bits)"
    )
    parser.add_argument(
        '--dictionary_id', type=int, default=cv2.aruco.DICT_5X5_1000, 
        help="ArUco dictionary type ID"
    )
    parser.add_argument(
        '--start_id', type=int, default=0, 
        help="Starting marker ID"
    )
    parser.add_argument(
        '--end_id', type=int, default=None, 
        help="Ending marker ID (None means generate all markers)"
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    # Call the function with arguments from the command line
    generate_aruco_markers(
        output_folder=args.output_folder,
        size=args.size,
        border=args.border,
        dictionary_id=args.dictionary_id,
        start_id=args.start_id,
        end_id=args.end_id
    )
