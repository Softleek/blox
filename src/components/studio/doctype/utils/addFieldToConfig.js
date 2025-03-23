// Utility function to generate a unique fieldname based on a prefix
export const generateUniqueName = (prefix, items) => {
  const generateRandomSuffix = () => Math.random().toString(36).substring(2, 6);
  let suffix = generateRandomSuffix();
  while (items?.some((item) => item?.fieldname === `${prefix}_${suffix}`)) {
    suffix = generateRandomSuffix();
  }
  return `${prefix}_${suffix}`;
};

// Utility function to generate the next numerical label for tabs
const generateNextLabel = (prefix, items) => {
  const existingNumbers = items
    ?.filter(
      (item) =>
        item?.fieldtype === "Tab Break" && item?.label?.startsWith(prefix)
    )
    ?.map((item) => parseInt(item?.label?.replace(/\D+/g, ""), 10))
    ?.filter(Number.isFinite);

  const nextNumber =
    existingNumbers?.length > 0 ? Math.max(...existingNumbers) + 1 : 1;
  return `${prefix} ${nextNumber}`;
};

export const addFieldToConfig = (
  config,
  after_field,
  fieldType,
  addBefore = false
) => {
  if (!config) {
    console.error("addFieldToConfig: 'config' is null or undefined.");
    return null; // or handle the fallback
  }

  const fieldname = generateUniqueName(fieldType.toLowerCase(), config?.fields);
  let newField;

  if (fieldType === "Tab") {
    const label = generateNextLabel("Tab", config?.fields);
    newField = {
      fieldname,
      label,
      fieldtype: "Tab Break",
      is_new: true,
    };
  } else if (fieldType === "Section") {
    newField = {
      fieldname,
      fieldtype: "Section Break",
      is_new: true,
    };
  } else if (fieldType === "Column") {
    newField = {
      fieldname,
      fieldtype: "Column Break",
      is_new: true,
    };
  } else {
    newField = {
      fieldname,
      fieldtype: fieldType,
      is_new: true,
    };
  }

  config.fields = config.fields || [];
  config.fields.push(newField);

  config.field_order = config.field_order || [];

  const index = config.field_order.indexOf(after_field);
  if (index !== -1) {
    const insertIndex = addBefore ? index : index + 1;
    config.field_order.splice(insertIndex, 0, fieldname);
  } else {
    config.field_order.push(fieldname);
  }

  return config;
};
