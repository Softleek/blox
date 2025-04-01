import Select from "react-select";

const MultiSelectField = ({
  value = [],
  onChange,
  options,
  placeholder,
  readOnly,
}) => {
  // Convert string options to { label, value } format
  const formattedOptions = options?.map((opt) => ({ label: opt, value: opt }));

  // Convert selected values to the expected format for react-select
  const selectedValues = value?.map((val) => ({ label: val, value: val }));

  return (
    <div
      className={`relative flex flex-col w-full break-words rounded-md font-bold text-[14px] ${
        readOnly ? "cursor-not-allowed" : ""
      }`}
    >
      <Select
        isMulti
        options={formattedOptions}
        value={selectedValues}
        onChange={(selected) =>
          !readOnly && onChange(selected?.map((item) => item.value))
        }
        placeholder={placeholder || "Select options"}
        classNamePrefix="custom-select"
        isDisabled={readOnly}
      />
    </div>
  );
};

export default MultiSelectField;
