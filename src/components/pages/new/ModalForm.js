import React from "react";

const ModalForm = ({ handleCloseModal, doc }) => {
  return (
    <form>
      {/* Example form content */}
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2">
          Name
        </label>
        <input
          type="text"
          className="shadow-sm appearance-none border rounded-sm w-full py-2 px-3 text-gray-700 leading-tight focus:outline-hidden focus:shadow-outline"
          placeholder="Enter name"
        />
      </div>
      <div className="flex justify-end">
        <button
          type="button"
          className="py-2 px-4 rounded-sm bg-purple-500 hover:bg-purple-700 text-white mr-2"
          onClick={handleCloseModal}
        >
          Cancel
        </button>
        <button
          type="submit"
          className="py-2 px-4 rounded-sm bg-green-500 hover:bg-green-700 text-white"
        >
          Save
        </button>
      </div>
    </form>
  );
};

export default ModalForm;
