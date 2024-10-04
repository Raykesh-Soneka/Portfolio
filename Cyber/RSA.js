// Function to generate a random prime number
function generatePrime() {
    const max = 1000000;
    const min = 100000;
    const num = Math.floor(Math.random() * (max - min + 1)) + min;
    if (isPrime(num)) {
      return num;
    } else {
      return generatePrime();
    }
  }
  
  // Function to check if a number is prime
  function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }
  
  // Function to calculate the greatest common divisor (GCD)
  function gcd(a, b) {
    if (b === 0) return a;
    return gcd(b, a % b);
  }
  
  // Function to calculate the modular inverse
  function modInverse(a, m) {
    let m0 = m;
    let y = 0;
    let x = 1;
    if (m === 1) return 0;
    while (a > 1) {
      let q = Math.floor(a / m);
      let t = m;
      m = a % m;
      a = t;
      t = y;
      y = x - q * y;
      x = t;
    }
    if (x < 0) x += m0;
    return x;
  }
  
  // Function to generate a key pair
  async function generateKeyPair() {
    let p = generatePrime();
    let q = generatePrime();
    let n = p * q;
    let phi = (p - 1) * (q - 1);
    let e = 2;
    while (gcd(e, phi) !== 1) {
      e++;
    }
    const d = modInverse(e, phi);
    return { publicKey: { e, n }, privateKey: { d, n } };
  }
  
  // Function to encrypt a message
  async function encryptMessage(message, publicKey) {
    const { e, n } = publicKey;
    const encrypted = [];
    for (let i = 0; i < message.length; i++) {
      const charCode = message.charCodeAt(i);
      const encryptedCharCode = Math.pow(charCode, e) % n;
      encrypted.push(encryptedCharCode);
    }
    return encrypted;
  }
  
  // Function to decrypt a message
  async function decryptMessage(encryptedMessage, privateKey) {
    const { d, n } = privateKey;
    const decrypted = [];
    for (let i = 0; i < encryptedMessage.length; i++) {
      const encryptedCharCode = encryptedMessage[i];
      const charCode = Math.pow(encryptedCharCode, d) % n;
      decrypted.push(String.fromCharCode(charCode));
    }
    return decrypted.join('');
  }
  
  // Example usage:
  async function main() {
    const keyPair = await generateKeyPair();
    const message = 'Hello, World!';
    const encryptedMessage = await encryptMessage(message, keyPair.publicKey);
    console.log(`Encrypted message: ${encryptedMessage}`);
    const decryptedMessage = await decryptMessage(encryptedMessage, keyPair.privateKey);
    console.log(`Decrypted message: ${decryptedMessage}`);
  }
  
  main();