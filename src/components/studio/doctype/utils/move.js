import { getFieldsAfterBreak } from "./getFieldsAfterBreak";

// Helper to extract field names
const getFieldName = (item) => {
  if (Array.isArray(item)) {
    return item?.[0]?.fieldname || item?.[0]?.id;
  }
  return item?.fieldname || item?.id || item;
};

// Generic move function
export const moveItem = (
  draggedItem,
  targetItem,
  localConfig,
  moveAfter = false
) => {
  const draggedFieldName = getFieldName(draggedItem);
  const targetFieldName = getFieldName(targetItem);

  const updatedFieldOrder = [...(localConfig?.field_order || [])];

  const draggedItemIndex = updatedFieldOrder.indexOf(draggedFieldName);
  const targetItemIndex = updatedFieldOrder.indexOf(targetFieldName);

  if (draggedItemIndex === -1 || targetItemIndex === -1) {
    // Remove dragged item if it exists to avoid duplicates
    if (draggedItemIndex !== -1) {
      updatedFieldOrder.splice(draggedItemIndex, 1);
    }
    // Append dragged item to end (even if it wasn't found before)
    updatedFieldOrder.push(draggedFieldName);
    return { ...localConfig, field_order: updatedFieldOrder };
  }

  // Normal reordering
  updatedFieldOrder.splice(draggedItemIndex, 1);

  const newTargetIndex = moveAfter
    ? targetItemIndex + 1
    : targetItemIndex > draggedItemIndex
    ? targetItemIndex - 1
    : targetItemIndex;

  updatedFieldOrder.splice(newTargetIndex, 0, draggedFieldName);
  return { ...localConfig, field_order: updatedFieldOrder };
};

// Move column items
export const moveColumn = (draggedItem, targetItem, localConfig) => {
  return moveGroupedItems(draggedItem, targetItem, localConfig, "Column");
};

// Move section items
export const moveSection = (draggedItem, targetItem, localConfig) => {
  return moveGroupedItems(draggedItem, targetItem, localConfig, "Section");
};

// Move tab items
export const moveTab = (draggedItem, targetItem, localConfig) => {
  return moveGroupedItems(draggedItem, targetItem, localConfig, "Tab");
};

// Helper to move fields after breaks (not used directly but kept for completeness)
const moveGroupedItems1 = (draggedItem, targetItem, localConfig, breakType) => {
  const draggedFieldName = getFieldName(draggedItem);
  const targetFieldName = getFieldName(targetItem);

  const updatedFieldOrder = [...(localConfig?.field_order || [])];
  const draggedItemIndex = updatedFieldOrder.indexOf(draggedFieldName);
  const targetItemIndex = updatedFieldOrder.indexOf(targetFieldName);

  if (draggedItemIndex === -1 || targetItemIndex === -1) {
    // Fallback: move dragged group to end
    const draggedItemsToMove = [
      draggedFieldName,
      ...getFieldsAfterBreak(localConfig, draggedFieldName, breakType),
    ];
    draggedItemsToMove.forEach((fieldname) => {
      const index = updatedFieldOrder.indexOf(fieldname);
      if (index !== -1) {
        updatedFieldOrder.splice(index, 1);
      }
    });
    updatedFieldOrder.push(...draggedItemsToMove);
    return { ...localConfig, field_order: updatedFieldOrder };
  }

  const draggedItemsToMove = [
    draggedFieldName,
    ...getFieldsAfterBreak(localConfig, draggedFieldName, breakType),
  ];

  draggedItemsToMove.forEach((fieldname) => {
    const index = updatedFieldOrder.indexOf(fieldname);
    if (index !== -1) {
      updatedFieldOrder.splice(index, 1);
    }
  });

  const insertIndex = updatedFieldOrder.indexOf(targetFieldName);
  if (insertIndex !== -1) {
    updatedFieldOrder.splice(insertIndex, 0, ...draggedItemsToMove);
  } else {
    updatedFieldOrder.push(...draggedItemsToMove);
  }

  return { ...localConfig, field_order: updatedFieldOrder };
};

