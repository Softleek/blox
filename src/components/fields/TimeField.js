import React, { useState } from "react";
import CustomTimePicker from "./time";
import "react-datepicker/dist/react-datepicker.css";

const TimeField = ({ value = "", onChange, readOnly, hidden }) => {
  return (
    <div
      className={`w-full flex flex-row items-center justify-between ${
        readOnly ? "cursor-not-allowed" : ""
      }`}
    >
      <CustomTimePicker value={value} onChange={onChange} />
    </div>
  );
};

export default TimeField;
