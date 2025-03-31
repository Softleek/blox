import { useConfig } from "@/contexts/ConfigContext";
import React, { useEffect, useState } from "react";
import SectionItem from "./SectionItem";
import { useData } from "@/contexts/DataContext";
import { evaluateDependsOn } from "@/utils/evaluationUtils";

const Section = ({ section, handleFocus, handleBlur }) => {
  const { selectedItem } = useConfig();
  const { form } = useData();
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    if (section?.depends_on) {
      const visibility = evaluateDependsOn(section.depends_on, form);
      setIsVisible(visibility);
    }
  }, [form, section?.depends_on]);

  if (!isVisible) return null;

  return (
    <div>
      <SectionItem
        section={section}
        handleFocus={handleFocus}
        handleBlur={handleBlur}
        selectedItem={selectedItem}
      />
    </div>
  );
};

export default Section;
