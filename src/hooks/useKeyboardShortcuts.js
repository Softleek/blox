// src/hooks/useKeyboardShortcuts.js (updated)
import { getShortcutAction } from "@/config/keyboardShortcutsConfig";
import * as buttonActions from "@/components/pages/form/actions";

export const useKeyboardShortcuts = (options) => {
  const { form, router, slug, handleSave, disabled = false } = options;

  const handleKeyDown = (e) => {
    if (disabled) return;
    if (
      ["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement.tagName)
    ) {
      return;
    }

    const action = getShortcutAction(e);
    if (!action) return;

    e.preventDefault();

    switch (action) {
      case "save":
        handleSave();
        break;
      case "print":
        buttonActions.handlePrint({ form, router });
        break;
      case "new":
        buttonActions.handleNew({ router, slug });
        break;
      case "duplicate":
        buttonActions.handleDuplicate({ form, router, slug });
        break;
      default:
        break;
    }
  };

  const setupShortcuts = () => {
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  };

  return {
    setupShortcuts,
  };
};
