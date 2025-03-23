import React, { Suspense, useEffect, useRef, useState } from "react";
import { useDrag, useDrop } from "react-dnd";
import clsx from "clsx";
import DraggableItem from "../DraggableItem"; // Assuming lazy loading is used in DraggableItem
import CustomButton from "@/components/core/common/buttons/Custom"; // Assuming lazy loading for CustomButton
import { COLUMN_TYPE, ITEM_TYPE } from "../constants"; // Make sure ITEM_TYPE and COLUMN_TYPE are imported
import { useConfig } from "@/contexts/ConfigContext";
import {
  moveColumn,
  moveGroupedItems,
  moveGroupfields,
  moveItem,
} from "../utils/move";
import { getFieldsAfterBreak } from "../utils/getFieldsAfterBreak";
import ColumnActions from "./ColumnActions";
import { getLastFieldname } from "../utils/getLastFieldname";
import { addFieldToConfig } from "../utils/addFieldToConfig";
import { getFirstFieldname } from "../utils/getFirstField";

const ColumnItem = ({ section, column, handleFocus, handleBlur }) => {
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
    accept: [COLUMN_TYPE],
    hover: (draggedItem) => {
      handleDropAndHover(draggedItem);
    },
    drop: (draggedItem) => {
      handleDropAndHover(draggedItem);
    },
    collect: (monitor) => ({
      isOver: monitor?.isOver(),
      canDrop: monitor?.canDrop(),
    }),
  }));

  const handleDropAndHover = (draggedItem) => {
    if (!draggedItem?.column || !column) return;

    const draggedFieldName = draggedItem?.column?.fieldname;
    const lastDraggedFieldName = draggedItem?.column?.fields?.length
      ? draggedItem?.column?.fields[draggedItem?.column?.fields?.length - 1]
          ?.fieldname
      : draggedItem?.column?.fieldname;
    const targetFieldName = column?.fieldname;

    if (!draggedFieldName || draggedFieldName === targetFieldName) return;

    const fieldOrder = localConfig?.field_order || [];
    const draggedIndex = fieldOrder.indexOf(draggedFieldName);
    const targetIndex = fieldOrder.indexOf(targetFieldName);

    if (draggedIndex === -1 || targetIndex === -1) return;
    let newConfig;

    if (draggedIndex < targetIndex) {
      // Dragged item is above the target item; move it after
      newConfig = moveGroupfields(
        localConfig,
        draggedFieldName,
        lastDraggedFieldName,
        targetFieldName,
        false
      ); // true = moveAfter
    } else {
      // Dragged item is below or same level; default behavior
      newConfig = moveGroupfields(
        localConfig,
        draggedFieldName,
        lastDraggedFieldName,
        targetFieldName,
        true
      );
    }

    setLocalConfig(newConfig);
  };

  const handleColClick = (e) => {
    if (e?.stopPropagation) {
      e.stopPropagation();
    }
    handleFocus(column);
  };

  const handleAddField = async () => {
    const targetField =
      getLastFieldname(column) || column?.fieldname || column?.prevField;
    const newConfig = await addFieldToConfig(localConfig, targetField, "Data");
    setLocalConfig({ ...newConfig });
  };

  dropColumn(dragColumn(ref));

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

        {column?.fields?.map((item) => (
          <Suspense fallback={<div>Loading...</div>} key={item?.fieldname}>
            <DraggableItem
              item={item}
              handleFocus={handleFocus}
              handleBlur={handleBlur}
              itemType={COLUMN_TYPE}
            />
          </Suspense>
        ))}

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

export default ColumnItem;
