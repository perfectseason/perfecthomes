import Navbar from "../components/ui/NavBar";
import Footer from "../components/ui/Footer";
import MyCarousel from "../components/ui/MyCarousel";

const Home = () => {
  return (
    <div className="flex flex-col gap-4 p-4">
      <Navbar />
      <div className="bg-blue-200 p-6"><MyCarousel /></div>
      <div className="bg-red-200 p-6">Box 2</div>
      <div className="bg-green-200 p-6">Box 3</div>
      <Footer />
    </div>
  );
};

export default Home;
