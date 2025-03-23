import ToastTemplates from "@/components/core/common/toast/ToastTemplates";

export const generateFieldnameFromLabel = (label) => {
  return label
    ?.toLowerCase()
    ?.replace(/[^a-z0-9\s]/g, "") // Remove non-alphanumeric characters
    ?.trim()
    ?.replace(/\s+/g, "_"); // Replace spaces with underscores
};

export const validateFieldnames = (fields) => {
  const fieldnames = new Set();

  for (const field of fields) {
    if (fieldnames.has(field?.fieldname)) {
      throw new Error(
        `Fieldname conflict detected: "${field?.fieldname}" is duplicated.`
      );
    }
    fieldnames.add(field?.fieldname);
  }
};

export const handleDocSave = (localConfig, form, handleSave) => {
  try {
    // Remove undefined keys from form
    const cleanForm = Object.fromEntries(
      Object.entries(form)?.filter(([_, value]) => value !== undefined)
    );

    // Merge all properties of localConfig with cleaned form, with form taking precedence
    const updatedConfig = {
      ...localConfig,
      ...cleanForm, // Override properties from cleaned form
    };

    // Ensure fields and field_order are arrays (or empty)
    updatedConfig.fields = Array.isArray(updatedConfig.fields)
      ? updatedConfig.fields
      : [];

    updatedConfig.field_order = Array.isArray(updatedConfig.field_order)
      ? updatedConfig.field_order
      : [];

    // Only process fields if we have any
    if (updatedConfig.fields.length > 0) {
      updatedConfig.fields = updatedConfig.fields.map((field) => {
        let updatedField = { ...field };

        // Check if the field exists in the form and has been changed
        const matchingField = cleanForm?.fields?.find(
          (f) => f?.fieldname === field?.fieldname
        );

        if (matchingField) {
          updatedField = { ...updatedField, ...matchingField };
        }

        // Handle new fields
        if (updatedField?.is_new && updatedField?.label) {
          const newFieldname = generateFieldnameFromLabel(updatedField.label);

          if (
            updatedConfig.fields.some(
              (existingField) =>
                existingField?.fieldname === newFieldname &&
                existingField !== updatedField
            )
          ) {
            throw new Error(
              `Fieldname conflict: "${newFieldname}" already exists. Please use a different label.`
            );
          }

          updatedField.fieldname = newFieldname;

          // Update field_order
          const fieldOrderIndex = updatedConfig?.field_order.indexOf(
            field?.fieldname
          );
          if (fieldOrderIndex !== -1) {
            updatedConfig.field_order[fieldOrderIndex] = newFieldname;
          }
        }

        delete updatedField?.is_new;
        delete updatedField?.prevField;

        return updatedField;
      });
    }

    // Handle field_order mapping (though you’re not mapping any changes here, so this may not be needed)
    updatedConfig.field_order = updatedConfig.field_order.map((fieldname) => {
      // This map currently has no effect since fieldnameMap is empty
      return fieldname;
    });

    // Validate fieldnames (optional safety)
    validateFieldnames(updatedConfig.fields);

    handleSave(updatedConfig);
  } catch (error) {
    console.error(error);
    ToastTemplates?.error(error?.message);
  }
};
