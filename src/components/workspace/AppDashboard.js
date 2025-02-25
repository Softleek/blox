import React, { useEffect, useState } from "react";
// import { ReportGraph, ReportCards } from "./Graph";
import { FaChevronLeft, FaChevronRight } from "react-icons/fa";
import { fetchData } from "@/utils/Api";
import ReportCards from "./ReportCards";
import ReportGraph from "./Graph";

const FILTER_OPTIONS = [
  { label: "Day", value: "day" },
  { label: "Week", value: "week" },
  { label: "Month", value: "month" },
  { label: "Year", value: "year" },
];

const initialReportData = {
  summary: {
    total_customers: 0,
    total_crossborders: 1,
    total_items: 1,
    total_invoices: 0,
    total_payments: "0.00",
    avg_invoice_amount: "0.00",
  },
  analytics: [
    {
      period: "2025-02-01T00:00:00Z",
      total_invoices: 0,
      total_invoice_amount: 0,
      total_items: 1,
    },
  ],
  top_items: [
    {
      name: "Test",
      count: 1,
    },
  ],
};

const AppDashboard = () => {
  const [reportData, setReportData] = useState(initialReportData);
  const [filter, setFilter] = useState("month");
  const [selectedDate, setSelectedDate] = useState("");

  useEffect(() => {
    const fetchReportData = async () => {
      try {
        const response = await fetchData(
          {},
          `reports/detailed?filter=${filter}${
            selectedDate ? `&date=${selectedDate}` : ""
          }`
        );

        console.log("Report data:", response.data);

        setReportData({
          summary: {
            total_customers: response.data.total_customers,
            total_crossborders: response.data.total_crossborders,
            total_items: response.data.total_items,
            total_invoices: response.data.total_invoices,
            total_payments: response.data.total_payments,
            avg_invoice_amount: response.data.avg_invoice_amount,
          },
          analytics: response.data.analytics || [],
          top_items: response.data.top_items || [],
        });
      } catch (error) {
        console.error("Error fetching report data:", error);
      }
    };

    fetchReportData();
  }, [filter, selectedDate]);

  const adjustDate = (direction) => {
    const currentDate = selectedDate ? new Date(selectedDate) : new Date();

    switch (filter) {
      case "day":
        currentDate.setDate(
          currentDate.getDate() + (direction === "next" ? 1 : -1)
        );
        setSelectedDate(currentDate.toISOString().split("T")[0]);
        break;
      case "week":
        currentDate.setDate(
          currentDate.getDate() + (direction === "next" ? 7 : -7)
        );
        setSelectedDate(currentDate.toISOString().split("T")[0]);
        break;
      case "month":
        currentDate.setMonth(
          currentDate.getMonth() + (direction === "next" ? 1 : -1)
        );
        setSelectedDate(currentDate.toISOString().slice(0, 7));
        break;
      case "year":
        currentDate.setFullYear(
          currentDate.getFullYear() + (direction === "next" ? 1 : -1)
        );
        setSelectedDate(currentDate.getFullYear().toString());
        break;
      default:
        break;
    }
  };

  return (
    <div className="flex flex-col space-y-6 px-4 py-4 rounded-xl shadow-lg">
      <h2 className="text-3xl font-bold text-purple-800">Dashboard</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-x-3 items-center">
        <div className="grid grid-cols-4 gap-x-3">
          {FILTER_OPTIONS.map((option) => (
            <button
              key={option.value}
              className={`px-5 py-1 w-28 h-12 text-md font-medium rounded-full transition-all duration-300 focus:outline-none shadow-md ${
                filter === option.value
                  ? "bg-purple-600 text-white"
                  : "bg-white text-purple-800 hover:bg-purple-200"
              }`}
              onClick={() => {
                setFilter(option.value);
                setSelectedDate("");
              }}
            >
              {option.label}
            </button>
          ))}
        </div>

        <div className="flex items-center space-x-3 bg-white px-4 py-2 rounded-full shadow-md">
          <button
            className="p-2 bg-purple-300 rounded-full hover:bg-purple-400"
            onClick={() => adjustDate("prev")}
          >
            <FaChevronLeft className="h-5 w-5 text-purple-800" />
          </button>
          <input
            type={
              filter === "day"
                ? "date"
                : filter === "month"
                ? "month"
                : "number"
            }
            min={filter === "year" ? "2000" : undefined}
            max={filter === "year" ? new Date().getFullYear() : undefined}
            className="px-4 py-2 w-full border border-purple-300 rounded-lg focus:ring focus:ring-purple-400 text-purple-800 bg-white"
            value={selectedDate}
            onChange={(e) => setSelectedDate(e.target.value)}
          />
          <button
            className="p-2 bg-purple-300 rounded-full hover:bg-purple-400"
            onClick={() => adjustDate("next")}
          >
            <FaChevronRight className="h-5 w-5 text-purple-800" />
          </button>
        </div>
      </div>

      {reportData ? (
        <>
          <ReportCards data={reportData?.summary} />
          <ReportGraph data={reportData} />
        </>
      ) : (
        <p className="text-purple-600 text-md">Loading reports...</p>
      )}
    </div>
  );
};

export default AppDashboard;
