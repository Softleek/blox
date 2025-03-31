import React, { createContext, useContext, useState } from "react";

const ModalContext = createContext();

export const useModal = () => useContext(ModalContext);

export const ModalProvider = ({ children }) => {
  const [modalState, setModalState] = useState({
    isOpen: false,
    title: "",
    message: "",
    onConfirm: null,
    confirmButtonStyles: "",
    showButtons: true,
    position: "top",
    className: "!pt-10",
  });

  const openModal = ({
    title,
    message,
    onConfirm,
    confirmButtonStyles = "",
    showButtons = true, // Default to true
    position,
    className = "!pt-10",
  }) => {
    setModalState({
      isOpen: true,
      title,
      message,
      onConfirm,
      confirmButtonStyles,
      showButtons,
      position,
      className,
    });
  };

  const closeModal = () => {
    setModalState({ ...modalState, isOpen: false });
  };

  return (
    <ModalContext.Provider value={{ modalState, openModal, closeModal }}>
      {children}
    </ModalContext.Provider>
  );
};
