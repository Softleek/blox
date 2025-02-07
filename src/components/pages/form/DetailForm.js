import React, { useEffect, useState, lazy, Suspense } from "react";
import dynamic from "next/dynamic";

// Lazy-load components and utility functions
const Section = dynamic(() => import("./section"), { ssr: false });
const PrimaryButton1 = lazy(() =>
  import("@/components/core/common/buttons/Primary1")
);

import { useConfig } from "@/contexts/ConfigContext";
import { generateTabList } from "@/components/studio/doctype/utils/generateTabList ";
import { getFieldsForTab } from "@/components/studio/doctype/utils/getFieldsForTab";
import Tab from "./Tab";
import DocumentLogs from "./Logs";

const DetailForm = () => {
  const [tabs, setTabs] = useState([]);
  const [tabFields, setTabFields] = useState([]);
  const [showLogs, setShowLogs] = useState(false);
  const {
    localConfig,
    setLocalConfig,
    setSelectedItem,
    selectedTab,
    setSelectedTab,
  } = useConfig();

  useEffect(() => {
    // Recompute tabs whenever `localConfig` changes
    const fetchTabs = async () => {
      const uniqueTabs = generateTabList(localConfig) || [];

      setTabs(uniqueTabs);

      // Default to the first tab if none is selected
      if (!selectedTab && uniqueTabs.length > 0) {
        setSelectedTab(uniqueTabs[0]);
      }
    };
    fetchTabs();
  }, [localConfig]);

  useEffect(() => {
    // Update tabFields when the selected tab changes
    const fetchFields = async () => {
      const sectionFields = getFieldsForTab(localConfig, selectedTab);

      setTabFields(sectionFields);
    };
    fetchFields();
  }, [selectedTab, localConfig]);

  const handleFocus = (id) => {
    setSelectedItem(id);
  };

  const handleBlur = () => {
    setSelectedItem(null);
  };

  const handleShowLogs = () => {
    setShowLogs(true);
  };

  return (
    <div className="w-full">
      <div>
        <div className="relative flex items-center justify-between px-4 pt-2 bg-gradient-to-tl from-purple-100 to-pink-100 text-white rounded-t-xl">
          <ul className="flex pt-2 gap-x-6 list-none bg-transparent">
            <Suspense fallback={<div>Loading Tabs...</div>}>
              {tabs.map((tab) => (
                <Tab
                  key={tab.fieldname}
                  tab={tab}
                  handleFocus={handleFocus}
                  setShowLogs={setShowLogs}
                />
              ))}
            </Suspense>
          </ul>
          <div
            className={`flex flex-row items-center font-medium text-base  cursor-pointer ${
              showLogs
                ? "border-b-[1px] border-slate-800  text-purple-700 "
                : "text-slate-900"
            }`}
            onClick={handleShowLogs}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5 mr-2"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fillRule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v4a1 1 0 002 0V7zm-1 8a1 1 0 100-2 1 1 0 000 2z"
                clipRule="evenodd"
              />
            </svg>
            Activity Logs
          </div>
        </div>
        <div className="px-2 py-4 h-[78vh] overflow-y-auto">
          {showLogs ? (
            <>
              <DocumentLogs />
            </>
          ) : (
            <Suspense fallback={<div>Loading Sections...</div>}>
              {tabFields?.map((section, index) => (
                <Section
                  key={index}
                  section={section}
                  handleFocus={handleFocus}
                  handleBlur={handleBlur}
                />
              ))}
            </Suspense>
          )}
        </div>
      </div>
    </div>
  );
};

export default DetailForm;
