import { useState, useEffect } from "react";
import { postData, updateData } from "@/utils/Api";
import { getFromDB } from "@/utils/indexedDB";
import { toast } from "react-toastify";
import useLoadingOffloadingKeyEvents from "@/hooks/useLoadingOffloadingKeyEvents";
import { useConfig } from "@/contexts/ConfigContext";
import { useData } from "@/contexts/DataContext";
import { useRouter } from "next/router";

export const useStatusHandler = (dashboardText) => {
  const router = useRouter();
  const { slug, id } = router?.query;
  const { localConfig: config, localAppData } = useConfig();
  const { data } = useData();
  const [isLoading, setIsLoading] = useState(false);
  const [errorModal, setErrorModal] = useState({
    isOpen: false,
    message: null,
    title: "",
    onProceed: () => {},
  });
  const [perms, setPerms] = useState(null);
  const [canEdit, setCanEdit] = useState(null);
  const [canDelete, setCanDelete] = useState(null);

  const currentStatusConfig = config?.workflow?.find(
    (statusConfig) =>
      statusConfig.name.toString() ===
      (typeof data?.status === "string"
        ? data.status.trim()
        : data?.status?.toString())
  );

  const currentStatus = currentStatusConfig?.name?.trim();
  const nextStatus = currentStatusConfig?.nextStatus?.trim();
  const action = currentStatusConfig?.actions[0];

  const handleErrorResponse = (res) => {
    if (res?.error) {
      const list = res?.message?.data;
      if (list) setIsLoading(false);
      toast.error(res?.message?.error);
      return false;
    }
    return true;
  };

  const updateStatus = async () => {
    try {
      let postDataPayload, endpoint;
      setIsLoading(true);

      if (nextStatus === "In Transit") {
        await postData(
          { crossborder_id: id, action: "Transit" },
          "crossborder/update-status"
        );
      } else if (nextStatus === "Offloaded") {
        postDataPayload = { crossborder_id: id, action: "Offload" };
        endpoint = "crossborder/update-status";
      } else if (nextStatus === "Dispatched") {
        postDataPayload = { item_id: id };
        endpoint = "item/dispatch";
      }

      if (endpoint) {
        const res = await postData(postDataPayload, endpoint);
        if (!handleErrorResponse(res)) return;
      }

      const response = await updateData(
        { status: nextStatus },
        `${localAppData?.app_id}/${slug}/${id}`
      );
      if (response?.data) router.reload();
    } catch (error) {
      console.error("Error updating status:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleScannedCode = async (code) => {
    const extractedCode = code.split("/").pop();
    let response;
    try {
      switch (currentStatus) {
        case "Loading":
          response = await postData(
            { item_id: extractedCode, crossborder_id: id, action: "Load" },
            "crossborder/add-item"
          );
          break;
        case "Offloading":
          response = await postData(
            { item_id: extractedCode, crossborder_id: id, action: "Offload" },
            "crossborder/add-item"
          );
          break;
        case "Adding Items":
          response = await postData(
            { item_id: extractedCode, dispatch_id: id },
            "dispatch/add-item"
          );
          break;
      }
      if (response?.data)
        toast.success(`${extractedCode} - ${response.data.message}`);
      else toast.error(`${extractedCode} - ${response?.message?.error}`);
    } catch (error) {
      toast.error(`Error: ${error.message}`);
    }
  };

  useLoadingOffloadingKeyEvents(currentStatus, handleScannedCode);

  useEffect(() => {
    (async () => {
      const perm = await getFromDB("permissions");
      setPerms(perm);
    })();
  }, [router]);

  useEffect(() => {
    if (perms != null) {
      setCanEdit(
        perms === "all" ||
          perms.includes(`change_${dashboardText?.toLowerCase()}`)
      );
      setCanDelete(
        perms === "all" ||
          perms.includes(`delete_${dashboardText?.toLowerCase()}`)
      );
    }
  }, [dashboardText, perms]);

  return {
    isLoading,
    errorModal,
    updateStatus,
    handleScannedCode,
    currentStatus,
    canEdit,
    canDelete,
    action,
  };
};
