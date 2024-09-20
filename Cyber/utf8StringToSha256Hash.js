function utf8StringToSha256Hash(string) {
  // Convert the UTF-8 string to a Uint8Array
  console.log("Début du hash");
  const utf8Bytes = [];
  for (let i = 0; i < string.length; i++) {
    let charCode = string.charCodeAt(i);
    if (charCode < 0x80) {
      utf8Bytes.push(charCode);
    } else if (charCode < 0x800) {
      utf8Bytes.push(0xc0 | (charCode >> 6));
      utf8Bytes.push(0x80 | (charCode & 0x3f));
    } else if (charCode < 0xd800 || charCode >= 0xe000) {
      utf8Bytes.push(0xe0 | (charCode >> 12));
      utf8Bytes.push(0x80 | ((charCode >> 6) & 0x3f));
      utf8Bytes.push(0x80 | (charCode & 0x3f));
    } else {
      utf8Bytes.push(0xf0 | (charCode >> 18));
      utf8Bytes.push(0x80 | ((charCode >> 12) & 0x3f));
      utf8Bytes.push(0x80 | ((charCode >> 6) & 0x3f));
      utf8Bytes.push(0x80 | (charCode & 0x3f));
    }
  }

  // SHA-256 constants
  const k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
    0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
    0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
    0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
    0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
  ];
  console.log("SHA-256 constants définie");

  // SHA-256 functions
  function rotr(x, n) {
    return (x >>> n) | (x << (32 - n));
  }

  function sigma0(x) {
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22);
  }

  function sigma1(x) {
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25);
  }

  function gamma0(x) {
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >>> 3);
  }

  function gamma1(x) {
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >>> 10);
  }
  console.log("SHA-256 functions définie");

  // SHA-256 main loop
  let h0 = 0x6a09e667;
  let h1 = 0xbb67ae85;
  let h2 = 0x3c6ef372;
  let h3 = 0xa54ff53a;
  let h4 = 0x510e527f;
  let h5 = 0x9b05688c;
  let h6 = 0x1f83d9ab;
  let h7 = 0x5be0cd19;

  for (let i = 0; i < utf8Bytes.length; i += 64) {
    let w = new Array(64);
    for (let j = 0; j < 16; j++) {
      w[j] =
        (utf8Bytes[i + j * 4] << 24) |
        (utf8Bytes[i + j * 4 + 1] << 16) |
        (utf8Bytes[i + j * 4 + 2] << 8) |
        utf8Bytes[i + j * 4 + 3];
    }
    for (let j = 16; j < 64; j++) {
      w[j] = gamma1(w[j - 2]) + w[j - 15];
    }

    let a = h0;
    let b = h1;
    let c = h2;
    let d = h3;
    let e = h4;
    let f = h5;
    let g = h6;
    let h = h7;

    for (let j = 0; j < 64; j++) {
      let S1 = sigma1(e);
      let ch = (e & f) ^ (~e & g);
      let temp1 = h + S1 + ch + k[j] + w[j];
      let S0 = sigma0(a);
      let maj = (a & b) ^ (a & c) ^ (b & c);
      let temp2 = S0 + maj;

      h = g;
      g = f;
      f = e;
      e = (d + temp1) >>> 0;
      d = c;
      c = b;
      b = a;
      a = (temp1 + temp2) >>> 0;
    }

    h0 = (h0 + a) >>> 0;
    h1 = (h1 + b) >>> 0;
    h2 = (h2 + c) >>> 0;
    h3 = (h3 + d) >>> 0;
    h4 = (h4 + e) >>> 0;
    h5 = (h5 + f) >>> 0;
    h6 = (h6 + g) >>> 0;
    h7 = (h7 + h) >>> 0;
  }

  // Convert the hash values to a hexadecimal string
  let hash = [
    h0.toString(16).padStart(8, "0"),
    h1.toString(16).padStart(8, "0"),
    h2.toString(16).padStart(8, "0"),
    h3.toString(16).padStart(8, "0"),
    h4.toString(16).padStart(8, "0"),
    h5.toString(16).padStart(8, "0"),
    h6.toString(16).padStart(8, "0"),
    h7.toString(16).padStart(8, "0"),
  ].join("");
  console.log("SHA-256 hash finie");

  return hash;
}

//TODO
function hashInput() {
  const input = document.getElementById("input").value;
  const hash = utf8StringToSha256Hash(input);
  var hashTest = hash;

  const originalStr = "Hello, World! Test";
  const key = "${hashTest}";
  const encryptedStr = xorEncrypt(originalStr, key);
  console.log(encryptedStr); // Output: a encrypted string
  document.getElementById("output2").innerHTML = `Encrypt : ${encryptedStr}`;

  // To decrypt, simply call the function again with the same key
  const decryptedStr = xorEncrypt(encryptedStr, key);
  console.log(decryptedStr); // Output: a decrypted string
  document.getElementById("output3").innerHTML = `Decrypt : ${decryptedStr}`;

  document.getElementById("output").innerHTML = `SHA-256 Hash: ${hash}`;
}

function xorEncrypt(str, key) {
  let encryptedStr = "";
  for (let i = 0; i < str.length; i++) {
    encryptedStr += String.fromCharCode(
      str.charCodeAt(i) ^ key.charCodeAt(i % key.length)
    );
  }
  return encryptedStr;
}

// //Test
// const originalStr = 'Hello, World!';
// const key = 'mySecretKey';
// const encryptedStr = xorEncrypt(originalStr, key);
// console.log(encryptedStr); // Output: a encrypted string

// // To decrypt, simply call the function again with the same key
// const decryptedStr = xorEncrypt(encryptedStr, key);
// console.log(decryptedStr); // Output: 'Hello, World!'
