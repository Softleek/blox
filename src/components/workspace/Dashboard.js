import React, { useState, useEffect } from "react";
import {
  faBox,
  faShoppingCart,
  faCreditCard,
  faChartLine,
} from "@fortawesome/free-solid-svg-icons";
import LinkSection from "@/components/workspace/LinkSection";
import LinkCard from "@/components/workspace/LinkCard";
import config from "@/data/config.json";

const Dashboard = () => {
  const [appModules, setAppModules] = useState([]);

  useEffect(() => {
    setAppModules(config);
  }, []);

  return (
    <div className="flex flex-col">
      {/* Header Section */}
      <div className="w-full mx-4 px-6 py-4 bg-gradient-to-r from-orange-500 to-yellow-500">
        <h1 className="text-3xl font-bold text-white">DEO AFRICAN MAGIC</h1>
        <p className="text-lg text-white opacity-90">
          Welcome to the eCommerce Dashboard.
        </p>
      </div>

      {/* Quick Stats Section */}
      <div className="w-full px-6 py-4">
        <h6 className="text-xl font-bold text-gray-800">Quick Stats</h6>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
          <div className="p-4 bg-white rounded-lg shadow-md">
            <p className="text-sm text-gray-600">Total Products</p>
            <p className="text-2xl font-bold text-orange-600">320</p>
          </div>
          <div className="p-4 bg-white rounded-lg shadow-md">
            <p className="text-sm text-gray-600">Pending Orders</p>
            <p className="text-2xl font-bold text-green-600">45</p>
          </div>
          <div className="p-4 bg-white rounded-lg shadow-md">
            <p className="text-sm text-gray-600">Total Sales</p>
            <p className="text-2xl font-bold text-purple-600">KSH 1,245,000</p>
          </div>
        </div>
      </div>

      {/* Quick Links Section */}
      <div className="w-full px-3 mt-4">
        <h6 className="pl-3 ml-2 text-sm font-bold leading-tight text-orange-900 uppercase opacity-90">
          Quick Links
        </h6>
        <div className="grid grid-cols-2 md:grid-cols-3 px-4 py-2 gap-4">
          <LinkCard
            title="Products"
            icon={faBox}
            href="/app/product"
            iconBg="bg-gradient-to-tl from-orange-400 to-red-500"
            bgColor="bg-white"
            tooltipContent="Manage Products"
          />
          <LinkCard
            title="Orders"
            icon={faShoppingCart}
            href="/app/order"
            iconBg="bg-gradient-to-tl from-green-400 to-blue-500"
            bgColor="bg-white"
            tooltipContent="View Orders"
          />
          <LinkCard
            title="Payments"
            icon={faCreditCard}
            href="/app/payment"
            iconBg="bg-gradient-to-tl from-purple-400 to-pink-500"
            bgColor="bg-white"
            tooltipContent="Manage Payments"
          />
        </div>
      </div>

      {/* Recent Activity Section */}
      <div className="w-full px-6 py-4">
        <h6 className="text-xl font-bold text-gray-800">Recent Activity</h6>
        <div className="mt-4 bg-white rounded-lg shadow-md p-4">
          <ul className="space-y-3">
            <li className="flex items-center space-x-3">
              <span className="text-green-500">✔</span>
              <p className="text-sm text-gray-700">
                New product "Handmade Beaded Necklace" added.
              </p>
            </li>
            <li className="flex items-center space-x-3">
              <span className="text-blue-500">📦</span>
              <p className="text-sm text-gray-700">
                Order #4567 has been shipped.
              </p>
            </li>
            <li className="flex items-center space-x-3">
              <span className="text-yellow-500">⚠</span>
              <p className="text-sm text-gray-700">
                Payment for Order #1234 is pending verification.
              </p>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
