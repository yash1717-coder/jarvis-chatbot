import * as THREE from 'three';

class JarvisRobot {
    constructor() {
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(this.renderer.domElement);

        this.robot = this.createRobot();
        this.scene.add(this.robot);
        this.camera.position.z = 5;

        this.animate();
    }

    createRobot() {
        const geometry = new THREE.BoxGeometry(1, 1, 1);
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
        const robot = new THREE.Mesh(geometry, material);
        return robot;
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        this.robot.rotation.x += 0.01;
        this.robot.rotation.y += 0.01;
        this.renderer.render(this.scene, this.camera);
    }
}

export default JarvisRobot;