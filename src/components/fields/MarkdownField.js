import React, { useState, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import rehypeRaw from "rehype-raw";
import rehypeSanitize from "rehype-sanitize";
import rehypeHighlight from "rehype-highlight";
import rehypeKatex from "rehype-katex";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import { ChevronDown, ChevronUp, Eye, Pencil } from "lucide-react";
import "highlight.js/styles/github.css";
import "katex/dist/katex.min.css";

const MarkdownEditorField = ({
  value = "",
  onChange,
  readOnly,
  hidden,
  placeholder = "Enter Markdown content...",
}) => {
  const [editorValue, setEditorValue] = useState(value);
  const [rows, setRows] = useState(8);
  const [showPreview, setShowPreview] = useState(true);

  useEffect(() => {
    setEditorValue(value);
  }, [value]);

  const handleChange = (e) => {
    setEditorValue(e.target.value);
    if (onChange) onChange(e.target.value);
  };

  const expand = () => setRows((prev) => prev + 4);
  const collapse = () => setRows((prev) => (prev > 4 ? prev - 4 : 4));

  if (hidden) return null;

  return (
    <div className="flex flex-col space-y-2 w-full p-2 bg-white">
      <div className="flex justify-between items-center">
        <div className="flex space-x-2 mb-1 pb-1 overflow-auto">
          <button
            type="button"
            onClick={() => setShowPreview(false)}
            className={`flex items-center px-2 py-1 rounded-md text-xs ${
              !showPreview ? "bg-pink-200" : "hover:bg-pink-100"
            }`}
          >
            <Pencil className="w-3 h-3 mr-1" /> Edit
          </button>
          <button
            type="button"
            onClick={() => setShowPreview(true)}
            className={`flex items-center px-2 py-1 rounded-md text-xs ${
              showPreview ? "bg-pink-200" : "hover:bg-pink-100"
            }`}
          >
            <Eye className="w-3 h-3 mr-1" /> Preview
          </button>
        </div>
      </div>

      {!showPreview ? (
        <textarea
          value={editorValue}
          readOnly={readOnly}
          disabled={readOnly}
          onChange={handleChange}
          rows={rows}
          className={`p-2 text-xs text-gray-900 w-full border border-gray-200 rounded !font-medium outline-none ${
            readOnly ? "cursor-not-allowed" : ""
          }`}
          placeholder={placeholder}
        />
      ) : (
        <div className="prose prose-sm max-w-none w-full text-left p-2 border border-gray-200 rounded bg-gray-50 min-h-[100px] overflow-auto">
          <ReactMarkdown
            rehypePlugins={[
              rehypeRaw,
              rehypeSanitize,
              rehypeHighlight,
              rehypeKatex,
            ]}
            remarkPlugins={[remarkGfm, remarkMath]}
            components={{
              code({ node, inline, className, children, ...props }) {
                const match = /language-(\w+)/.exec(className || "");
                return !inline && match ? (
                  <div className="bg-gray-100 rounded p-2 overflow-x-auto">
                    <code className={className} {...props}>
                      {children}
                    </code>
                  </div>
                ) : (
                  <code className="bg-gray-100 px-1 py-1 rounded text-xs">
                    {children}
                  </code>
                );
              },
            }}
          >
            {editorValue || "*Nothing to preview*"}
          </ReactMarkdown>
        </div>
      )}
      <div className="flex space-x-2">
        {!readOnly && (
          <>
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
          </>
        )}
      </div>
    </div>
  );
};

export default MarkdownEditorField;
