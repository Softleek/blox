import React, { useRef, useEffect, useState } from "react";
import { useConfig } from "@/contexts/ConfigContext";
import FieldRenderer from "./FieldRenderer";
import { useData } from "@/contexts/DataContext";
import { evaluateDependsOn } from "@/utils/evaluationUtils";

const FieldItem = ({ item, handleFocus, placeholder = false }) => {
  const { selectedItem, setSelectedItem } = useConfig();
  const { form, setForm, data } = useData();
  const ref = useRef(null);
  const [isVisible, setIsVisible] = useState(true);
  const [isRequired, setIsRequired] = useState(item?.reqd || false);

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
          item?.read_only
            ? "text-gray-500"
            : item.fieldtype === "Check" ||
              item.fieldtype === "Button" ||
              item.fieldtype === "MultiSelect" ||
              item.fieldtype === "Table"
            ? "border-none bg-transparent py-2"
            : "border min-h-10 bg-white"
        } 
        ${item?.hidden || (item?.read_only && !fieldValue) ? "hidden" : ""}
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
        readOnly={item.read_only}
        disabled={item.disabled}
      />
    </div>
  );
};

export default FieldItem;
