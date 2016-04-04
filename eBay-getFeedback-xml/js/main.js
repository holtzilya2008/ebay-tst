

/* Getting FeedBack on eBay User
	Using GetFeedback API call from the Trading API
*/

var appID = 'xxx';
var sellerName = 'dealsbuy2015';

console.log('eBay APP ID : '+appID);
console.log('current seller name : '+sellerName);

var inputData = '' +
'<?xml version="1.0" encoding="utf-8"?>' +
'<GetFeedbackRequest xmlns="urn:ebay:apis:eBLBaseComponents">' +
  '<RequesterCredentials>' +
    '<eBayAuthToken>ABC...123</eBayAuthToken>' +
  '</RequesterCredentials>' +
  '<UserID>magicalbookseller</UserID>' +
  '<DetailLevel>ReturnAll</DetailLevel>' +
'</GetFeedbackRequest>';

console.log('xml input data : ' + inputData);

var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
		  document.getElementById("demo").innerHTML =
		  xmlhttp.responseText;
		}
	};


xmlhttp.open("POST","https://api.ebay.com/ws/api.dll",true);
xmlhttp.send(escape(inputData));
