import React, { useRef, useEffect, useState } from "react";
import { useConfig } from "@/contexts/ConfigContext";
import FieldRenderer from "./FieldRenderer";
import { useData } from "@/contexts/DataContext";
import { evaluateDependsOn } from "@/utils/evaluationUtils";
import { useRouter } from "next/router";

const FieldItem = ({ item, handleFocus, placeholder = false }) => {
  const { selectedItem, localConfig, localAppData } = useConfig();
  const { form, setForm, data } = useData();
  const router = useRouter();
  const ref = useRef(null);
  const [isVisible, setIsVisible] = useState(true);
  const [isRequired, setIsRequired] = useState(item?.reqd || false);
  const [isReadOnly, setIsReadOnly] = useState(item?.read_only || false);

  useEffect(() => {
    if (item?.depends_on) {
      const visibility = evaluateDependsOn(item.depends_on, form);
      setIsVisible(visibility);

      // Dynamically set "required" if depends_on conditions are met
      if (item?.reqd && visibility) {
        setIsRequired(true);
      } else {
        setIsRequired(false);
      }
    }
  }, [form, item?.depends_on]);

  useEffect(() => {
    // Only enforce submittable checks if we're editing an existing document (has ID)
    if (router.query.id && localConfig?.is_submittable && data?.docstatus) {
      if (data.docstatus === 2) {
        // Cancelled document - always readonly
        setIsReadOnly(true);
      } else if (data.docstatus === 1) {
        // Submitted document - check allow_on_submit
        if (item.allow_on_submit) {
          setIsReadOnly(false);
        } else {
          setIsReadOnly(true);
        }
      }
    } else {
      // For new documents or non-submittable forms, use the original read_only value
      setIsReadOnly(item?.read_only || false);
    }
  }, [
    router.query.id,
    localConfig?.is_submittable,
    data?.docstatus,
    item?.allow_on_submit,
    item?.read_only,
  ]);

  if (!item) {
    console.error(`Item is undefined`);
    return null;
  }

  const fieldValue = form?.[item?.fieldname] || null;

  const handleSelect = (e) => {
    e.stopPropagation();
    handleFocus(item);
  };

  const handleChange = (field, value) => {
    setForm((prevData) => ({
      ...prevData,
      [field.fieldname]: value,
    }));
  };

  if (!isVisible) return null;

  return (
    <div
      ref={ref}
      className={`relative flex flex-col w-full break-words rounded-md font-bold text-[14px] px-2 text-gray-900 my-4 
        ${selectedItem === item ? "border-yellow-600" : "border-gray-300"} 
        ${
          isReadOnly
            ? "border text-gray-400 bg-gray-50 cursor-not-allowed"
            : item.fieldtype === "Check" ||
              item.fieldtype === "Button" ||
              item.fieldtype === "MultiSelect" ||
              item.fieldtype === "Table"
            ? "border-none bg-transparent py-2"
            : "border min-h-10 bg-white"
        } 
        ${item?.hidden || (isReadOnly && !fieldValue) ? "hidden" : ""}
      `}
      onClick={handleSelect}
      tabIndex={0}
    >
      <FieldRenderer
        fieldtype={item.fieldtype}
        item={item}
        value={fieldValue}
        placeholder={item?.label}
        handleInputChange={handleChange}
        label={item.label}
        required={isRequired}
        readOnly={isReadOnly}
        disabled={item.disabled || isReadOnly}
      />
    </div>
  );
};

export default FieldItem;
