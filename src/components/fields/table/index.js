import React from "react";
import TableRow from "./TableRow";

const Table = ({
  columnsData,
  tableData,
  selectedRows,
  handleCellChange,
  handleDeleteRow,
  handleDuplicateRow,
  handleRowEdit,
  handleSelectAll,
  selectAll,
  readOnly,
  preview,
  getFieldDetails,
  ordered,
  configData,
  handleRowSelect,
}) => {
  // Ensure there is always at least one row
  const displayedTableData = tableData?.length > 0 ? tableData : [{}];

  return (
    <div>
      <table className="w-full table-condensed border border-gray-200 border-collapse text-xs text-center">
        <thead className="rounded-t-md bg-gray-200">
          <tr>
            <th>
              <input
                type="checkbox"
                checked={selectAll}
                onChange={handleSelectAll}
                className="form-checkbox"
              />
            </th>
            {/* <th>No</th> */}
            <th>ID</th>
            {columnsData.map((column) => (
              <th key={column.fieldname} className="px-2">
                {column.label}
              </th>
            ))}
            <th hidden={readOnly}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {displayedTableData.map((row, rowIndex) => (
            <TableRow
              key={rowIndex}
              rowIndex={rowIndex}
              row={row}
              columnsData={columnsData}
              selectedRows={selectedRows}
              handleCellChange={handleCellChange}
              handleDeleteRow={handleDeleteRow}
              handleDuplicateRow={handleDuplicateRow}
              handleRowEdit={handleRowEdit}
              readOnly={readOnly}
              preview={preview}
              getFieldDetails={getFieldDetails}
              configData={configData}
              handleRowSelect={handleRowSelect}
            />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
