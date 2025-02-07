import { useState, useEffect } from "react";
import { fetchAll, fetchData, login } from "@/utils/Api"; // Fetch users and handle login
import { toast } from "react-toastify";
import Layout from "./Layout";
import Loading from "./Loading";
import Link from "next/link";
import { saveToDB } from "@/utils/indexedDB"; // Save auth token
import { useRouter } from "next/router";
import { FaEye, FaEyeSlash } from "react-icons/fa"; // Icons for show/hide password

export default function LoginForm() {
  const [users, setUsers] = useState(null);
  const [selectedUser, setSelectedUser] = useState(null); // Store selected user
  const [password, setPassword] = useState(""); // Store password
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false); // Password toggle
  const router = useRouter();

  useEffect(() => {
    // Fetch list of users from API
    const fetchUsers = async () => {
      setIsLoading(true);
      try {
        const response = await fetchAll({}, "user/list");

        if (response?.data) {
          setUsers(response.data);
        } else {
          toast.error("Failed to fetch users");
        }
      } catch (error) {
        toast.error("Error fetching users");
      } finally {
        setIsLoading(false);
      }
    };
    if (!users) {
      fetchUsers();
    }
  }, []);

  const handleUserSelect = (user) => {
    setSelectedUser(user); // Move to step 2 by selecting the user
  };

  const handleLogin = async () => {
    setIsLoading(true);
    try {
      const response = await login({
        username: selectedUser.username,
        password,
      });

      if (response?.data) {
        toast.success("Login successful!");
        const { token, firstTimeLogin } = response.data;

        if (token) {
          await saveToDB("authToken", token);
        }

        if (firstTimeLogin) {
          toast.info("OTP sent for first-time login.");
          router.push("/otp-verification"); // Redirect to OTP verification page
        } else {
          router.push("/").then(() => {
            // router.reload();
          });
        }
      } else {
        toast.error(`Login failed: ${response?.message || "Unknown error"}`, {
          autoClose: false,
        });
      }
    } catch (error) {
      toast.error(`Login failed: ${error.message || "Unknown error"}`, {
        autoClose: false,
      });
    } finally {
      setIsLoading(false);
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword((prevState) => !prevState);
  };

  return (
    <Layout gradientFrom="purple-700" gradientTo="pink-500">
      {isLoading && <Loading />}
      <div className={`mx-auto p-8 ${isLoading ? "opacity-60" : ""}`}>
        <div className="flex flex-row justify-between">
          <h1 className="text-2xl text-black font-semibold">Login</h1>
          <Link href="/">
            <div className="transition duration-300">Home</div>
          </Link>
        </div>

        {!selectedUser ? (
          // Step 1: Display list of users to select from
          <div className="grid grid-cols-2 text-center gap-4 mt-8">
            {users?.map((user) => (
              <div
                key={user.username}
                className="p-4 border flex items-center rounded-lg shadow cursor-pointer hover:bg-gray-100"
                onClick={() => handleUserSelect(user)}
              >
                <h3 className="text-lg font-semibold">{user.username}</h3>
              </div>
            ))}
          </div>
        ) : (
          // Step 2: Display password input for the selected user
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleLogin();
            }}
            className="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7"
          >
            <div className="relative">
              <h3 className="text-lg font-semibold">
                @{selectedUser.username}
              </h3>
            </div>
            <div className="relative mt-4">
              <input
                required
                autoComplete="off"
                id="password"
                name="password"
                type={showPassword ? "text" : "password"} // Toggle between text/password
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="peer placeholder-transparent h-10 w-full border-b-2 border-gray-300 text-gray-900 focus:outline-none focus:border-b-blue-600"
                placeholder="Password"
              />
              <label
                htmlFor="password"
                className="absolute left-0 -top-3.5 text-gray-600 text-sm peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-440 peer-placeholder-shown:top-2 transition-all peer-focus:-top-3.5 peer-focus:text-gray-600 peer-focus:text-sm"
              >
                Password <span className="text-red-600">*</span>
              </label>
              <span
                onClick={togglePasswordVisibility}
                className="absolute right-0 top-2 cursor-pointer text-gray-600"
              >
                {showPassword ? <FaEyeSlash /> : <FaEye />}
              </span>
            </div>
            <button
              type="submit"
              className="relative inline-block w-full px-6 py-3 my-4 text-xs font-bold text-center text-white uppercase align-middle transition-all ease-in border-0 rounded-lg select-none shadow-soft-md bg-150 bg-x-25 leading-pro bg-gradient-to-tl from-purple-800 to-purple-700 hover:shadow-soft-2xl hover:scale-102"
            >
              Login
            </button>
          </form>
        )}
      </div>
    </Layout>
  );
}
