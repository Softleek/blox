// components/core/DocHeader.js

import React, { useEffect, useRef, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useNavbar } from "@/contexts/NavbarContext";
import { getFromDB } from "@/utils/indexedDB";
import Loading from "@/components/core/account/Loading";
import { useRouter } from "next/navigation";
import ButtonGroup from "../buttons/ButtonGroup";
import PrimaryButton from "../buttons/Primary";
import Link from "next/link";
import { toTitleCase } from "@/utils/textConvert";
import { useRouter as useRt } from "next/router";
import { toast } from "react-toastify";
import { postData } from "@/utils/Api";
import { useStatusHandler } from "@/custom/masafa";
import useLoadingOffloadingKeyEvents from "@/hooks/useLoadingOffloadingKeyEvents";
import CustomMessageModal from "../modal/CustomMessageModal";
import { useConfig } from "@/contexts/ConfigContext";
import { useData } from "@/contexts/DataContext";
import { useDocActions } from "@/hooks/useDocActions";
import { removeIdAndRelatedFields } from "@/components/pages/form/actions/handleDuplicate";
import { Edit, CheckCircle2, XCircle } from "lucide-react";

const DocHeader = ({
  title,
  link = "#",
  subtitle,
  tabs,
  handleTabClick,
  selectedTab,
  isEditing,
  handleSaveClick,
  actions = [],
  buttons = [],
  config,
  data,
}) => {
  const componentRef = useRef();
  const { dashboardText } = useNavbar();
  const [perms, setPerms] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const { localConfig, localAppData } = useConfig();
  const { form, setForm, setLoading, data: localData, setData } = useData();

  const router = useRouter();

  const rt = useRt();

  const { slug, id } = rt?.query;

  const { errorModal, currentStatus, action, updateStatus, handleScannedCode } =
    useStatusHandler(dashboardText);
  const [canEdit, setCanEdit] = useState(false);
  const [canDelete, setCanDelete] = useState(false);

  const { handleSubmit, handleCancel, isProcessing } = useDocActions({
    localConfig,
    localData,
    setForm,
    setData,
    setLoading,
    localAppData,
    slug,
    id,
  });

  useEffect(() => {
    const checkAuth = async () => {
      const perm = await getFromDB("permissions");
      setPerms(perm);
    };
    checkAuth();
  }, [router]);

  useEffect(() => {
    if (perms != null && perms === "all") {
      setCanEdit(true);
      setCanDelete(true);
    } else if (perms != null) {
      const permission = `${dashboardText?.toLowerCase()}_change`;
      setCanEdit(perms?.includes(permission));
      setCanDelete(perms?.includes(`${dashboardText?.toLowerCase()}_delete`));
    }
  }, [perms, dashboardText]);

  useLoadingOffloadingKeyEvents("Loading", handleScannedCode);

  const handleAmend = async () => {
    // Set form data with amended_from
    setForm((prev) => ({
      ...removeIdAndRelatedFields(prev),
      amended_from: id, // Store the original ID
      docstatus: 0, // Reset docstatus to 0 for the new document
    }));

    const newPath = `/app/${slug}/new`;
    router.push(newPath);
  };

  // Function to get status label and style based on docstatus
  const getDocStatusInfo = () => {
    if (!localConfig?.is_submittable) return null;

    const statusMap = {
      0: {
        label: "Draft",
        color: "bg-yellow-600 text-purple-100 font-bold",
        icon: <Edit className="w-3.5 h-3.5 mr-1" />,
      },
      1: {
        label: "Submitted",
        color: "bg-green-600 text-purple-100 font-bold",
        icon: <CheckCircle2 className="w-3.5 h-3.5 mr-1" />,
      },
      2: {
        label: "Cancelled",
        color: "bg-red-600 text-purple-100 font-bold",
        icon: <XCircle className="w-3.5 h-3.5 mr-1" />,
      },
    };

    return statusMap[localData.docstatus] || null;
  };

  // Function to get status label and style based on status field and config.states
  const getCustomStatusInfo = () => {
    if (!localData?.status || !localConfig?.states) return null;

    const stateConfig = localConfig.states.find(
      (state) => state.title === localData.status
    );

    if (!stateConfig) return null;

    const colorMap = {
      Blue: "bg-blue-600 text-blue-100",
      Green: "bg-green-600 text-green-100",
      Red: "bg-red-600 text-red-100",
      Orange: "bg-orange-600 text-orange-100",
      // Add more colors as needed
    };

    return {
      label: stateConfig.title,
      color: colorMap[stateConfig.color] || "bg-gray-600 text-gray-100",
      icon: <CheckCircle2 className="w-3.5 h-3.5 mr-1" />,
    };
  };

  const docStatusInfo = getDocStatusInfo();
  const customStatusInfo = getCustomStatusInfo();

  return (
    <>
      {isLoading && <Loading />}
      <div
        className="relative flex items-center mx-4 mt-4 md:mt-0 p-0 bg-center bg-cover min-h-14 rounded-2xl"
        style={{
          backgroundImage: `url('/img/curved-images/curved0.jpg')`,
          backgroundPositionY: "50%",
        }}
      >
        <span className="absolute inset-y-0 w-full h-full bg-center bg-cover bg-gradient-to-tl from-purple-700 to-pink-500 opacity-60 rounded-xl"></span>
      </div>
      <div
        style={{
          zIndex: 2,
        }}
        className="relative flex flex-col flex-auto min-w-0 px-4 py-1 mx-6 -mt-10 break-words border-0 shadow-blur rounded-2xl bg-white bg-clip-border backdrop-blur-2xl backdrop-saturate-200"
      >
        <div className="flex flex-wrap -mx-3 min-h-12 justify-between">
          <div className="flex-none w-auto max-w-full px-3 my-auto">
            <div className="h-full">
              <div className="flex items-center">
                <Link href={link}>
                  <h5 className="mb-1 text-gray-900 font-bold">{title}</h5>
                </Link>
                {docStatusInfo && (
                  <span
                    className={`ml-2 px-2 py-1 text-xs font-bold rounded-full flex items-center ${docStatusInfo.color}`}
                  >
                    {docStatusInfo.icon}
                    {docStatusInfo.label}
                  </span>
                )}
                {customStatusInfo && (
                  <span
                    className={`ml-2 px-2 py-1 text-xs font-bold rounded-full flex items-center ${customStatusInfo.color}`}
                  >
                    {customStatusInfo.icon}
                    {customStatusInfo.label}
                  </span>
                )}
              </div>
              <p className="mb-0 font-semibold leading-normal text-sm">
                {subtitle}
              </p>
            </div>
          </div>
          <div className="px-2 md:px-3 flex flex-wrap items-center justify-end w-fit">
            <div className="relative right-0 flex flex-wrap items-center justify-end w-full">
              <ul className="relative flex flex-wrap p-1 list-none bg-transparent">
                {tabs?.map((tab) => (
                  <li
                    key={tab.name}
                    className="z-30 flex-auto text-center cursor-pointer"
                  >
                    <a
                      onClick={() => handleTabClick(tab.name)}
                      className={`z-30 block w-full px-4 py-1 mb-0 transition-all border-0 rounded-lg ease-soft-in-out ${
                        selectedTab === tab.name
                          ? "bg-white text-slate-700"
                          : "bg-inherit text-slate-700"
                      }`}
                    >
                      <FontAwesomeIcon
                        icon={tab.icon}
                        className="text-slate-700"
                      />
                      <span className="ml-1">{tab.label}</span>
                    </a>
                  </li>
                ))}
              </ul>
              <div className="flex flex-wrap space-x-2 w-full items- w-fit justify-start md:justify-end">
                {action && (
                  <PrimaryButton text={action} onClick={updateStatus} />
                )}
                <ButtonGroup buttons={buttons} />
                {isEditing &&
                  handleSaveClick &&
                  ((localConfig?.is_submittable &&
                    localData?.docstatus === 0) ||
                    !localConfig?.is_submittable ||
                    !id) && (
                    <button type="button" onClick={handleSaveClick}>
                      <PrimaryButton
                        text="Save"
                        className="flex items-center justify-center p-1"
                      />
                    </button>
                  )}

                {localData && id && (
                  <>
                    {isEditing && localData.docstatus === 1 && (
                      <PrimaryButton
                        text="Update"
                        onClick={handleSaveClick}
                        disabled={isProcessing}
                      />
                    )}

                    {localConfig?.is_submittable &&
                      localData.docstatus === 0 &&
                      !isEditing && (
                        <PrimaryButton
                          text="Submit"
                          onClick={handleSubmit}
                          disabled={isProcessing}
                        />
                      )}

                    {localData.docstatus === 1 && (
                      <PrimaryButton
                        text="Cancel"
                        onClick={handleCancel}
                        disabled={isProcessing}
                      />
                    )}
                    {localData?.docstatus === 2 && (
                      <PrimaryButton text="Amend" onClick={handleAmend} />
                    )}
                  </>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
      {errorModal?.isOpen && (
        <CustomMessageModal
          isOpen={errorModal?.isOpen}
          onRequestClose={errorModal?.onRequestClose}
          message={errorModal?.message}
          title={errorModal?.title}
          onProceed={errorModal?.onProceed}
        />
      )}
    </>
  );
};

export default DocHeader;
