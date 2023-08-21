import * as THREE from "./three.min.js";
import { STLLoader } from "./STLLoader.js";
import { OrbitControls } from "./OrbitControls.js";


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  70,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableZoom = false;
controls.enablePan = false;
controls.enableDamping = true;
controls.dampingFactor = 0.45;

// Load Light
var ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);
const light2 = new THREE.PointLight(0xffffff, 1.4, 2000);
light2.position.set(0, 0, 1);
camera.add(light2);
scene.add(camera);

// Instantiate a loader
const loader = new STLLoader();

const targetSize = 5;
let distance=0;
let modelCenter=0;

loader.load(
  // resource URL
  URL_OF_STL_MODEL_FILE,
  // called when the resource is loaded
  function (geometry) {
    geometry.center();
    const material = new THREE.MeshStandardMaterial({ color: 0x595959 });
    const obj = new THREE.Mesh(geometry, material);

    // Calculate scaling factor and apply it
    const boundingBox = new THREE.Box3().setFromObject(obj);
    const modelSize = boundingBox.getSize(new THREE.Vector3()).length();
    const scaleFactor = targetSize / modelSize;
    obj.scale.set(scaleFactor/2, scaleFactor/2, scaleFactor/2);

    scene.add(obj);

    // Adjust camera position
    const fovInRadians = THREE.MathUtils.degToRad(camera.fov);
    const halfHeight = targetSize / 2;
     distance = halfHeight / Math.tan(fovInRadians / 2);
     modelCenter = boundingBox
      .getCenter(new THREE.Vector3())
      .multiplyScalar(scaleFactor);
    camera.position.set(modelCenter.x, modelCenter.y, modelCenter.z + distance);
    camera.lookAt(modelCenter);
    camera.updateProjectionMatrix();
  },
  // called while loading is progressing
  function (xhr) {
    console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
  },
  // called when loading has errors
  function (error) {
    console.log(error);
  }
);

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
  controls.update();
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

animate();
window.addEventListener("resize", onWindowResize, false);
document
  .querySelector(".icon-home-container")
  .addEventListener("click", (e) => {
  
    controls.reset();
    camera.position.set(modelCenter.x, modelCenter.y, modelCenter.z + distance);
});
