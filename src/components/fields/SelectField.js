const SelectField = ({
  value = "",
  onChange,
  readOnly,
  preview,
  hidden,
  options,
  placeholder,
}) => (
  <select
    value={preview ? "" : value || ""} // In preview mode, do not display any value
    readOnly={readOnly || preview} // Make input readOnly in both readOnly and preview mode
    disabled={readOnly || preview}
    onChange={onChange}
    placeholder={placeholder}
    hidden={hidden}
    className="px-1 w-full focus:outline-none focus:ring-0 focus:border-none"
  >
    {options.map((opt, idx) => (
      <option key={idx} value={opt}>
        {opt}
      </option>
    ))}
  </select>
);

export default SelectField;
