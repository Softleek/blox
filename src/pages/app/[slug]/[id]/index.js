import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { ConfigProvider } from "@/contexts/ConfigContext";
import Loading from "@/components/core/account/Loading";
import DoctypeForm from "@/components/pages/form";
import { useDocumentData } from "@/hooks/useDocumentData";
import { handleSave } from "@/utils/handleSave";
import { useData } from "@/contexts/DataContext";

const DocumentDetail = () => {
  const router = useRouter();
  const { slug, id } = router.query;
  const [config, setConfig] = useState(null);
  const { data, form, setData, setForm, loading, setLoading } = useData();
  const [printComponents, setPrintComponents] = useState({});
  const [customConfig, setCustomConfig] = useState({
    lifecycleHooks: {},
    customButtons: [],
    customComponents: {},
  });

  const { appData, setAppData } = useDocumentData(slug, id, setConfig);

  const saveData = async (f) => {
    await handleSave({
      data,
      form,
      appData,
      slug,
      id,
      setData,
      setForm,
      setLoading,
      config,
    });
  };

  useEffect(() => {
    if (!appData) return;

    const loadDynamicConfig = async () => {
      try {
        setPrintComponents({});
        setCustomConfig({
          lifecycleHooks: {},
          customButtons: [],
          customComponents: {},
        });

        const moduleImport = await import(
          `../../../../../apps/${appData?.app_id}/${appData?.app_id}/${appData?.module_id}/doctype/${appData?.doc?.id}/${appData?.doc?.id}.js`
        );

        setPrintComponents(moduleImport); // Store all exports dynamically

        // Extract lifecycleHooks, customButtons, and customComponents if available
        setCustomConfig({
          lifecycleHooks: moduleImport.lifecycleHooks || {},
          customButtons: moduleImport.customButtons || [],
          customComponents: moduleImport.customComponents || {},
        });
      } catch (error) {
        console.error("Failed to load print format or custom config:", error);
      }
    };

    loadDynamicConfig();
  }, [appData]);

  if (!config) {
    return <Loading />;
  }

  return (
    <ConfigProvider initialConfig={config} initialAppData={appData}>
      <DoctypeForm
        handleSave={saveData}
        config={config}
        lifecycleHooks={customConfig.lifecycleHooks}
        customButtons={customConfig.customButtons}
        customComponents={customConfig.customComponents}
        printComponents={printComponents} // Pass all imported exports
      />
    </ConfigProvider>
  );
};

export default DocumentDetail;
