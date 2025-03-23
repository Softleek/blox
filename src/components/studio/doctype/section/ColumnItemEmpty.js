import React, { Suspense, useEffect, useRef, useState } from "react";
import { useDrag, useDrop } from "react-dnd";
import clsx from "clsx";
import DraggableItem from "../DraggableItem"; // Assuming lazy loading is used in DraggableItem
import CustomButton from "@/components/core/common/buttons/Custom"; // Assuming lazy loading for CustomButton
import { COLUMN_TYPE, ITEM_TYPE } from "../constants"; // Make sure ITEM_TYPE and COLUMN_TYPE are imported
import { useConfig } from "@/contexts/ConfigContext";
import { moveColumn, moveGroupedItems, moveItem } from "../utils/move";
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
    drop: (item, monitor) => {
      handleDrop(item, monitor);
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

  const getDropType = (current) => {
    const attributeUsed = current?.getAttribute("fieldname")
      ? "fieldname"
      : current?.getAttribute("firstfield")
      ? "firstfield"
      : current?.getAttribute("sectionname")
      ? "sectionname"
      : current?.getAttribute("tabname")
      ? "tabname"
      : "other";

    const moveAbove =
      attributeUsed === "sectionname" || attributeUsed === "tabname"
        ? false
        : true;

    return { moveAbove, attributeUsed };
  };

  const handleDrop = (item, monitor) => {
    const current = ref?.current;
    const targetField =
      current?.getAttribute("fieldname") ||
      current?.getAttribute("sectionname") ||
      current?.getAttribute("firstfield") ||
      current?.getAttribute("tabname");

    const { moveAbove, attributeUsed } = getDropType?.(ref?.current);

    if (item?.type === COLUMN_TYPE) {
      const firstfield = getFirstFieldname?.(item?.column);
      const targetRect = ref?.current?.getBoundingClientRect();
      const clientOffset = monitor?.getClientOffset();

      const dropPercentage =
        ((clientOffset?.x - targetRect?.left) / targetRect?.width) * 100;

      const dropSide = dropPercentage <= 50 ? "left" : "right";
      const targetFields = getFieldsAfterBreak?.(
        localConfig,
        targetField,
        "Column",
        true
      );
      const specificTargetField = targetFields?.[targetFields?.length - 1];

      const droppedFields = getFieldsAfterBreak?.(
        localConfig,
        firstfield,
        "Column",
        true
      );

      const newConfig = moveGroupedItems?.(
        droppedFields,
        specificTargetField,
        localConfig,
        false
      );

      setLocalConfig?.(newConfig);
    } else {
      const newConfig = moveItem?.(
        item?.id,
        targetField,
        localConfig,
        moveAbove
      );
      setLocalConfig?.(newConfig);
    }
  };

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
