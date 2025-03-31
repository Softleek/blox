import React, { useState, useEffect, useRef } from "react";
import dynamic from "next/dynamic";
import "react-quill/dist/quill.snow.css";
import { Pencil, Eye, ChevronDown, ChevronUp } from "lucide-react";

const ReactQuill = dynamic(
  async () => {
    const { default: RQ } = await import("react-quill");
    return function ReactQuillWrapper({ forwardedRef, ...props }) {
      return <RQ ref={forwardedRef} {...props} />;
    };
  },
  {
    ssr: false,
    loading: () => (
      <div className="w-full h-40 border rounded-md bg-gray-50 animate-pulse"></div>
    ),
  }
);

const TextEditorField = ({
  value = "",
  onChange,
  readOnly,
  hidden,
  placeholder = "Enter text here...",
}) => {
  const [editorValue, setEditorValue] = useState(value);
  const [mode, setMode] = useState("preview");
  const [height, setHeight] = useState(160);
  const quillRef = useRef(null);

  useEffect(() => {
    setEditorValue(value);
  }, [value]);

  const handleEditorChange = (content) => {
    setEditorValue(content);
    if (onChange) onChange(content);
  };

  const expand = () => setHeight((prev) => prev + 100);
  const collapse = () => setHeight((prev) => (prev > 160 ? prev - 100 : 160));

  const modules = {
    toolbar:
      mode === "edit"
        ? [
            [{ header: [1, 2, 3, false] }],
            ["bold", "italic", "underline", "strike"],
            [{ color: [] }, { background: [] }],
            [{ list: "ordered" }, { list: "bullet" }],
            ["link", "image"],
            ["clean"],
          ]
        : false,
    clipboard: { matchVisual: false },
  };

  return (
    <div className={`w-full p-2 ${hidden ? "hidden" : ""} overflow-hidden`}>
      <div className="flex space-x-2 mb-1 pb-1 overflow-auto">
        <button
          type="button"
          onClick={() => setMode("edit")}
          className={`flex items-center px-2 py-1 rounded-md text-xs ${
            mode === "edit" ? "bg-pink-200" : "hover:bg-pink-100"
          }`}
        >
          <Pencil className="w-3 h-3 mr-1" /> Edit
        </button>
        <button
          type="button"
          onClick={() => setMode("preview")}
          className={`flex items-center px-2 py-1 rounded-md text-xs ${
            mode === "preview" ? "bg-pink-200" : "hover:bg-pink-100"
          }`}
        >
          <Eye className="w-3 h-3 mr-1" /> Preview
        </button>
      </div>

      {mode === "edit" ? (
        <ReactQuill
          ref={quillRef}
          value={editorValue}
          onChange={handleEditorChange}
          readOnly={readOnly}
          theme="snow" // Always use snow theme to maintain styling
          placeholder={placeholder}
          modules={modules}
          className="w-full border-b bg-white overflow-hidden transition-all"
          style={{ height: `${height - 5}px` }}
        />
      ) : (
        <div
          className="ql-snow w-full text-xs border-y bg-white text-gray-800 overflow-auto transition-all"
          style={{ height: `${height - 5}px` }}
        >
          <div
            className="ql-editor"
            dangerouslySetInnerHTML={{
              __html:
                editorValue ||
                '<span class="text-gray-400">(No content)</span>',
            }}
          />
        </div>
      )}

      <div className="flex space-x-2 mt-2">
        <button
          type="button"
          onClick={expand}
          className="text-xs text-blue-500 hover:text-blue-700"
          aria-label="Expand editor"
        >
          <ChevronDown className="w-4 h-4" />
        </button>
        <button
          type="button"
          onClick={collapse}
          className="text-xs text-red-500 hover:text-red-700"
          aria-label="Collapse editor"
        >
          <ChevronUp className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export default React.memo(TextEditorField);
