``` javascript
/*
Template Description: This function implements the checksum algorithm for validating the integrity of self-maintained order books on Okex.
Usage: $.okex_checksum(bids, asks)

Parameters:
- bids Array, e.g., [["49194", "5", "0", "1"], ["49190.4", "1", "0", "1"]]
- asks Array, e.g., [["49194.1", "447", "0", "5"], ["49197.1", "132", "0", "1"]]

Return:
- Result of the calculation, number, e.g., -1089185544
*/

// ********************* CRC32 Algorithm Start ***********************
function signed_crc_table() {
	var c = 0, table = new Array(256);

	for(var n =0; n != 256; ++n){
		c = n;
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		c = ((c&1) ? (-306674912 ^ (c >>> 1)) : (c >>> 1));
		table[n] = c;
	}

	return typeof Int32Array !== 'undefined' ? new Int32Array(table) : table;
}

var T = signed_crc_table();

function crc32_str(str, seed) {
	var C = seed ^ -1;
	for(var i = 0, L=str.length, c, d; i < L;) {
		c = str.charCodeAt(i++);
		if(c < 0x80) {
			C = (C>>>8) ^ T[(C ^ c)&0xFF];
		} else if(c < 0x800) {
			C = (C>>>8) ^ T[(C ^ (192|((c>>6)&31)))&0xFF];
			C = (C>>>8) ^ T[(C ^ ((c>>6)&31))&0xFF] | C << 8;
			C = (C>>>8) ^ T[(C ^ (c<<6)|192)&0xFF];
		} else if(c < 0x10000) {
			C = (C>>>8) ^ T[(C ^ ((c>>12)&31))&0xFF] | C << 8;
			C = (C>>>8) ^ T[(C ^ (c<<12)|480)&0xFF];
		}
	}
	return C;
}

// ********************* End of CRC32 Algorithm ***********************

function okexChecksum(bids, asks) {
	var bidStr = JSON.stringify(bids);
	var askStr = JSON.stringify(asks);
	return crc32_str(bidStr + askStr, 0);
}

var bids = [
	["49194", "5", "0", "1"],
	["49190.4", "1", "0", "1"]
];

var asks = [
	["49194.1", "447", "0", "5"],
	["49197.1", "132", "0", "1"]
];

console.log(okexChecksum(bids, asks));
``` 

This code snippet defines the `okexChecksum` function that calculates the CRC32 checksum for a given set of bids and asks using the provided algorithm. The example also includes sample data for bids and asks to demonstrate usage. Please ensure you replace the sample data with actual data as needed. Note that the `crc32_str` implementation here is simplified for clarity, but in practice, more optimized or precomputed tables might be used for better performance. 

The `okexChecksum` function concatenates the stringified bid and ask arrays, then computes the CRC32 checksum using the `crc32_str` function. The result is printed to the console. Adjust the sample data as necessary for your specific use case. If you have more bids and asks, just extend the respective arrays accordingly. 

If there are any specific parts of this code or the explanation that need further clarification, please let me know! 🚀✨