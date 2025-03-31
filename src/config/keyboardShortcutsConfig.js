export const keyboardShortcuts = [
  {
    keys: ["ctrl+s", "cmd+s"],
    action: "save",
    description: "Save the current document",
  },
  {
    keys: ["ctrl+p", "cmd+p"],
    action: "print",
    description: "Print the current document",
  },
  {
    keys: ["ctrl+n", "cmd+n"],
    action: "new",
    description: "Create new document",
  },
  {
    keys: ["ctrl+d", "cmd+d"],
    action: "duplicate",
    description: "Duplicate current document",
  },
];

export const getShortcutAction = (e) => {
  const key = e.key.toLowerCase();
  const ctrlOrCmd = e.ctrlKey || e.metaKey;

  if (!ctrlOrCmd) return null;

  switch (key) {
    case "s":
      return "save";
    case "p":
      return "print";
    case "n":
      return "new";
    case "d":
      return "duplicate";
    default:
      return null;
  }
};
