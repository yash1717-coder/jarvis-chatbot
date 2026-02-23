import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';

const JarvisRobot = () => {
    const containerRef = useRef(null);
    const sceneRef = useRef(null);
    const cameraRef = useRef(null);
    const rendererRef = useRef(null);

    useEffect(() => {
        // Create scene
        sceneRef.current = new THREE.Scene();

        // Create camera
        cameraRef.current = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        cameraRef.current.position.z = 5;

        // Create renderer
        rendererRef.current = new THREE.WebGLRenderer({ antialias: true });
        rendererRef.current.setSize(window.innerWidth, window.innerHeight);
        containerRef.current.appendChild(rendererRef.current.domElement);

        // Add a robot (simple cube as a placeholder)
        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
        const robot = new THREE.Mesh(geometry, material);
        sceneRef.current.add(robot);

        // Animation loop
        const animate = () => {
            requestAnimationFrame(animate);
            robot.rotation.x += 0.01;
            robot.rotation.y += 0.01;
            rendererRef.current.render(sceneRef.current, cameraRef.current);
        };
        animate();

        // Handle window resize
        const handleResize = () => {
            const width = window.innerWidth;
            const height = window.innerHeight;
            cameraRef.current.aspect = width / height;
            cameraRef.current.updateProjectionMatrix();
            rendererRef.current.setSize(width, height);
        };

        window.addEventListener('resize', handleResize);

        // Cleanup
        return () => {
            window.removeEventListener('resize', handleResize);
            rendererRef.current.dispose();
            sceneRef.current = null;
            cameraRef.current = null;
            rendererRef.current = null;
        };
    }, []);

    return <div ref={containerRef} />;
};

export default JarvisRobot;