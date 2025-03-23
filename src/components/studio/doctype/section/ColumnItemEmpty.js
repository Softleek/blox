import React, { Suspense, useEffect, useRef, useState } from "react";
import { useDrag, useDrop } from "react-dnd";
import clsx from "clsx";
import DraggableItem from "../DraggableItem"; // Assuming lazy loading is used in DraggableItem
import CustomButton from "@/components/core/common/buttons/Custom"; // Assuming lazy loading for CustomButton
import { COLUMN_TYPE, ITEM_TYPE } from "../constants"; // Make sure ITEM_TYPE and COLUMN_TYPE are imported
import { useConfig } from "@/contexts/ConfigContext";
import {
  moveAfterField,
  moveColumn,
  moveGroupedItems,
  moveItem,
} from "../utils/move";
import { getFieldsAfterBreak } from "../utils/getFieldsAfterBreak";
import ColumnActions from "./ColumnActions";
import { getLastFieldname } from "../utils/getLastFieldname";
import { addFieldToConfig } from "../utils/addFieldToConfig";
import { getFirstFieldname } from "../utils/getFirstField";

const ColumnItemEmpty = ({ section, column, handleFocus, handleBlur }) => {
  const { selectedItem, localConfig, selectedTab, setLocalConfig } =
    useConfig();

  const ref = useRef(null);

  const [{ isDragging: isColumnDragging }, dragColumn] = useDrag(() => ({
    type: COLUMN_TYPE,
    item: { column, type: COLUMN_TYPE },
    collect: (monitor) => ({
      isDragging: monitor?.isDragging(),
    }),
  }));

  const [{ isOver, canDrop }, dropColumn] = useDrop(() => ({
    accept: [COLUMN_TYPE, ITEM_TYPE],
    hover: (draggedItem) => {
      const newConfig = moveAfterField(
        localConfig,
        draggedItem?.item?.fieldname,
        column?.fieldname || column?.prevField || section?.fieldname
      );

      setLocalConfig(newConfig);
    },
    drop: (draggedItem) => {
      const newConfig = moveAfterField(
        localConfig,
        draggedItem?.item?.fieldname,
        column?.fieldname || column?.prevField || section?.fieldname
      );

      setLocalConfig(newConfig);
    },
    collect: (monitor) => ({
      isOver: monitor?.isOver(),
      canDrop: monitor?.canDrop(),
    }),
  }));

  const handleColClick = (e) => {
    if (e?.stopPropagation) {
      e.stopPropagation();
    }
    handleFocus?.(column);
  };

  const handleAddField = async () => {
    const targetField =
      getLastFieldname?.(column) || column?.fieldname || column?.prevField;
    const newConfig = await addFieldToConfig?.(
      localConfig,
      targetField,
      "Data"
    );
    setLocalConfig?.({ ...newConfig });
  };

  dropColumn?.(dragColumn?.(ref));

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <div
        ref={ref}
        fieldname={column?.fieldname}
        sectionname={section?.fieldname}
        tabname={selectedTab?.fieldname}
        firstfield={column?.fields?.[0]?.fieldname}
        className={clsx("flex-1 bg-gray-100 p-2 rounded-md border-[1px]", {
          "border border-black": selectedItem === column,
          "border-dashed border-gray-500": selectedItem !== column,
          "opacity-50": isColumnDragging,
          "bg-green-200": isOver && canDrop,
        })}
        onClick={handleColClick}
        key={column?.fieldname}
      >
        <div className="flex flex-row w-full h-fit justify-between">
          <h5 className="text-md font-semibold p-2">{column?.label}</h5>
          {selectedItem === column && (
            <ColumnActions column={column} handleAddField={handleAddField} />
          )}
        </div>

        <Suspense fallback={<div>Loading...</div>}>
          <CustomButton
            text="Add field"
            className="-mt-2 ml-1 bg-white"
            onClick={handleAddField}
          />
        </Suspense>
      </div>
    </Suspense>
  );
};

export default ColumnItemEmpty;
