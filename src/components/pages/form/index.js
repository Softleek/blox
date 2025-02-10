import React, { useState, useEffect, useRef } from "react";
import DocHeader from "@/components/core/common/header/DocHeader";
import { useConfig } from "@/contexts/ConfigContext";
import { useData } from "@/contexts/DataContext";
import { useRouter } from "next/router";
import { useModal } from "@/contexts/ModalContext";
import useKeyEvents from "@/hooks/useKeyEvents";
import DetailForm from "./DetailForm";
import * as buttonActions from "./actions";
import { defaultButtons } from "./buttonConfig";
import { wrapButtonProperties } from "./utils/buttonUtils";
import { navigateUp, reloadData } from "./utils/navigationUtils";
import _ from "lodash";
import { toUnderscoreLowercase } from "@/utils/textConvert";

import { validateRequiredFields, cleanData } from "./utils/formUtils";
import ToastTemplates from "@/components/core/common/toast/ToastTemplates";

const DoctypeForm = ({ handleSave, config, customElements, is_doc = true }) => {
  const { localConfig, localAppData } = useConfig();
  const { form, setForm, setLoading, data, setData } = useData();
  const [isEditing, setIsEditing] = useState(false);
  const router = useRouter();
  const { openModal } = useModal();
  const endpoint = localAppData?.endpoint;
  const { slug, id } = router.query;
  const formRef = useRef(null);

  useEffect(() => {
    setIsEditing(!_.isEqual(form, data));
  }, [form, data]);

  useEffect(() => {
    if (config?.onLoad) {
      config.onLoad({ form, setForm, data, setData, router });
    }
  }, [form, data]);

  const handleSaveClick = async (event) => {
    event.preventDefault();
    // const cleanedForm = customElements.lifecycleHooks.beforeSave(form);
    const missingFields = validateRequiredFields(form, localConfig);
    if (missingFields.length > 0) {
      ToastTemplates.warning(
        `Please fill in the required fields: ${missingFields.join(", ")}`
      );
      return;
    }

    const cleanedForm = cleanData(form);
    await handleSave(cleanedForm);
    // customElements.lifecycleHooks.afterSave(cleanedForm);
  };

  useKeyEvents(
    () => {},
    handleSaveClick,
    (props) => buttonActions.handleDuplicate(props)
  );

  const sharedProps = {
    router,
    id,
    form,
    setForm,
    localConfig,
    openModal,
    endpoint,
    setLoading,
    setData,
    data,
    slug,
    navigateUp: () => navigateUp(router),
    reloadData: () => reloadData(router),
    onFieldChange: customElements?.lifecycleHooks?.onFieldChange,
  };

  const buttons = [
    ...defaultButtons,
    ...(customElements?.customButtons || []),
  ].map((button) => wrapButtonProperties(button, sharedProps));

  const link = is_doc
    ? `/app/${toUnderscoreLowercase(localConfig?.name)}`
    : `/${toUnderscoreLowercase(localConfig?.name)}`;

  return (
    <div className="flex flex-col">
      <DocHeader
        isEditing={isEditing}
        handleEditClick={() =>
          buttonActions.handleEditClick(setIsEditing, { id, config, router })
        }
        handleSaveClick={handleSaveClick}
        title={localConfig?.name}
        buttons={buttons}
        link={link}
      />
      <div className="relative z-1 px-4 flex flex-col mt-2 w-full">
        <div className="h-full shadow-md shadow-slate-300">
          {(customElements?.customComponents || []).map((Component, index) => (
            <Component key={index} />
          ))}
          <DetailForm onFieldChange={config?.onFieldChange} />
        </div>
      </div>
    </div>
  );
};

export default DoctypeForm;
