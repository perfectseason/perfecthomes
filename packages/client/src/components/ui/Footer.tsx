const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white mt-20">
      <div className="max-w-7xl mx-auto px-6 py-10 grid md:grid-cols-3 gap-8">
        <div>
          <h2 className="text-xl font-semibold">Perfect Season</h2>
          <p className="text-gray-400 mt-3">
            Your trusted ecommerce partner delivering quality worldwide.
          </p>
        </div>

        <div>
          <h3 className="font-semibold mb-3">Quick Links</h3>
          <ul className="space-y-2 text-gray-400">
            <li>Home</li>
            <li>About</li>
            <li>Contact</li>
          </ul>
        </div>

        <div>
          <h3 className="font-semibold mb-3">Contact Info</h3>
          <p className="text-gray-400">support@perfectseason.com</p>
          <p className="text-gray-400">+234 810 697 8741</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
