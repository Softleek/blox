import { useEffect, useState } from "react";
import { useNavbar } from "@/contexts/NavbarContext";
import { useSidebar } from "@/contexts/SidebarContext";
import Loading from "@/components/core/account/Loading";
import DoctypeStudio from "@/components/studio/doctype/DocStudio";
import { ConfigProvider } from "@/contexts/ConfigContext";
import ToastTemplates from "@/components/core/common/toast/ToastTemplates";
import { postData } from "@/utils/Api";
import { useData } from "@/contexts/DataContext";
import { constructPath } from "@/utils/importFile";
import { toUnderscoreLowercase } from "@/utils/textConvert";
import { useRouter } from "next/router";
// import { importFile } from "@/utils/importFile";

const DocumentDetail = () => {
  const [config, setConfig] = useState(null);
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
  const router = useRouter();

  useEffect(() => {
    const initializeDocument = async () => {
      try {
        // Update UI elements with default values
        const defaultTitle = "Doctype";
        updateDashboardText(defaultTitle);
        updatePagesText("Doctype");
        updatePageInfo({ text: defaultTitle, link: `app/doctype` });
        updateNavLinks([
          { text: "Default App", link: `/apps/default-app` },
          {
            text: "Documents",
            link: `/documents`,
          },
        ]);

        // Sidebar and UI customization
        updateTextColor("text-gray-200");
        updateIconColor("text-purple-300");
        setSidebarWidth(100);
        setSidebarHidden(false);
      } catch (error) {
        console.error(error.message);
      }
    };

    initializeDocument();
  }, []);

  const saveConfig = async (settings) => {
    try {
      const requiredFields = ["name", "module"];
      const missingFields = requiredFields.filter(
        (field) => !settings?.[field]
      );

      if (missingFields.length > 0) {
        throw `Missing required field(s): ${missingFields.join(", ")}`;
      }

      const name = toUnderscoreLowercase(settings.name);

      const filePath = constructPath(settings.module, name);

      if (!filePath) throw new Error("File path not set");
      setLoading(true);
      await fetch("/api/save-config", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          directoryPath: filePath,
          filename: `${name}.js`,
          content: `//\n`,
        }),
      });

      await fetch("/api/save-config", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          directoryPath: filePath,
          filename: `${name}.py`,
          content: `#\n`,
        }),
      });

      const response = await fetch("/api/save-config", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          directoryPath: filePath,
          filename: `${name}.json`,
          content: settings,
        }),
      });

      if (response.ok) {
        setConfig(settings);
        const response1 = await postData({}, `migrate`);
        if (!response1) {
          throw new Error("Failed to migrate");
        } else {
          ToastTemplates.success("Saved!");
          router.push(`/app/doctype/${name}`);
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
