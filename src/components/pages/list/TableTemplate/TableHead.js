import React from "react";

const TableHead = ({
  updatedFields,
  data,
  handleSelectAll,
  selectedRows,
  config,
}) => {
  // Check if we should show docstatus column
  const showDocStatus = config?.is_submittable;
  // Check if we should show custom status column
  const showCustomStatus =
    config?.states &&
    updatedFields?.some(
      (field) => field.fieldname === "status" || field.id === "status"
    );

  return (
    <thead className="bg-white shodow-lg shadow-black sticky top-0 w-full">
      <tr>
        <th
          className="items-start text-left sticky top-0 ml-4 z-10 shadow"
          style={{ position: "sticky", top: 0 }}
        >
          <input
            type="checkbox"
            onChange={handleSelectAll}
            checked={selectedRows.length === data.length}
          />
        </th>
        {/* Always show ID column first */}
        <th className="px-2 py-3 font-bold text-left uppercase align-middle shadow text-xs border-b-solid tracking-none text-slate-400 opacity-100 sticky top-0 z-10">
          ID
        </th>

        {/* Show docstatus column if document is submittable */}
        {showDocStatus && (
          <th className="px-2 py-3 font-bold text-left uppercase align-middle shadow text-xs border-b-solid tracking-none text-slate-400 opacity-100 sticky top-0 z-10">
            Status
          </th>
        )}

        {/* Show custom status column if configured */}
        {showCustomStatus && (
          <th className="px-2 py-3 font-bold text-left uppercase align-middle shadow text-xs border-b-solid tracking-none text-slate-400 opacity-100 sticky top-0 z-10">
            State
          </th>
        )}

        {/* Render other fields */}
        {updatedFields
          ?.filter(
            (field) =>
              field.fieldname !== "status" &&
              field.id !== "status" &&
              field.id !== "id" &&
              field.fieldname !== "docstatus"
          )
          ?.map((field, index) => (
            <th
              key={index}
              className="px-2 py-3 font-bold text-left uppercase align-middle shadow text-xs border-b-solid tracking-none text-slate-400 opacity-100 sticky top-0 z-10"
            >
              {field.name || field.label}
            </th>
          ))}

        {data[0]?.created && (
          <th className="px-2 py-3 font-bold text-left uppercase align-middle shadow text-xs border-b-solid tracking-none text-slate-400 opacity-100 sticky top-0 z-10">
            Created
          </th>
        )}
        {data[0]?.modified && (
          <th className="px-2 py-3 font-bold text-left uppercase align-middle shadow text-xs border-b-solid tracking-none text-slate-400 opacity-100 sticky top-0 z-10">
            Modified
          </th>
        )}
        <th className="px-2 py-3 font-semibold capitalize align-middle shadow tracking-none text-slate-400 opacity-100 sticky top-0 z-10"></th>
        <th className="px-2 py-3 font-semibold capitalize align-middle shadow tracking-none text-slate-400 opacity-100 sticky top-0 z-10"></th>
      </tr>
    </thead>
  );
};

export default TableHead;
