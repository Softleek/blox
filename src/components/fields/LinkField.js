import React, { useState, useRef, useCallback } from "react";
import { fetchData } from "@/utils/Api";
import { toast } from "react-toastify";
import { toUnderscoreLowercase } from "@/utils/textConvert";
import { useConfig } from "@/contexts/ConfigContext";
import { motion, AnimatePresence } from "framer-motion";
import QuickEntryModal from "../pages/list/quickentry";
import { findDocDetails } from "@/utils/findDocDetails";
import { importFile } from "@/utils/importFile";
import { ArrowRight, ArrowUpRight } from "lucide-react";

const LinkField = ({
  value = "",
  onChange,
  placeholder = "",
  isMulti = false,
  readOnly = false,
  preview = false,
  hidden = false,
  field,
  required = false,
  ...rest
}) => {
  const [endpoint, setEndpoint] = useState(null);
  const [appData, setAppData] = useState(null);
  const [options, setOptions] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [isQuickEntryModalOpen, setIsQuickEntryModalOpen] = useState(false);
  const { selectedItem, setSelectedItem } = useConfig();
  const inputRef = useRef(null);

  const initializeField = useCallback(async () => {
    if (!field) return;

    try {
      const slug = toUnderscoreLowercase(field.options);

      const docData = findDocDetails(slug);

      if (!docData) {
        setEndpoint(`${slug}`);

        setAppData({
          search_fields: field?.search_fields || "id",
          title_field: field?.title_field || "id",
        });

        if (value) {
          const response = await fetchData({}, `${slug}/${value}`);

          setSearchTerm(response?.data.id);
        }
      } else {
        setEndpoint(`${docData.app}/${slug}`);

        const configData = await importFile(slug, `${slug}.json`);

        setAppData(configData.content);

        if (value) {
          const titleField =
            configData.content?.title_field || configData.content?.id_field;
          if (typeof value === "string" || typeof value === "number") {
            const response = await fetchData(
              {},
              `${docData.app}/${slug}/${value}`
            );
            const newValue = response?.data;

            setSearchTerm(newValue[titleField] || newValue.id);
          } else {
            setSearchTerm(value[titleField] || value.id || value);
          }
        }
      }
    } catch (error) {
      // toast.error(error.message || "Error initializing field");
    }
  }, [field, value]);

  const fetchOptions = useCallback(
    async (search = "") => {
      if (!endpoint || readOnly || preview || hidden) return;

      try {
        const response = await fetchData({ page_length: 10, search }, endpoint);

        const fetchedOptions =
          response?.data?.data?.map((option) => {
            let searchFields = [];

            if (appData.search_fields) {
              if (Array.isArray(appData.search_fields)) {
                searchFields = appData.search_fields.map((key) => key.trim());
              } else if (typeof appData.search_fields === "string") {
                searchFields = appData.search_fields.includes(",")
                  ? appData.search_fields.split(",").map((key) => key.trim())
                  : [appData.search_fields.trim()];
              }
            }

            if (appData.title_field && !searchFields.includes("id")) {
              searchFields.unshift("id");
            }

            const subFields = searchFields
              .map((key) => option[key])
              .filter(Boolean)
              .join(", ");

            return {
              value: option.id,
              label: option[appData.title_field] || option.id,
              subFields: subFields,
            };
          }) || [];

        setOptions([
          ...fetchedOptions,
          {
            value: "add-new",
            label: "+ Add new",
            subFields: "",
            isAddNew: true,
          },
        ]);
      } catch (error) {
        setOptions([
          {
            value: "add-new",
            label: "+ Add new",
            subFields: "",
            isAddNew: true,
          },
        ]);
      }
    },
    [endpoint, appData, readOnly, preview, hidden]
  );

  const handleInputChange = (e) => {
    const term = e.target.value;
    setSearchTerm(term);
    fetchOptions(term);
    setIsDropdownOpen(true);
  };

  const handleSelectionChange = (option) => {
    if (option?.isAddNew) {
      setIsQuickEntryModalOpen(true);
    } else {
      setSearchTerm(option.label);
      onChange(option.value);
      setSelectedItem(null);
      setIsDropdownOpen(false);
    }
  };

  const handleClose = async (response) => {
    setIsQuickEntryModalOpen(false);
    if (response?.id) {
      const newLabel = response[appData.title_field] || response.id;
      setSearchTerm(newLabel);
      onChange(response);
      await fetchOptions();
    }
  };

  const clearSelection = () => {
    setSearchTerm("");
    onChange(null);
    setSelectedItem(null);
    fetchOptions("");
  };

  const openLink = () => {
    if (endpoint && searchTerm) {
      window.open(
        `/app/${toUnderscoreLowercase(field.options)}/${value?.id || value}`,
        "_blank"
      );
    }
  };

  React.useEffect(() => {
    initializeField();
  }, [initializeField]);

  if (hidden || preview) return null;

  return (
    <div className="relative w-full">
      {isQuickEntryModalOpen && (
        <QuickEntryModal
          isOpen={isQuickEntryModalOpen}
          onClose={handleClose}
          doc={appData?.name}
          configData={appData}
          redirect={false}
        />
      )}
      <div className="relative w-full flex flex-row items-center justify-between">
        <input
          ref={inputRef}
          type="text"
          value={searchTerm}
          onChange={handleInputChange}
          placeholder={placeholder}
          className={`px-1 w-full focus:outline-none focus:ring-0 focus:border-none ${
            readOnly ? "cursor-pointer" : ""
          }`}
          disabled={readOnly || preview}
          onFocus={() => {
            setIsDropdownOpen(true);
            fetchOptions(searchTerm);
          }}
          onBlur={(e) => {
            if (!e.relatedTarget?.closest(".dropdown-item")) {
              setIsDropdownOpen(false);
            }
          }}
          required={required}
          {...rest}
        />
        <button
          type="button"
          onMouseDown={(e) => {
            e.preventDefault();
            openLink();
          }}
          className="px-2 rounded-full  text-purple-600  transition-all duration-200 group"
          title="Open link"
          aria-label="Open link"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            className="w-5 h-5 transition-transform duration-300 transform group-hover:translate-x-1 group-hover:rotate-12"
          >
            <path
              fillRule="evenodd"
              d="M4.25 5.5a.75.75 0 00-.75.75v8.5c0 .414.336.75.75.75h8.5a.75.75 0 00.75-.75v-4a.75.75 0 011.5 0v4A2.25 2.25 0 0112.75 17h-8.5A2.25 2.25 0 012 14.75v-8.5A2.25 2.25 0 014.25 4h5a.75.75 0 010 1.5h-5z"
              clipRule="evenodd"
            />
            <path
              fillRule="evenodd"
              d="M6.194 12.753a.75.75 0 001.06.053L16.5 4.44v2.81a.75.75 0 001.5 0v-4.5a.75.75 0 00-.75-.75h-4.5a.75.75 0 000 1.5h2.553l-9.056 8.194a.75.75 0 00-.053 1.06z"
              clipRule="evenodd"
            />
          </svg>
        </button>
      </div>
      <AnimatePresence>
        {isDropdownOpen && options.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="absolute w-full mt-1 bg-white text-left border border-gray-300 rounded-sm shadow-lg z-10 max-h-80 overflow-y-auto"
          >
            {options.map((option) => (
              <div
                key={option.value}
                className={`dropdown-item cursor-pointer py-1 px-2 text-sm hover:bg-gray-100 ${
                  searchTerm === option.label ? "bg-gray-200" : ""
                }`}
                onMouseDown={(e) => {
                  e.preventDefault();
                  handleSelectionChange(option);
                }}
              >
                <div className="space-y-1">
                  <div
                    className={`font-semibold text-sm ${
                      option.isAddNew ? "text-blue-600" : "text-black"
                    }`}
                  >
                    {option.label}
                  </div>
                  {option.subFields && !option.isAddNew && (
                    <div className="text-xs text-gray-500">
                      {option.subFields}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default LinkField;
