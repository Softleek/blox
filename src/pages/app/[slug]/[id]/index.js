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
  const { appData, setAppData } = useDocumentData(slug, id, setConfig);
  const [customElements, setCustomElements] = useState(null);

  const saveData = async () => {
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
        const moduleImport = await import(
          `../../../../../apps/${appData?.app_id}/${appData?.app_id}/${appData?.module_id}/doctype/${appData?.doc?.id}/${appData?.doc?.id}.js`
        );

        if (moduleImport?.default) {
          // Instantiate CustomElements with required parameters
          const customInstance = new moduleImport.default(
            form,
            setForm,
            data,
            setData,
            router,
            () => {}, // Placeholder for reloadData function
            setLoading
          );

          setCustomElements(customInstance);
        }
      } catch (error) {
        // console.error("Failed to load custom elements:", error)
      }
    };

    loadDynamicConfig();
  }, [appData]);

  return (
    <ConfigProvider initialConfig={config} initialAppData={appData}>
      <DoctypeForm
        handleSave={saveData}
        config={config}
        customElements={customElements} // Pass dynamically imported and instantiated class
      />
    </ConfigProvider>
  );
};

export default DocumentDetail;
