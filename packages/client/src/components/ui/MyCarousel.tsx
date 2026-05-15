import Autoplay from "embla-carousel-autoplay";

import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "./carousel";

const images = [
  { src: "/house 1.jpg", alt: "Modern detached house exterior" },
  { src: "/house 2.jpg", alt: "Residential property frontage" },
  { src: "/house 3.jpg", alt: "Contemporary home exterior" },
  { src: "/house 4.jpg", alt: "Featured property exterior" },
  { src: "/interior 1.jpg", alt: "Finished living room interior" },
  { src: "/interior 3.jpg", alt: "Bright property interior" },
];

export default function MyCarousel() {
  return (
    <div className="w-full">
      <Carousel
        plugins={[
          Autoplay({
            delay: 3500,
            stopOnInteraction: true,
          }),
        ]}
      >
        <CarouselContent>
          {images.map((image) => (
            <CarouselItem key={image.src}>
              <img
                src={image.src}
                alt={image.alt}
                className="h-[360px] w-full rounded-lg object-cover sm:h-[460px]"
              />
            </CarouselItem>
          ))}
        </CarouselContent>

        <CarouselPrevious />
        <CarouselNext />
      </Carousel>
    </div>
  );
}
