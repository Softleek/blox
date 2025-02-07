import React from "react";
import {
  faCashRegister,
  faShoppingCart,
  faBox,
  faFileInvoice,
  faUsers,
  faTruck,
  faWarehouse,
  faClipboardList,
} from "@fortawesome/free-solid-svg-icons";
import LinkSection from "@/components/workspace/LinkSection";

const POSDashboard = () => {
  // POS Modules with categorized links
  const posSections = [
    {
      title: "Sales",
      description: "Manage customer transactions and invoices",
      links: [
        { href: "/sale", icon: faUsers, text: "New Sale" },
        {
          href: "/app/sales_invoice",
          icon: faCashRegister,
          text: "Sales Invoice",
        },
        { href: "/app/customer", icon: faUsers, text: "Customers" },
        { href: "/app/payment", icon: faCashRegister, text: "Payments" },
        {
          href: "/app/payment_method",
          icon: faClipboardList,
          text: "Payment Methods",
        },
        { href: "/app/commission", icon: faCashRegister, text: "Commissions" },
      ],
    },
    {
      title: "Inventory",
      description: "Manage stock, items, and warehouse operations",
      links: [
        { href: "/app/item", icon: faBox, text: "Items" },
        { href: "/app/item_group", icon: faBox, text: "Item Groups" },
        {
          href: "/app/stock_entry",
          icon: faClipboardList,
          text: "Stock Entry",
        },
        {
          href: "/app/stock_reconciliation",
          icon: faClipboardList,
          text: "Stock Reconciliation",
        },
        { href: "/app/stock_transfer", icon: faTruck, text: "Stock Transfer" },
        { href: "/app/stock_uom", icon: faClipboardList, text: "Stock UOM" },
      ],
    },
    {
      title: "Purchases",
      description: "Manage supplier transactions and expenses",
      links: [
        {
          href: "/app/purchase_invoice",
          icon: faShoppingCart,
          text: "Purchase Invoice",
        },
        { href: "/app/supplier", icon: faTruck, text: "Suppliers" },
        { href: "/app/expense", icon: faCashRegister, text: "Expenses" },
      ],
    },
  ];

  return (
    <div className="flex flex-col space-y-6 w-full px-6">
      {/* Page Header */}
      <div className="mt-4">
        <h2 className="text-2xl font-semibold">Point of Sale (POS)</h2>
        <p className="text-gray-600">
          Quick access to sales, inventory, and purchase operations.
        </p>
      </div>

      {/* POS Sections */}
      {posSections.map((section, index) => (
        <LinkSection
          key={index}
          title={section.title}
          description={section.description}
          links={section.links}
          bgColor="bg-gray-100"
          textColor="text-gray-900"
          className="rounded-lg p-4 shadow-sm bg-white"
          cols={6}
        />
      ))}
    </div>
  );
};

export default POSDashboard;
