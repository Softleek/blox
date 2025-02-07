// src/pages/ReportPage.js
import { useEffect, useState } from "react";
import { fetchData } from "@/utils/Api"; // Assuming you have a fetchData function in your API utils
import { toast } from "react-toastify";
import Report from "@/apps/pos/templates/report"; // Import the report component

export default function ReportPage() {
  const [salesData, setSalesData] = useState({
    totalRevenue: 0,
    growthPercentage: 0,
    unitsSold: 0,
    volumeChange: 0,
    topProducts: [],
  });
  const [stockData, setStockData] = useState({
    currentStockLevels: [],
    productsToReorder: [],
  });

  useEffect(() => {
    const fetchReportData = async () => {
      try {
        // Fetch sales data
        const salesResponse = await fetchData({}, "core/salesinvoice");
        if (salesResponse?.data) {
          setSalesData({
            totalRevenue: salesResponse.data.totalRevenue,
            growthPercentage: salesResponse.data.growthPercentage,
            unitsSold: salesResponse.data.unitsSold,
            volumeChange: salesResponse.data.volumeChange,
            topProducts: salesResponse.data.topProducts,
          });
        }

        // Fetch stock data
        const stockResponse = await fetchData({}, "stockdata"); // Change this endpoint as necessary
        if (stockResponse?.data) {
          setStockData({
            currentStockLevels: stockResponse.data.currentStockLevels,
            productsToReorder: stockResponse.data.productsToReorder,
          });
        }
      } catch (error) {
        toast.error(`Failed to fetch data: ${error.message || error}`);
      }
    };

    fetchReportData();
  }, []);

  return (
    <div className="min-h-screen text-purple">
      <main className="flex flex-col mt-8 px-4 gap-8">
        <h1 className="text-2xl font-bold mb-4">Sales and Stock Report</h1>
        <Report salesData={salesData} stockData={stockData} />
      </main>
    </div>
  );
}
