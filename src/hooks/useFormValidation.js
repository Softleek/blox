// src/hooks/useFormValidation.js
import { useModal } from "@/contexts/ModalContext";
import PropTypes from "prop-types";
import { AlertOctagon, List, X } from "lucide-react";
import { motion } from "framer-motion";

/**
 * @typedef {Object} FieldConfig
 * @property {string} [label] - Display label for the field
 * @property {boolean|number} [required] - Whether the field is required
 * @property {function} [validator] - Custom validation function
 */

/**
 * @typedef {Object} ValidationConfig
 * @property {Object.<string, FieldConfig>} fields - Field configurations
 * @property {string[]} [requiredFields] - List of required field names
 */

/**
 * @typedef {Object} ValidationError
 * @property {string} field - Name of the invalid field
 * @property {string} message - Error message to display
 */

/**
 * @typedef {Object} ValidationResult
 * @property {boolean} isValid - Overall validation status
 * @property {ValidationError[]} errors - Array of validation errors
 */

export const useFormValidation = () => {
  const { openModal, closeModal } = useModal();

  /**
   * Validates form data against the provided configuration
   * @param {Object} form - Form data object
   * @param {ValidationConfig} config - Validation configuration
   * @returns {ValidationResult} Validation result object
   */
  const validateForm = (form, config) => {
    if (!config?.fields) {
      return { isValid: true, errors: [] };
    }

    const errors = [];

    // Get all required fields from both sources
    const requiredFields = getRequiredFields(config);
    console.log("Required Fields:", requiredFields);

    // Validate required fields
    requiredFields.forEach((field) => {
      const fieldConfig = config.fields[field];
      const error = validateRequiredField(field, form[field], fieldConfig);
      if (error) errors.push(error);
    });

    // Run custom validators
    Object.entries(config.fields).forEach(([field, fieldConfig]) => {
      if (fieldConfig.validator) {
        const error = fieldConfig.validator(form[field], form);
        if (error) errors.push({ field, message: error });
      }
    });

    return {
      isValid: errors.length === 0,
      errors,
    };
  };

  /**
   * Gets all required fields from config
   * @param {ValidationConfig} config
   * @returns {string[]} Array of required field names
   */
  const getRequiredFields = (config) => {
    if (!config?.fields) return [];

    return [
      ...new Set([
        ...(config.requiredFields || []), // From requiredFields array
        ...Object.values(config.fields)
          .filter(
            ({ reqd, bold, mandatory }) =>
              reqd === 1 || reqd === true || bold === 1 || mandatory === 1
          )
          .map((field) => field.fieldname), // Use fieldname property
      ]),
    ];
  };

  /**
   * Validates a single required field
   * @param {string} field - Field name
   * @param {any} value - Field value
   * @param {FieldConfig} [config] - Field configuration
   * @returns {ValidationError|null} Validation error or null if valid
   */
  const validateRequiredField = (field, value, config) => {
    if (value === undefined || value === null) {
      return createFieldError(field, config);
    }

    if (typeof value === "string" && value.trim() === "") {
      return createFieldError(field, config);
    }

    if (Array.isArray(value) && value.length === 0) {
      return createFieldError(field, config);
    }

    if (typeof value === "object" && Object.keys(value).length === 0) {
      return createFieldError(field, config);
    }

    return null;
  };

  /**
   * Creates a validation error object
   * @param {string} field
   * @param {FieldConfig} [config]
   * @returns {ValidationError}
   */
  const createFieldError = (field, config) => ({
    field,
    message: `${config?.label || field} `,
  });

  /**
   * Displays validation errors in a modal dialog
   * @param {ValidationError[]} errors - Array of validation errors
   */

  const showValidationErrors = (errors) => {
    openModal({
      showButtons: false,
      className: "!pt-10",
      position: "top",
      message: (
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
          className="relative w-full bg-white shadow-lg rounded-lg overflow-hidden"
        >
          {/* Close Button */}
          <button
            onClick={closeModal}
            className="absolute top-2 right-2 text-red-700 bg-white hover:bg-red-500 font-bold p-1 rounded-full transition"
          >
            <X className="w-5 h-5" />
          </button>

          {/* Header with Icon */}
          <div className="flex items-center bg-red-600 text-white text-lg font-semibold px-4 py-3">
            <AlertOctagon className="w-6 h-6 mr-2 text-red-200 animate-pulse" />
            Validation Error
          </div>

          {/* Body */}
          <div className="p-5 space-y-4">
            <p className="text-gray-700 text-base font-medium">
              The following fields are mandatory:
            </p>

            {/* Enhanced List with subtle hover effect */}
            <ul className="space-y-2">
              {errors.map((error, index) => (
                <motion.li
                  key={index}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.3, delay: index * 0.1 }}
                  className="flex items-center bg-red-50 border-l-4 border-red-500 p-2 rounded-md shadow-sm hover:bg-red-100 transition"
                >
                  <List className="w-3 h-3 text-red-600 mr-3" />
                  <span className="text-red-900 font-medium text-xs">
                    {error.message}
                  </span>
                </motion.li>
              ))}
            </ul>
          </div>
        </motion.div>
      ),
    });
  };

  return {
    validateForm,
    validateRequiredFields: validateForm, // Legacy alias
    showValidationErrors,
    getRequiredFields,
  };
};

// PropTypes for documentation and development
useFormValidation.propTypes = {
  validateForm: PropTypes.func.isRequired,
  showValidationErrors: PropTypes.func.isRequired,
  getRequiredFields: PropTypes.func.isRequired,
};
