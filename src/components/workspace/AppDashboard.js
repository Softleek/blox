import React from "react";
import {
  faBox,
  faFileInvoice,
  faEdit,
  faCogs,
} from "@fortawesome/free-solid-svg-icons";
import LinkSection from "@/components/workspace/LinkSection";
import LinkCard from "@/components/workspace/LinkCard";
import { useRouter } from "next/router";
import {
  getDocsByModuleOrApp,
  getModulesByApp,
} from "../../utils/generateSidebarData";
import PrimaryButton from "../core/common/buttons/Primary";

const AppDashboard = () => {
  const router = useRouter();
  const { id } = router.query; // Get the app ID from the URL (e.g., /[id])

  // Retrieve modules for the current app using the app ID
  const appModules = id ? getModulesByApp(id) : [];

  const generateDocLinks = (docList) => {
    return docList.map((doc) => ({
      href: `${doc.link}`, // Generate link using doc ID
      icon: faFileInvoice,
      text: `${doc.name}`, // Display name from doc object
    }));
  };

  // Handle navigation to customize or edit the current path
  const handleNavigate = (type) => {
    router.push(`${router.asPath}${type}`); // Append '/edit' or '/customize' to current path
  };

  return (
    <div className="flex flex-col space-y-6">
      {/* Buttons Section */}
      <div className="flex justify-end space-x-4 px-6 mt-4">
        <PrimaryButton text={"Edit"} onClick={() => handleNavigate("/edit")} />
        <PrimaryButton
          text={"Customize"}
          onClick={() => handleNavigate("/customize")}
        />
      </div>

      {/* Module Section */}
      <div className="w-full px-6">
        <h2 className="text-xl font-semibold mb-4">Modules</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-3">
          {appModules.map((module) => (
            <LinkCard
              key={module.id}
              title={module.name} // Display the module name
              icon={faBox}
              href={module.link} // Use module.link to generate the correct URL
              iconBg="bg-gradient-to-tl from-green-400 to-blue-500"
              tooltipContent={`Manage ${module.name}`}
              className="text-slate-800 text-base"
            />
          ))}
        </div>
      </div>

      {/* Document Section */}
      <div className="w-full px-6">
        <h2 className="text-xl font-semibold mb-4">Documents</h2>
        {appModules.map((module) => {
          const coreDocs = getDocsByModuleOrApp(id, module.id) || [];

          return (
            <div key={module.id} className="mb-8">
              <h3 className="text-lg font-medium mb-2">
                {module.name} Documents
              </h3>
              <LinkSection
                title={`Manage ${module.name} Documents`}
                description={`Access and manage all documents related to ${module.name}.`}
                links={generateDocLinks(coreDocs)} // Use module.id to build links
                bgColor="bg-gray-100"
                textColor="text-gray-900"
                className="rounded-lg p-4 shadow-sm bg-white"
                cols={6}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default AppDashboard;
