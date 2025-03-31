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

import { motion } from "framer-motion";
import { useRouter } from "next/router";

const DetailForm = () => {
  const [tabs, setTabs] = useState([]);
  const [tabFields, setTabFields] = useState([]);
  const [showLogs, setShowLogs] = useState(false);
  const router = useRouter();
  const { slug, id } = router.query;
  const {
    localConfig,
    setLocalConfig,
    setSelectedItem,
    selectedTab,
    setSelectedTab,
  } = useConfig();

  useEffect(() => {
    const fetchTabs = async () => {
      const uniqueTabs = generateTabList(localConfig) || [];
      setTabs(uniqueTabs);

      if (!selectedTab && uniqueTabs.length > 0) {
        setSelectedTab(uniqueTabs[0]);
      }
    };
    fetchTabs();
  }, [localConfig]);

  useEffect(() => {
    const fetchFields = async () => {
      const sectionFields = getFieldsForTab(localConfig, selectedTab);
      setTabFields(sectionFields);
    };
    fetchFields();
  }, [selectedTab, localConfig]);

  const handleFocus = (id) => setSelectedItem(id);
  const handleBlur = () => setSelectedItem(null);
  const handleShowLogs = () => setShowLogs(true);

  // if (!slug) {
  //   return
  // }

  return (
    <motion.div
      className="w-full"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.2 }}
    >
      <motion.div
        initial={{ y: -10, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.3 }}
      >
        <div className="relative flex items-center justify-between px-4 pt-2 bg-gradient-to-tl from-purple-100 to-pink-100 text-white rounded-t-xl">
          <ul className="flex pt-2 gap-x-6 list-none bg-transparent">
            <Suspense fallback={<div>Loading Tabs...</div>}>
              {tabs.map((tab) => (
                <motion.li
                  key={tab.fieldname}
                  initial={{ opacity: 0, y: 5 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.2 }}
                >
                  <Tab
                    tab={tab}
                    handleFocus={handleFocus}
                    setShowLogs={setShowLogs}
                  />
                </motion.li>
              ))}
            </Suspense>
          </ul>
        </div>
      </motion.div>

      <motion.div
        className="px-2 py-4 h-[72vh] overflow-y-auto"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.2 }}
      >
        {showLogs ? (
          <DocumentLogs />
        ) : (
          <Suspense fallback={<div>Loading Sections...</div>}>
            {tabFields?.map((section) => (
              <motion.div
                key={section.fieldname}
                initial={{ opacity: 0, y: 5 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.2 }}
              >
                <Section
                  section={section}
                  handleFocus={handleFocus}
                  handleBlur={handleBlur}
                />
              </motion.div>
            ))}
          </Suspense>
        )}
      </motion.div>
    </motion.div>
  );
};

export default DetailForm;
