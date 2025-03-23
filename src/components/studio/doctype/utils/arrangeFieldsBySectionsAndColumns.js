export const arrangeFieldsIntoSectionsAndColumns = (
  fields,
  tabBreak = null
) => {
  const generateRandomId = (prefix) =>
    `${prefix}_${Math.random().toString(36).substring(2, 8)}`;

  const sections = [];
  let currentSection = null;
  let currentColumn = null;
  let prevField = tabBreak?.fieldname;

  const createDefaultSection = () => {
    const sectionId = generateRandomId("section");
    return {
      label: "",
      fieldname: "",
      id: sectionId,
      prevField,
      fieldtype: "Section Break",
      columns: [],
    };
  };

  const createDefaultColumn = () => {
    return {
      label: "",
      fieldname: "",
      id: generateRandomId("column"),
      prevField: currentSection?.id,
      fieldtype: "Column Break",
      fields: [],
    };
  };

  if (!fields || fields.length === 0) {
    const defaultSection = createDefaultSection();
    defaultSection.columns.push(createDefaultColumn());
    return [defaultSection];
  }

  currentSection = createDefaultSection();
  sections.push(currentSection);

  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];

    switch (field.fieldtype) {
      case "Section Break":
        currentSection = {
          ...field,
          prevField,
          columns: [],
        };
        sections.push(currentSection);
        currentColumn = null;

        const nextField = fields[i + 1];
        if (!nextField || nextField.fieldtype !== "Column Break") {
          currentColumn = createDefaultColumn();
          currentSection.columns.push(currentColumn);
        }
        break;

      case "Column Break":
        currentColumn = {
          ...field,
          prevField,
          fields: [],
        };
        currentSection.columns.push(currentColumn);
        break;

      default:
        if (!currentColumn) {
          currentColumn = createDefaultColumn();
          currentSection.columns.push(currentColumn);
        }

        currentColumn.fields.push({
          ...field,
          prevField,
          fieldname: field.fieldname || generateRandomId("field"),
        });
        break;
    }

    prevField = field.fieldname;
  }

  return sections;
};
