'use strict';

const express = require('express');
const crypto = require('crypto');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';
const KEY = 'af1dd3e67233248d30690ab0614b3fdf';
const algorithm = 'aes-256-cbc';
const newiv = 'f15188446e6e3167'

function encrypt(text) {
 let cipher = crypto.createCipheriv('aes-256-cbc', KEY, newiv);
 let encrypted = cipher.update(text);
 encrypted = Buffer.concat([encrypted, cipher.final()]);
 return { iv: newiv, encryptedData: encrypted.toString('hex')};
}

function decrypt(iv, text) {
 let encryptedText = Buffer.from(text, 'hex');
 let decipher = crypto.createDecipheriv(algorithm, KEY, iv);
 let decrypted = decipher.update(encryptedText);
 decrypted = Buffer.concat([decrypted, decipher.final()]);
 return decrypted.toString();
}

// App
const app = express();
app.get('/', (req, res) => {
    //res.redirect('http://' + HOST + ':' + PORT + '/login?iv=104fb073f9a131f2cab49184bb864ca2&session=d71100525e8655b19792e0331a3b741a')
    res.redirect('http://challenges.ctfd.io:30459/login?iv=f15188446e6e3167&session=bbf6ad986ed574e8949d7b7e9348f38c4d1d93ab85062c3f168b1c82b7279845')
});

app.get('/login', (req, res) => {
	var out = decrypt(req.query.iv, req.query.session);
	var split_txt = out.split('||');

    res.writeHeader(200, {"Content-Type": "text/html"});
    res.write('<!DOCTYPE html>\n');
    res.write('<html>\n');
    res.write('<body>\n');
	res.write('<h2>This is a restricted page only authorized users can access it</h2>\n');
	if (split_txt[1] == '00') {
		res.write('<h1>Welcome "root" here is the flag</h1>\n');
		res.write('<p>ATR[Crypt0IsAsGoodAsTheImplementation]</p>\n');
	}
	res.write('<br>\n');
 	res.write('<b>Current User: ' + split_txt[0] + ' UID: ' + split_txt[1] + '</b>\n');
    res.write('</body>\n');
    res.write('<!-- Changelog -->\n');
    res.write('<!-- 09/15/2018 - Changed from DES to AES-256-CBC after our latest data breach -->\n');
    res.write('<!-- 05/23/2018 - Todd is and idiot and somehow never knows how to login so I have added the encryption IV and the encrypted session to the URL parameters -->\n');
    res.write('<!-- 03/12/2018 - String compare of the users is acting up I found a different way to validate users -->\n');
    res.write('<!-- 02/08/2018 - Moved the default user from root to unprivlaged users. This way only admins can access this page -->\n');
    res.write('</html>\n');
    res.end();
});



app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
