import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { useDocumentData } from "@/hooks/useDocumentData";
import { useData } from "@/contexts/DataContext";

const PrintPage = () => {
  const router = useRouter();
  const { slug, id } = router.query;
  const [config, setConfig] = useState(null);
  const { data, form, setData, setForm, loading, setLoading } = useData();

  const { appData, setAppData } = useDocumentData(slug, id, setConfig);

  return <div>PrintPage</div>;
};

export default PrintPage;
