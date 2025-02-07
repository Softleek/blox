import React from "react";
import FieldInput from "./FieldInput";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEdit, faTrash, faCopy } from "@fortawesome/free-solid-svg-icons";
import { toUnderscoreLowercase } from "@/utils/textConvert";

const TableRow = ({
  rowIndex,
  row,
  columnsData,
  selectedRows,
  setSelectedRows,
  handleCellChange,
  readOnly,
  preview,
  handleRowEdit,
  handleRowSelect,
  handleDeleteRow,
  handleDuplicateRow, // New prop for duplicating a row
  getFieldDetails,
  configData,
}) => {
  const openFullForm = () => {
    if (configData?.name && row?.id) {
      window.open(
        `/app/${toUnderscoreLowercase(configData?.name)}/${row?.id}`,
        "_blank"
      );
    }
  };
  return (
    <tr key={rowIndex}>
      {/* Row selection checkbox */}
      <td className="px-2">
        <input
          type="checkbox"
          checked={selectedRows.includes(rowIndex)}
          onChange={() => handleRowSelect(rowIndex)}
          className="form-checkbox text-center"
        />
      </td>
      {/* Index Column (No Data Stored) */}
      {/* <td className="p-1 text-center border-r-[1px] border-gray-200">
        {rowIndex + 1} 
      </td> */}
      <td className="text-center border-r-[1px] border-gray-200">
        <span
          onClick={openFullForm}
          className={`px-2 text-purple-900 text-center border-r-[1px] cursor-pointer hover:text-purple-700 border-gray-200`}
        >
          {row?.id}
        </span>
      </td>
      {/* Row Data */}
      {columnsData.map((column) => (
        <td
          key={column.fieldname}
          className="p-0 w-fit border-b-[1px] border-gray-400"
        >
          <FieldInput
            fieldname={column.fieldname}
            value={row[column.fieldname] || ""}
            onChange={(field, newValue) => {
              handleCellChange(rowIndex, field.fieldname, newValue);
            }}
            readOnly={readOnly}
            preview={preview}
            getFieldDetails={getFieldDetails}
          />
        </td>
      ))}
      {/* Edit, Duplicate, and Delete Buttons */}
      <td
        className={`p-1 flex space-x-2 ${readOnly ? "hidden" : ""}`}
        hidden={readOnly}
      >
        {/* Edit Button */}
        <button
          className="text-blue-500"
          onClick={() => handleRowEdit(rowIndex)}
        >
          <FontAwesomeIcon icon={faEdit} />
        </button>
        {/* Duplicate Button */}
        <button
          className="text-green-500"
          onClick={() => handleDuplicateRow(rowIndex)}
        >
          <FontAwesomeIcon icon={faCopy} />
        </button>
        {/* Delete Button */}
        <button
          className="text-red-500"
          onClick={() => handleDeleteRow(rowIndex)}
        >
          <FontAwesomeIcon icon={faTrash} />
        </button>
      </td>
    </tr>
  );
};

export default TableRow;
