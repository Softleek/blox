import React, { useRef, useEffect, useState } from "react";
import Documentation from "@/components/core/common/sidebar/Documentation";
import SidebarList from "@/components/core/common/sidebar/List";
import {
  faDashboard,
  faUser,
  faAngleDoubleLeft,
  faAngleDoubleRight,
  faUserFriends,
  faCogs,
  faDiagnoses,
  faBook,
  faBookOpen,
  faTools,
  faBars,
  faCashRegister,
  faFileInvoice,
  faBox,
  faChartBar,
  faTruckPickup,
  faTruckLoading,
  faDriversLicense,
  faCar,
  faCartShopping,
  faPerson,
  faQuoteLeft,
  faMoneyBillTransfer,
  faBell,
  faSailboat,
  faUserGroup,
  faUserCheck,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useSidebar } from "@/contexts/SidebarContext";
import { useNavbar } from "@/contexts/NavbarContext";
import { useRouter } from "next/router";
import sidebarConfig from "@/data/sidebar.json"; // Import sidebar.json for sidebar settings

const Sidebar = () => {
  const { sidebarWidth, setSidebarWidth, sidebarHidden } = useSidebar();
  const { dashboardText } = useNavbar();
  const sidebarRef = useRef(null);
  const [isCollapsed, setIsCollapsed] = useState(false);
  const router = useRouter();

  // Extract sidebar links from sidebarConfig
  const sidebarLinks = sidebarConfig.sidebarLinks || []; // Assuming the sidebar.json has a links array

  useEffect(() => {
    const handleResize = () => {
      if (sidebarHidden) {
        setIsCollapsed(true);
      } else {
        if (sidebarRef.current) {
          setIsCollapsed(window.innerWidth < 1150);
        }
      }
    };

    handleResize();

    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, [router, sidebarHidden]);

  useEffect(() => {
    if (sidebarRef.current) {
      setSidebarWidth(sidebarRef.current.offsetWidth);
    }
  }, [isCollapsed, sidebarHidden]);

  const toggleSidebar = () => {
    setIsCollapsed(!isCollapsed);
  };

  return (
    <aside
      className={`${
        !sidebarHidden ? "" : "hidden"
      } w-fit relative flex flex-col`}
      ref={sidebarRef}
    >
      {isCollapsed && (
        <button
          onClick={toggleSidebar}
          className="w-fit fixed z-100 text-slate-700 py-2 px-2 group text-sm md:text-xl top-16 bg-gray-50 rounded" // Use group class for managing hover effect
        >
          {/* Default icon (faBars) */}
          <FontAwesomeIcon
            icon={faBars}
            className="transition-all duration-300 ease-in-out group-hover:hidden" // Hide on hover
          />
          {/* Hover icon (faAngleDoubleRight) */}
          <FontAwesomeIcon
            icon={faAngleDoubleLeft}
            className="transition-all duration-300 ease-in-out hidden group-hover:block" // Show on hover
          />
        </button>
      )}

      <div
        className={`w-fit max-h-[92vh] overflow-auto ease-nav-brand block -translate-x-full flex-wrap flex-grow items-center justify-between border-0 p-1 antialiased transition-transform duration-200 left-0 translate-x-0 ${
          !isCollapsed ? "" : "hidden"
        }`}
      >
        <div className="h-fit flex items-center justify-between px-4">
          <button
            onClick={toggleSidebar}
            className="group text-sm md:text-xl flex py-2" // Use group class for managing hover effect
          >
            {/* Default icon (faBars) */}
            <FontAwesomeIcon
              icon={faBars}
              className="transition-all duration-300 ease-in-out group-hover:hidden" // Hide on hover
            />
            {/* Hover icon (faAngleDoubleRight) */}
            <FontAwesomeIcon
              icon={faAngleDoubleRight}
              className="transition-all duration-300 ease-in-out hidden group-hover:block" // Show on hover
            />
          </button>
          <a
            className="block py-2 m-0 text-sm flex flex-col whitespace-nowrap justify-center items-center text-slate-700"
            target="_blank"
            rel="noreferrer"
            href="/"
          >
            <span className="ml-4 mr-2 font-semibold text-xl transition-all duration-200 ease-nav-brand">
              {dashboardText}
            </span>
          </a>
        </div>

        <hr className="h-px mt-0 bg-transparent bg-gradient-to-r from-transparent via-black/40 to-transparent" />

        <div className="items-center block w-auto h-fit grow basis-full scrollbar scrollbar-thin scrollbar-thumb-slate-50 scrollbar-track-slate-100 pr-2">
          <ul className="flex flex-col mb-4">
            <SidebarList
              icon={faDashboard}
              text="Home"
              link="/"
              active={dashboardText === "Home"}
            />
            <SidebarList
              icon={faBell}
              text="Reminder"
              link="/app/reminder"
              permission="view_reminder"
              active={dashboardText === "Reminder"}
            />

            {/* Dynamically add links from sidebar.json */}
            {sidebarLinks.map((link) => (
              <SidebarList
                key={link.text} // Use text as key or any unique identifier
                icon={link.icon} // Adjust the icon or load dynamically from sidebar.json
                text={link?.text}
                link={link?.link}
              />
            ))}

            <li className="w-full mb-2 mt-6 pr-2">
              <h6 className="pl-3 ml-2 text-xs font-bold leading-tight uppercase opacity-60">
                Admin
              </h6>
            </li>
            <SidebarList
              icon={faUser}
              text="Profile"
              link="/profile"
              active={dashboardText === "Profile"}
            />
            <SidebarList
              icon={faUserFriends}
              text="Users"
              link="/app/user"
              permission="view_user"
              active={dashboardText === "User"}
            />
            <SidebarList
              icon={faCogs}
              text="Rolegroup"
              link="/app/group"
              permission="view_rolegroup"
              active={dashboardText === "Group"}
            />
            <SidebarList
              icon={faDiagnoses}
              text="Permissions"
              link="/app/permission"
              permission="view_permission"
              active={dashboardText === "Permission"}
            />

            <Documentation />
          </ul>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
