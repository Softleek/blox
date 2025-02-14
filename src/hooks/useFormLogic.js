import { useEffect, useState } from "react";
import ToastTemplates from "@/components/core/common/toast/ToastTemplates";
import _ from "lodash";

export function useFormLogic(form, setForm, data, localConfig, handleSave) {
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    if (!_.isEqual(form, data)) {
      setIsEditing(true);
    } else {
      setIsEditing(false);
    }
  }, [form, data]);

  const validateFields = () => {
    const missingFields = [];
    localConfig?.field_order.forEach((fieldName) => {
      const field = localConfig?.fields?.[fieldName];

      if (field?.reqd && (!form[fieldName] || form[fieldName].trim() === "")) {
        missingFields.push(field.label || fieldName);
      }
    });

    if (missingFields.length > 0) {
      ToastTemplates.warning(
        `Please fill in the required fields: ${missingFields.join(", ")}`
      );
      return false;
    }
    return true;
  };

  const handleSaveClick = (event) => {
    event.preventDefault();
    if (!validateFields()) return;

    const cleanedForm = cleanData(form);
    handleSave(cleanedForm);
  };

  return { isEditing, setIsEditing, handleSaveClick };
}
