import React from "react";
import Link from "next/link";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faEdit,
  faTrash,
  faInfoCircle,
} from "@fortawesome/free-solid-svg-icons";
import { timeAgo } from "@/utils/DateFormat";
import handleDelete from "./DeleteHandler";
import { useModal } from "@/contexts/ModalContext";
import { motion } from "framer-motion";
import { Edit, CheckCircle2, XCircle } from "lucide-react";
import CustomTooltip from "@/components/tooltip/CustomTooltip";

const TableBody = ({
  data,
  updatedFields,
  selectedRows,
  handleSelectRow,
  currentPathWithoutParams,
  onEdit,
  onDeleteCallback,
  endpoint,
  setLoading,
  refresh,
  config,
}) => {
  const { openModal } = useModal();

  // Function to get docstatus label and style
  const getDocStatusInfo = (docstatus) => {
    if (!config?.is_submittable) return null;

    const statusMap = {
      0: {
        label: "Draft",
        bg: "bg-yellow-500/10",
        text: "text-yellow-800",
        border: "border-yellow-200",
        icon: <Edit className="w-3 h-3 mr-1" />,
        description: "This document is in draft state and not submitted yet",
      },
      1: {
        label: "Submitted",
        bg: "bg-green-500/10",
        text: "text-green-800",
        border: "border-green-200",
        icon: <CheckCircle2 className="w-3 h-3 mr-1" />,
        description: "This document has been submitted and is active",
      },
      2: {
        label: "Cancelled",
        bg: "bg-red-500/10",
        text: "text-red-800",
        border: "border-red-200",
        icon: <XCircle className="w-3 h-3 mr-1" />,
        description: "This document has been cancelled and is no longer active",
      },
    };

    return statusMap[docstatus] || null;
  };

  // Function to get custom status label and style
  const getCustomStatusInfo = (status) => {
    if (!status || !config?.states) return null;

    const stateConfig = config.states.find((state) => state.title === status);

    if (!stateConfig) return null;

    const colorMap = {
      Blue: {
        bg: "bg-blue-500/10",
        text: "text-blue-800",
        border: "border-blue-200",
      },
      Green: {
        bg: "bg-green-500/10",
        text: "text-green-800",
        border: "border-green-200",
      },
      Red: {
        bg: "bg-red-500/10",
        text: "text-red-800",
        border: "border-red-200",
      },
      Orange: {
        bg: "bg-orange-500/10",
        text: "text-orange-800",
        border: "border-orange-200",
      },
      Purple: {
        bg: "bg-purple-500/10",
        text: "text-purple-800",
        border: "border-purple-200",
      },
      Pink: {
        bg: "bg-pink-500/10",
        text: "text-pink-800",
        border: "border-pink-200",
      },
      Gray: {
        bg: "bg-gray-500/10",
        text: "text-gray-800",
        border: "border-gray-200",
      },
    };

    const colors = colorMap[stateConfig.color] || {
      bg: "bg-gray-500/10",
      text: "text-gray-800",
      border: "border-gray-200",
    };

    return {
      label: stateConfig.title,
      description: stateConfig.description,
      ...colors,
    };
  };

  const renderField = (field, item) => {
    const field_id = field?.id?.toString() || field?.fieldname?.toString();
    const value = item[field_id];

    // Handle empty values
    if (value === undefined || value === null || value === "") {
      return <span className="text-gray-400">-</span>;
    }

    switch (field.type) {
      case "text":
        return <span className="truncate max-w-xs">{value}</span>;
      case "number":
        return <span>{Number(value).toLocaleString()}</span>;
      case "date":
        return <span>{new Date(value).toLocaleDateString()}</span>;
      case "datetime":
        return <span>{new Date(value).toLocaleString()}</span>;
      case "boolean":
        return (
          <span
            className={`px-2 py-1.5 rounded-full text-xs ${
              value ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"
            }`}
          >
            {value ? "Yes" : "No"}
          </span>
        );
      case "options":
      case "select":
      case "status":
        const statusInfo = getCustomStatusInfo(value);
        return statusInfo ? (
          <div className="flex items-center">
            <span
              className={`px-2 py-1.5 text-xs rounded-full ${statusInfo.bg} ${statusInfo.text} border ${statusInfo.border}`}
            >
              {statusInfo.label}
            </span>
            {statusInfo.description && (
              <CustomTooltip content={statusInfo.description}>
                <FontAwesomeIcon
                  icon={faInfoCircle}
                  className="w-3 h-3 ml-1 text-gray-400 cursor-help"
                />
              </CustomTooltip>
            )}
          </div>
        ) : (
          <span>{value}</span>
        );
      case "link":
        return (
          <Link
            href={value}
            className="text-blue-500 underline hover:text-blue-700 truncate max-w-xs"
          >
            {value}
          </Link>
        );
      case "image":
        return (
          <div className="flex items-center">
            <img
              src={value}
              className="w-8 h-8 rounded-full object-cover"
              alt={field.label}
              onError={(e) => {
                e.target.onerror = null;
                e.target.src = "/img/default-avatar.png";
              }}
            />
          </div>
        );
      default:
        return <span className="truncate max-w-xs">{value}</span>;
    }
  };

  return (
    <tbody>
      {data?.map((item, index) => {
        const docStatusInfo = getDocStatusInfo(item.docstatus);
        const customStatusInfo = getCustomStatusInfo(item.status);
        const isSelected = selectedRows.includes(item.id);

        return (
          <motion.tr
            key={index}
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3, delay: index * 0.05 }}
            className={`
              ${index % 2 ? "bg-pink-50" : "bg-white"}
              hover:bg-purple-100
              ${isSelected ? "ring-1 ring-pink-300" : ""}
            `}
          >
            {/* Checkbox column */}
            <td className="px-1 py-1.5 whitespace-nowrap">
              <input
                type="checkbox"
                checked={isSelected}
                onChange={() => handleSelectRow(item.id)}
                className="h-3 w-3 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
              />
            </td>
            {/* ID Column */}
            <td className="px-1 py-1.5 whitespace-nowrap">
              <Link href={`${currentPathWithoutParams}/${item.id}`}>
                <span className="text-purple-600 hover:text-purple-800 hover:underline font-medium">
                  {item.id}
                </span>
              </Link>
            </td>

            {/* ID is automatically rendered as the first field in updatedFields */}

            {/* Docstatus Column */}
            {config?.is_submittable && (
              <td className="px-1 py-1.5 whitespace-nowrap">
                {docStatusInfo && (
                  <span
                    className={`px-2 py-1.5 text-xs rounded-full flex items-center ${docStatusInfo.bg} ${docStatusInfo.text} border ${docStatusInfo.border}`}
                  >
                    {docStatusInfo.icon}
                    {docStatusInfo.label}
                  </span>
                )}
              </td>
            )}

            {/* Custom Status Column */}
            {config?.states && item.status && (
              <td className="px-1 py-1.5 whitespace-nowrap">
                {customStatusInfo && (
                  <div className="flex items-center">
                    <span
                      className={`px-2 py-1.5 text-xs rounded-full ${customStatusInfo.bg} ${customStatusInfo.text} border ${customStatusInfo.border}`}
                    >
                      {customStatusInfo.label}
                    </span>
                    {customStatusInfo.description && (
                      <FontAwesomeIcon
                        icon={faInfoCircle}
                        className="w-3 h-3 ml-1 text-gray-400 cursor-help"
                      />
                    )}
                  </div>
                )}
              </td>
            )}

            {/* Other Fields */}
            {updatedFields
              ?.filter(
                (field) =>
                  field.fieldname !== "status" &&
                  field.id !== "status" &&
                  field.id !== "id" &&
                  field.fieldname !== "docstatus"
              )
              ?.map((field, fieldIndex) => (
                <td key={fieldIndex} className="px-1 py-1.5 whitespace-nowrap">
                  {renderField(field, item)}
                </td>
              ))}

            {/* Timestamps */}
            <td className="px-1 py-1.5 whitespace-nowrap text-xs text-gray-500">
              {item?.created && (
                <div className="flex items-center">
                  <span className="inline-block w-1.5 h-1.5 rounded-full bg-green-500 mr-2"></span>
                  <span> {timeAgo(new Date(item.created))}</span>
                </div>
              )}
            </td>
            <td className="px-1 py-1.5 whitespace-nowrap text-xs text-gray-500">
              {item?.modified && (
                <div className="flex items-center">
                  <span className="inline-block w-1.5 h-1.5 rounded-full bg-blue-500 mr-2"></span>
                  <span>{timeAgo(new Date(item.modified))}</span>
                </div>
              )}
            </td>

            {/* Action buttons */}
            <td className="px-1 py-1.5 whitespace-nowrap text-right text-xs font-medium">
              <button
                onClick={() => onEdit(item)}
                className="text-blue-600 hover:text-blue-900 mr-4"
                title="Edit"
              >
                <FontAwesomeIcon icon={faEdit} />
              </button>
              <button
                onClick={() =>
                  handleDelete({
                    id: item.id,
                    endpoint,
                    openModal,
                    setLoading,
                    refresh,
                  })
                }
                className="text-red-600 hover:text-red-900"
                title="Delete"
              >
                <FontAwesomeIcon icon={faTrash} />
              </button>
            </td>
          </motion.tr>
        );
      })}
    </tbody>
  );
};

export default TableBody;
