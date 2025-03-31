import React, { useState, useEffect } from "react";
import dynamic from "next/dynamic";
import { Eye, Pencil, ChevronDown, ChevronUp } from "lucide-react";

// Dynamic import for Monaco Editor (client-side only)
const MonacoEditor = dynamic(import("@monaco-editor/react"), { ssr: false });

const HtmlEditor = () => {
  const [code, setCode] = useState("<h1>No content</h1>");
  const [showPreview, setShowPreview] = useState(true);
  const [height, setHeight] = useState(200);

  const expand = () => setHeight((prev) => prev + 200);
  const collapse = () => setHeight((prev) => (prev > 200 ? prev - 200 : 200));

  // Apply custom theme when the component mounts
  useEffect(() => {
    if (typeof window !== "undefined" && window.monaco) {
      window.monaco.editor.defineTheme("pinkPurpleLight", {
        base: "vs",
        inherit: true,
        rules: [
          { token: "keyword", foreground: "c2185b" }, // Pink
          { token: "string", foreground: "7b1fa2" }, // Purple
          { token: "number", foreground: "673ab7" },
          { token: "comment", foreground: "9e9e9e", fontStyle: "italic" },
        ],
        colors: {
          "editor.lineHighlightBackground": "#fce4ec", // Soft highlight
          "editorCursor.foreground": "#880e4f", // Dark pink cursor
          "editor.selectionBackground": "#f8bbd0", // Selection color
          "editor.selectionHighlightBackground": "#f48fb1",
        },
      });
    }
  }, []);

  return (
    <div className="flex flex-col w-full px-2 py-4 bg-gray-50 text-gray-900">
      <div className="flex justify-between items-center mb-4">
        <div className="flex space-x-2">
          <button
            onClick={() => setShowPreview(false)}
            className={`flex items-center px-2 py-1 rounded-md text-xs transition ${
              !showPreview ? "bg-pink-200" : "hover:bg-pink-100"
            }`}
          >
            <Pencil className="w-4 h-4 mr-2" /> Edit
          </button>
          <button
            onClick={() => setShowPreview(true)}
            className={`flex items-center px-2 py-1 rounded-md text-xs transition ${
              showPreview ? "bg-pink-200" : "hover:bg-pink-100"
            }`}
          >
            <Eye className="w-4 h-4 mr-2" /> Preview
          </button>
        </div>
      </div>

      <div
        className="border rounded bg-white shadow-md "
        style={{ height: showPreview ? "auto" : `${height}px` }}
      >
        {!showPreview ? (
          <div className="h-full py-4">
            <MonacoEditor
              height={`${height}px`}
              defaultLanguage="html"
              theme="pinkPurpleLight" // Custom theme
              value={code}
              onChange={(value) => setCode(value)}
              options={{
                minimap: { enabled: false },
                fontSize: 12,
                smoothScrolling: true,
                scrollbar: {
                  vertical: "auto",
                  horizontal: "auto",
                  useShadows: false,
                },
                scrollBeyondLastLine: false,
                automaticLayout: true,
                wordWrap: "on",
              }}
            />
          </div>
        ) : (
          <div
            className="p-2 w-full text-left overflow-auto bg-gray-100 rounded border border-gray-300"
            dangerouslySetInnerHTML={{ __html: code }}
          />
        )}
      </div>

      <div className="flex space-x-2 mt-2">
        <button
          type="button"
          onClick={expand}
          className="p-1 rounded hover:bg-gray-100"
          title="Expand"
        >
          <ChevronDown size={16} className="text-blue-500" />
        </button>
        <button
          type="button"
          onClick={collapse}
          className="p-1 rounded hover:bg-gray-100"
          title="Collapse"
        >
          <ChevronUp size={16} className="text-red-500" />
        </button>
      </div>
    </div>
  );
};

export default HtmlEditor;
