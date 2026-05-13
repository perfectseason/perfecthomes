import React from "react";
import Autoplay from "embla-carousel-autoplay";

import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "./carousel";

export default function MyCarousel() {
  const images = [
    "/house1.jpg",
    "/house2.jpg",
    "/interior1.jpg",
    "/interior2.jpg",
  ];

  return (
    <div className="w-full max-w-4xl mx-auto">
      <Carousel
        plugins={[
          Autoplay({
            delay: 2000,
          }),
        ]}
      >
        <CarouselContent>
          {images.map((img, index) => (
            <CarouselItem key={index}>
              <img
                src={img}
                alt="carousel image"
                className="w-full h-[400px] object-cover rounded-xl"
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
