import * as nom2 from "../jsencrypt.min.js";
var decrypt = new JSEncrypt();
// decrypt.setPrivateKey(document.getElementById("privkeyRed").value);
decrypt.setPrivateKey("-----BEGIN RSA PRIVATE KEY-----\n"+
"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\n"+
"-----END RSA PRIVATE KEY-----");