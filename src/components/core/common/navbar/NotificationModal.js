import React from "react";
import Modal from "../modal/Modal";

const NotificationModal = ({ isOpen, onClose, reminders }) => {
  if (!isOpen) return null;

  return (
    <Modal isOpen={isOpen} onClose={onClose} position="top" className="!pt-20">
      <div className="py-2 px-5 w-[800px] overflow-y-auto">
        <div className="flex justify-between items-center mb-3">
          <h2 className="text-xl font-semibold text-purple-900">
            Upcoming Reminders
          </h2>
          {/* <button
            onClick={onClose}
            className="text-gray-600 hover:text-gray-900 font-bold focus:outline-none transition duration-300 ease-in-out"
          >
            &times;
          </button> */}
        </div>

        {reminders.length === 0 ? (
          <p className="text-gray-500 text-center">
            No upcoming reminders in the next 2 weeks.
          </p>
        ) : (
          <ul className="space-y-3">
            {reminders.map((reminder, index) => (
              <li
                key={index}
                className="bg-gradient-to-r from-blue-50 via-indigo-50 to-purple-50 py-2 px-4 rounded-xl shadow-md hover:shadow-lg transition-shadow duration-300 transform hover:scale-105"
              >
                <div className="flex justify-between items-start">
                  <div className="flex-1 pr-4">
                    <h3 className="text-lg font-bold text-pink-800 hover:text-indigo-900">
                      {reminder.name}
                    </h3>
                    <p className="text-green-800 mt-2 text-xs">
                      {reminder.message}
                    </p>
                  </div>
                  <div className="text-right">
                    <span className="block text-sm font-medium text-gray-800">
                      {new Date(reminder.next_run).toLocaleDateString()}
                    </span>
                    <span className="text-xs text-gray-700">
                      {new Date(reminder.next_run).toLocaleTimeString()}
                    </span>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </Modal>
  );
};

export default NotificationModal;
