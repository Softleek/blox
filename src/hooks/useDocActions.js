import ToastTemplates from "@/components/core/common/toast/ToastTemplates";
import { postData, updateData } from "@/utils/Api";
import { useState } from "react";

export const useDocActions = ({
  localConfig,
  localData,
  setForm,
  setData,
  setLoading,
  localAppData,
  slug,
  id,
}) => {
  const [isProcessing, setIsProcessing] = useState(false);

  const handleSubmit = async () => {
    if (!localConfig.is_submittable) return;

    setIsProcessing(true);
    setLoading(true);

    try {
      // Simulate API call
      const response = await postData(
        {},
        `${localAppData?.app}/${slug}/${id}/submit`
      );
      if (response.data) {
        setData((prev) => ({ ...prev, ...response.data }));
        setForm((prev) => ({ ...prev, ...response.data }));
      }

      // Update docstatus to 1 after submission
      setForm((prev) => ({ ...prev, docstatus: 1 }));
      ToastTemplates.success("Document submitted successfully!");
    } catch (error) {
      ToastTemplates.error("Error submitting document");
    } finally {
      setIsProcessing(false);
      setLoading(false);
    }
  };

  const handleCancel = async () => {
    setIsProcessing(true);
    setLoading(true);

    try {
      // Simulate API call

      const response = await postData(
        {},
        `${localAppData?.app}/${slug}/${id}/cancel`
      );
      if (response.data) {
        setData((prev) => ({ ...prev, ...response.data }));
        setForm((prev) => ({ ...prev, ...response.data }));
      }
      ToastTemplates.success("Document cancelled successfully!");
    } catch (error) {
      ToastTemplates.error("Error cancelling document");
    } finally {
      setIsProcessing(false);
      setLoading(false);
    }
  };

  return {
    isProcessing,
    handleSubmit,
    handleCancel,
  };
};
