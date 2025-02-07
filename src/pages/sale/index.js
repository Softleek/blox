import { useEffect, useState } from "react";
import { fetchData, postData } from "@/utils/Api";
import { useRouter } from "next/router";
import { toast } from "react-toastify";
import { getFromDB } from "@/utils/indexedDB";
import { useNavbar } from "@/contexts/NavbarContext";
import { useSidebar } from "@/contexts/SidebarContext";

import ProductList from "@/pos/pos/templates/sale/ProductList";
import Cart from "@/pos/pos/templates/sale/Cart";
import CheckoutForm from "@/pos/pos/templates/sale/CheckoutForm";
import ItemGroupSelector from "@/pos/pos/templates/sale/ItemGroupSelector"; // Import the new component
import { useData } from "@/contexts/DataContext";

export default function SalePage() {
  const [cart, setCart] = useState([]);
  const [total, setTotal] = useState(0);
  const [products, setProducts] = useState([]);
  const [pmt, setPmt] = useState([]);
  const [quantities, setQuantities] = useState({});
  const [transactionCode, setTransactionCode] = useState("");
  const [transactionMethod, setTransactionMethod] = useState("");
  const [commission, setCommission] = useState(0);
  const [discount, setDiscount] = useState(0);
  const [profile, setProfile] = useState(null);
  const [prices, setPrices] = useState({});
  const [selectedUOM, setSelectedUOM] = useState({});
  const [itemGroups, setItemGroups] = useState([]); // Store all item groups
  const [selectedItemGroup, setSelectedItemGroup] = useState(null); // State for the selected item group
  const [search, setSearch] = useState(""); // State to track search input

  const { updateDashboardText, updateTextColor, updateIconColor } = useNavbar();
  const { setSidebarHidden } = useSidebar();
  const router = useRouter();
  const { loading, setLoading } = useData();

  useEffect(() => {
    updateDashboardText("Sale");
    updateTextColor("text-gray-900");
    updateIconColor("text-purple-900");
    setSidebarHidden(true);
  }, [router.pathname, updateDashboardText, updateTextColor, setSidebarHidden]);

  // Fetch payment methods, profile, and item groups
  useEffect(() => {
    const fetchPmt = async () => {
      try {
        const response = await fetchData({}, "pos/payment_method");
        if (response?.data) {
          setPmt(response.data.data);
        }
      } catch (error) {
        toast.error(`Failed to fetch data: ${error.message || error}`);
      }
    };

    const fetchProfile = async () => {
      const storedProfile = await getFromDB("profile");
      setProfile(storedProfile);
    };

    const fetchItemGroups = async () => {
      try {
        const response = await fetchData({}, "pos/item_group");
        if (response?.data) {
          const itemGroupList = response.data.data;
          setItemGroups(itemGroupList);
          // Auto-select the first item group
          if (itemGroupList.length > 0) {
            setSelectedItemGroup(itemGroupList[0].id);
          }
        }
      } catch (error) {
        toast.error(`Failed to fetch item groups: ${error.message || error}`);
      }
    };

    fetchProfile();
    fetchPmt();
    fetchItemGroups();
  }, []);

  // Fetch products when an item group is selected
  useEffect(() => {
    const fetchProducts = async () => {
      if (!selectedItemGroup) return; // Only fetch if an item group is selected
      try {
        const response = await fetchData(
          { item_group: selectedItemGroup, search: search },
          "pos/item"
        );
        if (response?.data) {
          setProducts(response.data.data);
        }
      } catch (error) {
        toast.error(`Failed to fetch products: ${error.message || error}`);
      }
    };

    if (profile && selectedItemGroup) {
      fetchProducts();
    }
  }, [selectedItemGroup, profile, search]);

  const handleQuantityChange = (product, quantity) => {
    setQuantities({ ...quantities, [product.id]: quantity });
  };

  const handlePriceChange = (product, price) => {
    setPrices({ ...prices, [product.id]: price });
  };

  const handleUOMChange = (product, uom) => {
    setSelectedUOM({ ...selectedUOM, [product.id]: uom });
  };

  const addToCart = (product) => {
    const quantity = quantities[product.id] || 1;
    const price = prices[product.id] || product.selling_rate;
    const uom = selectedUOM[product.id] || "kg";

    if (price < product.selling_rate) {
      toast.warn(
        `Price for ${product.name} cannot be lower than Ksh. ${product.selling_rate}.`
      );
    }

    if (quantity > product.stock_quantity) {
      toast.warn("Requested quantity exceeds available stock");
      return;
    }

    const productInCart = cart.find((item) => item.id === product.id);
    if (productInCart) {
      toast.warn(
        `${product.name} is already in the cart. Please update the quantity.`
      );
      return;
    }

    setCart([
      ...cart,
      {
        ...product,
        quantity,
        price,
        uom,
        warehouse: product.default_warehouse,
      },
    ]);
    setTotal(total + price * quantity);

    updateProductStock(product.id, product.stock_quantity - quantity);
  };

  const updateProductStock = (productId, newStock) => {
    setProducts((prevProducts) =>
      prevProducts.map((product) =>
        product.id === productId
          ? { ...product, stock_quantity: newStock }
          : product
      )
    );
  };

  const removeFromCart = (product) => {
    const filteredCart = cart.filter((item) => item.id !== product.id);
    setTotal(total - product.price * product.quantity);
    setCart(filteredCart);
  };

  const handleCheckout = async () => {
    if (!transactionMethod) {
      toast.warn("Please select a transaction method");
      return;
    }

    const checkoutData = {
      items: cart,
      total,
      transactionCode,
      transactionMethod,
      commission,
      discount,
    };

    try {
      setLoading(true);
      const response = await postData(checkoutData, "core/sale");

      if (response?.success) {
        toast.success("Checkout successful!");
        router.push(`/app/sales_invoice/${response?.data?.id}`);
      } else {
        toast.error("Checkout failed. Please try again.");
      }
      setLoading(false);
    } catch (error) {
      toast.error(`Checkout failed: ${error.message || error}`);
    }
  };

  return (
    <div className="max-h-[80vh] text-purple">
      <main className="flex flex-col lg:flex-row px-2 gap-2">
        {/* Product List and Cart */}
        <div className="grid grid-cols-1 gap-4 lg:w-3/4">
          {/* Item Group Selector */}
          <ItemGroupSelector
            itemGroups={itemGroups}
            selectedItemGroup={selectedItemGroup}
            setSelectedItemGroup={setSelectedItemGroup}
            search={search}
            setSearch={setSearch}
          />
          <ProductList
            products={products}
            addToCart={addToCart}
            quantities={quantities}
            prices={prices}
            selectedUOM={selectedUOM}
            handleQuantityChange={handleQuantityChange}
            handlePriceChange={handlePriceChange}
            handleUOMChange={handleUOMChange}
          />
        </div>
        <div className="grid grid-cols-1 max-h-[100vh] p-2 w-1/4 overflow-auto gap-4 h-fit justify-left items-start">
          <Cart cart={cart} total={total} removeFromCart={removeFromCart} />

          <CheckoutForm
            pmt={pmt}
            transactionMethod={transactionMethod}
            setTransactionMethod={setTransactionMethod}
            transactionCode={transactionCode}
            setTransactionCode={setTransactionCode}
            commission={commission}
            setCommission={setCommission}
            setDiscount={setDiscount}
            discount={discount}
            handleCheckout={handleCheckout}
            total={total}
          />
        </div>
      </main>
    </div>
  );
}
