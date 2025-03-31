/**
 * Evaluates a depends_on condition against form data
 * @param {string} dependsOn - The condition to evaluate
 * @param {object} form - The form data to evaluate against
 * @returns {boolean} - Whether the condition is met
 */
export const evaluateDependsOn = (dependsOn, form) => {
  try {
    if (!form) return true;

    // Handle simple field conditions (fieldname==value or fieldname!=value)
    const simpleConditionMatch = dependsOn.match(
      /^\s*(\w+)\s*(!=|==)\s*(['"]?)(.*?)\3\s*$/
    );
    if (simpleConditionMatch) {
      const [, key, operator, , value] = simpleConditionMatch;
      const formValue = form[key.trim()];

      if (operator === "!=") {
        return formValue !== value;
      } else if (operator === "==") {
        return formValue === value;
      }
      return true;
    }

    // Handle eval conditions
    if (dependsOn.trim().startsWith("eval:")) {
      const evalExpression = dependsOn.replace(/^eval:/, "").trim();
      return evaluateEvalExpression(evalExpression, form);
    }

    // Handle direct field name (truthy check)
    if (/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(dependsOn.trim())) {
      return !!form[dependsOn.trim()];
    }

    console.warn("Unsupported depends_on condition format:", dependsOn);
    return true;
  } catch (error) {
    console.error("Error evaluating depends_on condition:", error);
    return true;
  }
};

/**
 * Safely evaluates a JavaScript expression in the context of form data
 * @param {string} expression - The JavaScript expression to evaluate
 * @param {object} form - The form data to provide as context
 * @returns {boolean} - The result of the evaluation
 */
export const evaluateEvalExpression = (expression, form) => {
  try {
    // Create a safe context for evaluation
    const context = {
      doc: form,
      data: form,
      // Add helper functions if needed
      _: (value) => value, // placeholder for potential helper functions
    };

    // Replace doc. with context.doc. for safety
    const safeExpression = expression
      .replace(/\b(doc\.)/g, "context.doc.")
      .replace(/\b(data\.)/g, "context.data.");

    // Create function with the expression
    const func = new Function(
      "context",
      `try { return ${safeExpression}; } catch(e) { console.error("Eval error:", e); return false; }`
    );

    return !!func(context);
  } catch (error) {
    console.error("Error evaluating expression:", error);
    return false;
  }
};
