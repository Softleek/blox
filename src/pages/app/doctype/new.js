import { useEffect, useState } from "react";
import { useNavbar } from "@/contexts/NavbarContext";
import { useSidebar } from "@/contexts/SidebarContext";
import Loading from "@/components/core/account/Loading";
import DoctypeStudio from "@/components/studio/doctype/DocStudio";
import { ConfigProvider } from "@/contexts/ConfigContext";
import ToastTemplates from "@/components/core/common/toast/ToastTemplates";
import { postData } from "@/utils/Api";
import { useData } from "@/contexts/DataContext";
import { importFile } from "@/utils/importFile";

const DocumentDetail = () => {
  const [config, setConfig] = useState(null);
  const [filePath, setFilePath] = useState(null);
  const { setLoading } = useData();

  const {
    updateDashboardText,
    updatePagesText,
    updateTextColor,
    updateIconColor,
    updatePageInfo,
    updateNavLinks,
  } = useNavbar();
  const { setSidebarHidden, setSidebarWidth } = useSidebar();

  useEffect(() => {
    const initializeDocument = async () => {
      try {
        // Set default file path or configuration
        const defaultFilePath = "/default/path/to/document";
        setFilePath(defaultFilePath);

        // Update UI elements with default values
        const defaultTitle = "New Document";
        updateDashboardText(defaultTitle);
        updatePagesText("Default Module");
        updatePageInfo({ text: defaultTitle, link: `documents/new-document` });
        updateNavLinks([
          { text: "Default App", link: `/apps/default-app` },
          {
            text: "Documents",
            link: `/documents`,
          },
        ]);

        // Load default configuration
        const configData = await importFile("default", "default-config.json");
        if (configData) {
          setConfig(configData.content);
        }

        // Sidebar and UI customization
        updateTextColor("text-gray-200");
        updateIconColor("text-purple-300");
        setSidebarWidth(100);
        setSidebarHidden(true);
      } catch (error) {
        console.error(error.message);
      }
    };

    initializeDocument();
  }, []);

  const saveConfig = async (settings) => {
    try {
      if (!filePath) throw new Error("File path not set");
      setLoading(true);
      const response = await fetch("/api/save-config", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          directoryPath: filePath,
          filename: `default-config.json`,
          content: settings,
        }),
      });

      if (response.ok) {
        setConfig(settings);
        const response1 = await postData({ doc: "default" }, `migrate`);
        if (!response1) {
          throw new Error("Failed to migrate");
        } else {
          ToastTemplates.success("Saved!");
        }
      } else throw new Error("Failed to save configuration");
    } catch (error) {
      console.error("Error saving configuration:", error);
      ToastTemplates.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ConfigProvider
      initialConfig={config}
      initialAppData={{ endpoint: `documents/new-document` }}
    >
      <DoctypeStudio handleSave={saveConfig} isNew={true} />
    </ConfigProvider>
  );
};

export default DocumentDetail;
