const axios = require('axios');
const cheerio = require('cheerio');

const getCardBrawlers = async (cardNameSearch) => {
    try {
        //creates the appropriate url (will be changed to accept input in the future)
        var urlToSearch = createAppropriateURL(cardNameSearch);
        const { data } = await axios.get(
			urlToSearch,
        );
        
        //loads in the html
        const $ = cheerio.load(data);
        const cardListings = [];

        //filtering out the irrelevant data
        let cardInfo = $('div.Norm');
        let cardTitle = cardInfo.find('p.productTitle');
        let cardPriceBasic = cardInfo.find('p.productPrice'/* > span.money' */);
        //TODO: handle varies prices
        let cardLink = cardInfo.find('div.hoverMask > div.buyWrapper > div.view > a');

        //let cardPriceComplex = cardInfo.find('div.hoverMask > ');

        //transforming the data into JS arrays so I can use it more easily.
        var cardTitleArray = cardTitle.toArray().map((element) => { return $(element).text().trim() });
        var cardPriceArray = cardPriceBasic.toArray().map((element) => { return $(element) });
        //var cardPriceArrayText = cardPriceBasic.toArray().map((element) => { return $(element).text() });
        var cardLinkArray = cardLink.toArray().map((element) => { return $(element).attr('href') });

        //will remove these, still useful for testing right now
        // console.log(cardTextArray);
        // console.log(cardPriceArrayText);
        // console.log(cardLinkArray);
        
        //fills the array with JS objects containing the card's title/set, its price, and the seller who is selling it.
        for (var i = 0; i < cardTitle.length; i++){
            if (cardPriceArray[i].text().includes('Varies')){
                continue;
            } else {
                var listing = {
                    title: cardTitleArray[i],
                    price: cardPriceArray[i].find('span.money').text(),
                    seller: "cardbrawlers.com",
                    link: "https://cardbrawlers.com/" + cardLinkArray[i],
                }
                    cardListings.push(listing);
            }
        }
        return cardListings;
        
    } catch (error) {
        throw error;
    }
} 

//takes a string input and appropriately formats the cardbrawlers url to be functional
function createAppropriateURL(cardName){
    var card_words_array = cardName.split();
    var url_name_section = "";

    //generates a url based on the given card name
    for (var i = 0; i < card_words_array.length; i++){
        if ((card_words_array.length - 1) == i){
            url_name_section += card_words_array[i];
        } else {
            url_name_section += card_words_array[i];
            url_name_section += "+"
        }
    }
    var url = "https://cardbrawlers.com/search?q=*" + url_name_section + "*+product_type%3A%22yugioh%22";
    return url;
}

getCardBrawlers("monster reborn")
.then((cardListings) => console.log(cardListings));