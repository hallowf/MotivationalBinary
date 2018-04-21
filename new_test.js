const http = require ('http');

const quotes_url =  'http://quotes.rest/qod.json';


var get_quote = function() {
  http.get(quotes_url, (res) => {
    let data = '';
    res.on('data', (chunk) => {
      data += chunk;
    });
    res.on('end', () => {
      var json = JSON.parse(data);
      var quote_obj = json.contents.quotes;
      var quote_text = quote_obj[0].quote;
      var quote_author = quote_obj[0].author;
      console.log(quote_text)
      return_quote(quote_text)
    });
  }).on("error", (err) => {
    console.log("Error: " + err.message);
  });
}

function return_quote(res) {
  return res
}

function convert_quote(quote) {
    binary_quote = quote.toString().split('').map((char) => '0'.concat(char.charCodeAt(0).toString(2).slice(-8))).join(' ');
    console.log(binary_quote);
  }


console.log(get_quote())