// Function to move multiple fields relative to a target field
export const moveGroupedItems = (
  fieldsToMove,
  targetField,
  localConfig,
  moveAbove = true // Default to moving above the target field
) => {
  const fieldOrder = [...(localConfig?.field_order || [])];

  const fieldNamesToMove = fieldsToMove?.map(getFieldName) || [];
  const targetFieldName = getFieldName(targetField);

  // Filter out undefined/null values
  const validFieldsToMove = fieldNamesToMove.filter(Boolean);

  // Remove existing fields to avoid duplicates
  const updatedFieldOrder = fieldOrder.filter(
    (field) => !validFieldsToMove.includes(field)
  );

  const targetIndex = updatedFieldOrder.indexOf(targetFieldName);

  if (targetIndex === -1) {
    // Target not found, move fields to end
    updatedFieldOrder.push(...validFieldsToMove);
  } else {
    const insertionIndex = moveAbove ? targetIndex : targetIndex + 1;
    updatedFieldOrder.splice(insertionIndex, 0, ...validFieldsToMove);
  }

  return { ...localConfig, field_order: updatedFieldOrder };
};

// New Function: Move `newField` exactly after `oldField`
export const moveAfterField = (config, newFieldName, oldFieldName) => {
  try {
    const fieldOrder = [...(config?.field_order || [])];

    if (!newFieldName || !oldFieldName) return config;

    // Remove newField if it exists to avoid duplicates
    const cleanedFieldOrder = fieldOrder.filter(
      (field) => field !== newFieldName
    );

    const oldFieldIndex = cleanedFieldOrder.indexOf(oldFieldName);

    if (oldFieldIndex === -1) {
      // Old field not found, append new field to end
      cleanedFieldOrder.push(newFieldName);
    } else {
      // Insert new field after old field
      cleanedFieldOrder.splice(oldFieldIndex + 1, 0, newFieldName);
    }

    return { ...config, field_order: cleanedFieldOrder };
  } catch (error) {
    console.error("Error in moveAfterField:", error);
    return config;
  }
};

// New Function: Move `newField` exactly before `oldField`
export const moveBeforeField = (config, newFieldName, oldFieldName) => {
  try {
    const fieldOrder = [...(config?.field_order || [])];

    if (!newFieldName || !oldFieldName) return config;

    // Remove newField if it exists to avoid duplicates
    const cleanedFieldOrder = fieldOrder.filter(
      (field) => field !== newFieldName
    );

    const oldFieldIndex = cleanedFieldOrder.indexOf(oldFieldName);

    if (oldFieldIndex === -1) {
      // Old field not found, append new field to end
      cleanedFieldOrder.push(newFieldName);
    } else {
      // Insert new field before old field
      cleanedFieldOrder.splice(oldFieldIndex, 0, newFieldName);
    }

    return { ...config, field_order: cleanedFieldOrder };
  } catch (error) {
    console.error("Error in moveBeforeField:", error);
    return config;
  }
};

export const moveGroupfields = (
  config,
  firstFieldName,
  lastFieldName,
  targetFieldName,
  insertBefore = true
) => {
  try {
    const fieldOrder = [...(config?.field_order || [])];

    if (!firstFieldName || !lastFieldName || !targetFieldName) return config;

    const startIndex = fieldOrder.indexOf(firstFieldName);
    const endIndex = fieldOrder.indexOf(lastFieldName);
    const targetIndex = fieldOrder.indexOf(targetFieldName);

    if (startIndex === -1 || endIndex === -1 || targetIndex === -1)
      return config;

    const groupFields = fieldOrder.slice(startIndex, endIndex + 1);

    // Remove groupFields from fieldOrder
    const cleanedFieldOrder = fieldOrder.filter(
      (field) => !groupFields.includes(field)
    );

    // Determine new index for insertion
    const adjustedTargetIndex = insertBefore ? targetIndex : targetIndex + 1;

    // Insert group at the correct position
    cleanedFieldOrder.splice(adjustedTargetIndex, 0, ...groupFields);

    return { ...config, field_order: cleanedFieldOrder };
  } catch (error) {
    console.error("Error in moveGroupRelativeToTarget:", error);
    return config;
  }
};
