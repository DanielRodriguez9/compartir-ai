import Particles from "react-tsparticles";
import { loadSlim } from "tsparticles-slim";

const ParticlesBackground = () => {
  const particlesInit = async (engine) => {
    await loadSlim(engine);
  };

  return (
    <Particles
      id="tsparticles"
      init={particlesInit}
      options={{
        background: { color: { value: "transparent" } },
        fpsLimit: 60,
        particles: {
          color: { value: "#ffffff" },
          links: { enable: true, color: "#ffffff", distance: 150 },
          move: { enable: true, speed: 1 },
          number: { value: 80 },
          size: { value: 2 },
          opacity: { value: 0.5 },
        },
        interactivity: {
          events: { onHover: { enable: true, mode: "repulse" } },
        },
      }}
      className="absolute inset-0 -z-10"
    />
  );
};

export default ParticlesBackground;