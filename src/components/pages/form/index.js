// src/components/pages/form/DoctypeForm.js
import React, { useEffect, useRef, useState, useCallback } from "react";
import DocHeader from "@/components/core/common/header/DocHeader";
import DetailForm from "./DetailForm";
import { useConfig } from "@/contexts/ConfigContext";
import { useData } from "@/contexts/DataContext";
import { useRouter } from "next/router";
import { useModal } from "@/contexts/ModalContext";
import SendEmail from "@/components/functions/communication/SendEmail";
import SendSms from "@/components/functions/communication/SendSms";
import { useFormEvents } from "@/hooks/useFormEvents";
import { useFormLogic } from "@/hooks/useFormLogic";
import { useFormButtons } from "@/hooks/useFormButtons";
import { useFormValidation } from "@/hooks/useFormValidation";
import { useKeyboardShortcuts } from "@/hooks/useKeyboardShortcuts";

const DoctypeForm = ({ handleSave, config, title }) => {
  const [smsModalOpen, setSmsModalOpen] = useState(false);
  const [emailModalOpen, setEmailModalOpen] = useState(false);
  const { localConfig, localAppData } = useConfig();
  const { form, setForm, setLoading, data, setData, doc, setDoc } = useData();
  const router = useRouter();
  const { openModal } = useModal();
  const { slug, id } = router.query;
  const formRef = useRef(null);

  const { initializeFormEvents } = useFormEvents(form, setForm, doc, setDoc);
  const { isEditing, handleSaveClick: originalHandleSaveClick } = useFormLogic(
    form,
    setForm,
    data,
    localConfig,
    handleSave
  );
  const { validateRequiredFields, showValidationErrors } = useFormValidation();

  // Define handleSaveClick using useCallback to maintain stable reference
  const handleSaveClick = useCallback(
    async (e) => {
      e?.preventDefault();

      // const validation = validateRequiredFields(form, localConfig);
      // if (!validation.isValid) {
      //   showValidationErrors(validation.errors);
      //   return;
      // }

      await originalHandleSaveClick(e);
    },
    [
      form,
      doc?.meta?.requiredFields,
      validateRequiredFields,
      showValidationErrors,
      originalHandleSaveClick,
    ]
  );

  // Initialize keyboard shortcuts after handleSaveClick is defined
  const { setupShortcuts } = useKeyboardShortcuts({
    form,
    router,
    slug,
    handleSave: handleSaveClick,
    disabled: !isEditing,
  });

  const { buttons } = useFormButtons(
    form,
    setForm,
    router,
    openModal,
    localAppData?.endpoint,
    setLoading,
    data,
    setData,
    slug,
    setSmsModalOpen,
    setEmailModalOpen,
    setDoc,
    localConfig
  );

  useEffect(() => {
    if (slug) {
      initializeFormEvents(slug);
    }
    return setupShortcuts();
  }, [slug, form, router, isEditing, initializeFormEvents, setupShortcuts]);

  const ComponentBefore = doc?.componentBefore || null;
  const ComponentAfter = doc?.componentAfter || null;
  const ComponentReplace = doc?.componentReplace || null;

  return (
    <div className="flex flex-col">
      <DocHeader
        isEditing={isEditing}
        handleSaveClick={handleSaveClick}
        title={id || slug || title}
        buttons={buttons}
      />
      <div className="relative z-1 px-4 flex flex-col mt-2 w-full">
        {ComponentBefore && <ComponentBefore />}
        <div className="h-full shadow-md shadow-slate-300">
          {ComponentReplace ? <ComponentReplace /> : <DetailForm />}
        </div>
        {ComponentAfter && <ComponentAfter />}
      </div>
      <SendEmail
        isOpen={emailModalOpen}
        msg="Hi,"
        email={form?.email}
        onRequestClose={() => setEmailModalOpen(false)}
      />
      <SendSms
        isOpen={smsModalOpen}
        msg="Hi,"
        phone={form?.phone}
        onRequestClose={() => setSmsModalOpen(false)}
      />
    </div>
  );
};

export default DoctypeForm;
