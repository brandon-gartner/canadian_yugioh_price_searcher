const axios = require('axios');
const cheerio = require('cheerio');

const getFaceToFace = async (cardNameSearch) => {
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
        let cardInfo = $('ul > li > article')
        let cardText = cardInfo.find('div.card-body > h4.card-title > a')
        let cardPrice = cardInfo.find('div.card-text > div.card-addtoCart > div.card-price > div.primary-price--withoutTax > span.price--withoutTax')

        //transforming the data into JS arrays so I can use it more easily.
        var cardTextArray = cardText.toArray().map((element) => { return $(element).text().trim() });
        var cardPriceArray = cardPrice.toArray().map((element) => { return $(element).text() });

        //will remove these, still useful for testing right now
        // console.log(cardTextArray)
        // console.log(cardPriceArray)
        
        //fills the array with JS objects containing the card's title/set, its price, and the seller who is selling it.
        //TODO: add a link to the listing, which I can redirect users to if they click
        for (var i = 0; i < cardText.length; i++){
            var listing = {
                title: cardTextArray[i],
                price: cardPriceArray[i],
                seller: "facetofacegames.com",
                //TODO: add link
            }
            cardListings.push(listing);
        }

        return cardListings;
        
    } catch (error) {
        throw error;
    }
} 

//takes a string input and appropriately formats the facetoface url to be functional
function createAppropriateURL(cardName){
    var url = "https://www.facetofacegames.com/search.php?search_query=" + cardName + "&section=product&_bc_fsnf=1&in_stock=1&category=4878";
    return url;
}

getFaceToFace("monster reborn")
.then((cardListings) => console.log(cardListings));