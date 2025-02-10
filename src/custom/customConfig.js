import { executeAction } from "@/utils/customActions";

// Sample lifecycle hooks
export const lifecycleHooks = {
  beforeSave: (form) => {
    console.log("Before Save Hook Executed");
    // return cleanData(form);
  },
  afterSave: (form) => {
    console.log("After Save Hook Executed");
  },
  onFieldChange: (field, value, setForm) => {
    console.log(`Field Changed: ${field} => ${value}`);
    // setForm((prev) => ({ ...prev, [field]: value }));
  },
};

// Sample custom buttons
export const customButtons = [
  {
    label: "Custom Action",
    type: "primary",
    text: "⚡",
    action: (props) => console.log("After Save Hook Executed"),
  },
  {
    label: "Refresh",
    text: "🔄",
    // action: (props) => reloadData(props.router),
  },
];

// Sample custom components
export const customComponents = [
  ({ form }) => (
    <div className="bg-blue-100 p-2 rounded-md">
      <p>Custom Component Loaded</p>
      <p>Form Data: {JSON.stringify(form, null, 2)}</p>
    </div>
  ),
];
