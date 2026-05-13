import Navbar from "../components/ui/NavBar";
import Footer from "../components/ui/Footer";
import ChatBot from "@/components/chat/ChatBot";
import customerImg from "../assets/products/customer.jpeg";
import supermarketImg from "../assets/products/supermarket.jpg";
import supermarket2Img from "../assets/products/supermarket2.jpg";

const Contact = () => {
  const customer = {
    id: 1,
    name: "customer",
    image: customerImg,
  };

  const supermarket = {
    id: 2,
    name: "supermarket",
    image: supermarketImg,
  };

  const supermarket2 = {
    id: 3,
    name: "supermarket2",
    image: supermarket2Img,
  };
  return (
    <>
      <Navbar />
      <section className="pt-28 min-h-screen bg-gray-50">
        <div className="max-w-3xl mx-auto px-6 py-20">
          <h1 className="text-2xl font-bold text-gray-800 mb-8">Contact Us</h1>
          <h2 className="text-lg text-gray-600 mb-6">
            Have questions? Get in touch with our support team.
          </h2>

          <form className="bg-white shadow-md rounded-lg p-8 space-y-6">
            <div>
              <label className="block text-gray-700 mb-2">Full Name</label>
              <input
                type="text"
                className="w-full border rounded-md px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div>
              <label className="block text-gray-700 mb-2">Email</label>
              <input
                type="email"
                className="w-full border rounded-md px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div>
              <label className="block text-gray-700 mb-2">Message</label>
              <textarea
                rows={4}
                className="w-full border rounded-md px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"
              ></textarea>
            </div>

            <button
              type="submit"
              className="w-full bg-blue-400 text-white py-3 rounded-md hover:bg-blue-700 transition"
            >
              Send Message
            </button>
          </form>
        </div>
      </section>

      <div className="min-h-1/2-screen w-full grid md:grid-cols-2">
        {/* LEFT COLUMN */}
        <div className="flex flex-col p-8 gap-6 space-y-6 mt-2 bg-gray-50">
          <div
            key={customer.id}
            className="bg-white shadow-md rounded-xl p-6 flex flex-col items-center text-center"
          >
            <img
              src={customer.image}
              alt={customer.name}
              className="w-40  h-40 object-cover rounded-md mb-4"
            />
            <h3 className="text-xl font-semibold text-gray-600">
              Talk to our customer support agent
            </h3>
          </div>

          <div className="flex-1 bg-white shadow-md rounded-xl p-4">
            <ChatBot />
          </div>
        </div>

        {/* RIGHT COLUMN */}
        <div className="flex flex-col p-8 gap-6 bg-white">
          <div
            key={supermarket.id}
            className="flex-1 bg-white shadow-md rounded-xl overflow-hidden"
          >
            <img
              src={supermarket.image}
              alt={supermarket.name}
              className="w-full h-full object-cover"
            />
          </div>

          <div
            key={supermarket2.id}
            className="flex-1 bg-white shadow-md rounded-xl overflow-hidden"
          >
            <img
              src={supermarket2.image}
              alt={supermarket2.name}
              className="w-full h-full object-cover"
            />
          </div>
        </div>
      </div>

      <Footer />
    </>
  );
};

export default Contact;
