import React, { useState } from "react";
import { XCircle, Eye } from "lucide-react"; // Import Lucide icons
import Modal from "../core/common/modal/Modal";
import { uploadFile } from "@/utils/Api";

const ImageField = ({ value, onChange, readOnly, preview, hidden }) => {
  const [imageFile, setImageFile] = useState(value || null);
  const [previewImage, setPreviewImage] = useState(value ? value : null);
  const [imageName, setImageName] = useState(value ? value.name : "");
  const [showPreview, setShowPreview] = useState(false);
  const [showConfirmationModal, setShowConfirmationModal] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const [isPrivate, setIsPrivate] = useState(false); // Private/public toggle

  // Split filename into name and extension
  const getFileNameAndExtension = (filename) => {
    const lastDotIndex = filename?.lastIndexOf(".");
    const name =
      lastDotIndex !== -1 ? filename?.slice(0, lastDotIndex) : filename;
    const extension = lastDotIndex !== -1 ? filename?.slice(lastDotIndex) : "";
    return { name, extension };
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const validExtensions = [
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/webp",
      ];
      if (!validExtensions.includes(file.type)) {
        alert(
          "Invalid file type. Please select an image (JPEG, PNG, GIF, WebP)."
        );
        return;
      }

      // Set the selected file and open the confirmation modal
      setSelectedFile(file);
      setImageName(file.name); // Set the initial image name
      setPreviewImage(URL.createObjectURL(file)); // Generate a preview URL
      setShowConfirmationModal(true);
    }
  };

  const handleConfirmUpload = async () => {
    if (selectedFile) {
      try {
        // Upload the file to the server and get the URL
        const resp = await uploadFile(
          selectedFile,
          "uploads",
          imageName, // Use the updated image name
          isPrivate // Pass the private/public value
        );
        if (resp?.success) {
          const fileUrl = resp?.url;
          // Update the state with the new file URL
          setImageFile(null); // Clear the file object
          setPreviewImage(fileUrl); // Set the URL as the preview image
          setImageName(imageName); // Keep the updated name

          // Pass the file URL to the parent component
          onChange(fileUrl);

          // Close the confirmation modal
          setShowConfirmationModal(false);
        }
      } catch (error) {
        console.error("Error uploading file:", error);
        ToastTemplates.error("Failed to upload image.");
      }
    }
  };

  const handleCancelUpload = () => {
    // Clear the selected file and close the confirmation modal
    setSelectedFile(null);
    setPreviewImage(null); // Clear the preview image
    setShowConfirmationModal(false);
  };

  const handleRename = (e) => {
    const newName = e.target.value;
    setImageName(newName); // Update the image name
  };

  const handleRemoveImage = () => {
    setImageFile(null);
    setPreviewImage(null);
    setImageName("");
    onChange(null);
  };

  return (
    <div className="relative image-field" hidden={hidden}>
      {previewImage ? (
        <div className="relative image-preview">
          <img
            src={previewImage}
            alt="Preview"
            className="image-preview__img w-full h-fit object-cover rounded-lg cursor-pointer"
            onClick={() => setShowPreview(true)}
          />
          <div className="flex items-center mt-2">
            {/* <input
              type="text"
              className="image-preview__rename border border-gray-300 text-right rounded-sm px-2 py-2 m-2 focus:outline-none focus:ring-1 focus:ring-yellow-500"
              value={getFileNameAndExtension(imageName).name} // Only show the name part
              onChange={handleRename}
              readOnly={readOnly}
            /> */}
            <span className="text-gray-800 py-4 px-2">
              {getFileNameAndExtension(imageName).name}
              {getFileNameAndExtension(imageName).extension}{" "}
              {/* Display the extension */}
            </span>
          </div>
          <button
            type="button"
            className="absolute top-2 right-2 bg-white rounded-full p-1 shadow-md hover:bg-gray-100"
            onClick={handleRemoveImage}
          >
            <XCircle className="w-6 h-6 text-red-500" />{" "}
            {/* Lucide icon for removal */}
          </button>
        </div>
      ) : (
        <div className="image-upload">
          <label
            htmlFor="image-upload"
            className="image-upload__label bg-purple-100 text-black px-4 py-2 my-2 rounded-lg cursor-pointer hover:bg-purple-200"
          >
            <span>Upload Image</span>
          </label>
          <input
            type="file"
            id="image-upload"
            accept="image/jpeg, image/png, image/gif, image/webp"
            readOnly={readOnly || preview}
            disabled={readOnly || preview}
            onChange={handleFileChange}
            className="hidden"
          />
        </div>
      )}

      {/* Full-Image Preview Modal */}
      {showPreview && (
        <Modal
          className="fixed inset-0 p-4 flex items-center justify-center bg-gray-600 bg-opacity-50 backdrop-blur-sm h-screen !z-500 rounded-md "
          onClick={() => setShowPreview(false)}
          isOpen={showPreview}
          onClose={() => setShowPreview(false)}
        >
          <div className="relative bg-white rounded-lg p-4 max-w-4xl max-h-screen overflow-auto">
            <img
              src={previewImage}
              alt="Full Preview"
              className="max-w-full max-h-[80vh] object-contain"
            />
            <button
              type="button"
              className="absolute top-4 right-4 bg-white rounded-full p-1 shadow-md hover:bg-pink-100"
              onClick={() => setShowPreview(false)}
            >
              <XCircle className="w-6 h-6 text-red-500" />{" "}
              {/* Lucide icon for closing modal */}
            </button>
          </div>
        </Modal>
      )}

      {/* Confirmation Modal */}
      {showConfirmationModal && (
        <Modal
          className="flex items-center justify-center w-full h-full"
          onClick={() => setShowConfirmationModal(false)}
          isOpen={showConfirmationModal}
          onClose={() => setShowConfirmationModal(false)}
        >
          <div className="flex flex-col items-center justify-center bg-white rounded-lg p-6 max-w-4xl">
            <h2 className="text-lg font-semibold mb-4">Confirm Image Upload</h2>
            <p className="mb-4">Are you sure you want to upload this image?</p>

            {/* Preview Image */}
            <div className="mb-4">
              <img
                src={previewImage}
                alt="Preview"
                className="w-full h-48 object-cover rounded-lg"
              />
            </div>

            <div className="flex items-center justify-center gap-x-6 mb-4 w-full">
              {/* Private/Public Toggle */}
              <div className="flex items-center">
                <label className="flex items-center">
                  <input
                    type="checkbox"
                    className="form-checkbox h-4 w-4 text-purple-500"
                    checked={isPrivate}
                    onChange={(e) => setIsPrivate(e.target.checked)}
                  />
                  <span className="ml-2 text-sm text-gray-700">Private</span>
                </label>
              </div>
              {/* Image Name Input */}
              <div className="">
                <input
                  type="text"
                  className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-1 focus:ring-yellow-500"
                  value={imageName}
                  onChange={handleRename}
                />
              </div>
            </div>
            {/* Action Buttons */}
            <div className="flex justify-end gap-x-4">
              <button
                type="button"
                className="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600"
                onClick={handleCancelUpload}
              >
                Cancel
              </button>
              <button
                type="button"
                className="bg-purple-500 text-white px-4 py-2 rounded-lg hover:bg-purple-600"
                onClick={handleConfirmUpload}
              >
                Confirm
              </button>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
};

export default ImageField;
