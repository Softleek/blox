import React from "react";

const ProfileMessages = () => {
  return (
    <div className="w-full max-w-full px-4 lg-max:mt-6">
      <div className="relative flex flex-col h-full min-w-0 break-words bg-white border-0 shadow-lg rounded-2xl bg-clip-border">
        <div className="p-4 pb-0 mb-0 bg-pink-50 border-b-0 rounded-t-2xl">
          <h6 className="mb-0 text-lg font-semibold text-blue-800">ProfileMessages</h6>
        </div>
        <div className="flex-auto p-4">
          <ul className="flex flex-col pl-0 mb-0 rounded-lg space-y-2">
            <li className="relative flex items-center px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg shadow-sm">
              <div className="flex-shrink-0 w-12 h-12 mr-4 bg-blue-100 rounded-full flex items-center justify-center">
                <img
                  src="https://via.placeholder.com/48"
                  alt="shipment update"
                  className="w-8 h-8 rounded-full"
                />
              </div>
              <div className="flex flex-col flex-grow">
                <h6 className="mb-1 text-sm font-medium text-blue-700">
                  Shipment Update
                </h6>
                <p className="text-xs text-gray-600">
                  Your shipment with tracking number XYZ123 has been dispatched.
                </p>
              </div>
              <a
                className="ml-auto py-1 px-3 text-xs font-semibold text-blue-600 hover:bg-blue-50 rounded-lg border border-blue-200 transition-all duration-200"
                href="/"
              >
                View
              </a>
            </li>
            <li className="relative flex items-center px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg shadow-sm">
              <div className="flex-shrink-0 w-12 h-12 mr-4 bg-blue-100 rounded-full flex items-center justify-center">
                <img
                  src="https://via.placeholder.com/48"
                  alt="delivery status"
                  className="w-8 h-8 rounded-full"
                />
              </div>
              <div className="flex flex-col flex-grow">
                <h6 className="mb-1 text-sm font-medium text-blue-700">
                  Delivery Status
                </h6>
                <p className="text-xs text-gray-600">
                  Your package is out for delivery and is expected to arrive by
                  EOD.
                </p>
              </div>
              <a
                className="ml-auto py-1 px-3 text-xs font-semibold text-blue-600 hover:bg-blue-50 rounded-lg border border-blue-200 transition-all duration-200"
                href="/"
              >
                View
              </a>
            </li>
            <li className="relative flex items-center px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg shadow-sm">
              <div className="flex-shrink-0 w-12 h-12 mr-4 bg-red-100 rounded-full flex items-center justify-center">
                <img
                  src="https://via.placeholder.com/48"
                  alt="system alert"
                  className="w-8 h-8 rounded-full"
                />
              </div>
              <div className="flex flex-col flex-grow">
                <h6 className="mb-1 text-sm font-medium text-red-700">
                  System Alert
                </h6>
                <p className="text-xs text-gray-600">
                  There was an issue with your last order. Please check the
                  details.
                </p>
              </div>
              <a
                className="ml-auto py-1 px-3 text-xs font-semibold text-red-600 hover:bg-red-50 rounded-lg border border-red-200 transition-all duration-200"
                href="/"
              >
                View
              </a>
            </li>
            <li className="relative flex items-center px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg shadow-sm">
              <div className="flex-shrink-0 w-12 h-12 mr-4 bg-green-100 rounded-full flex items-center justify-center">
                <img
                  src="https://via.placeholder.com/48"
                  alt="package delivered"
                  className="w-8 h-8 rounded-full"
                />
              </div>
              <div className="flex flex-col flex-grow">
                <h6 className="mb-1 text-sm font-medium text-green-700">
                  Package Delivered
                </h6>
                <p className="text-xs text-gray-600">
                  Your package has been successfully delivered.
                </p>
              </div>
              <a
                className="ml-auto py-1 px-3 text-xs font-semibold text-green-600 hover:bg-green-50 rounded-lg border border-green-200 transition-all duration-200"
                href="/"
              >
                View
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default ProfileMessages;
