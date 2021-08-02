const axios = require('axios');
const cheerio = require('cheerio');

const getGamekeeperVerdun = async (cardNameSearch) => {
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
        let cardInfo = $('ul > li > div.inner')
        let cardLink = cardInfo.find('div.image-meta > div.meta > a')
        //title is contained inside of the 'a' tag in the html
        let cardTitle = cardLink.find('h4')
        let cardPriceInfo = cardInfo.find('div.variants > div.variant-row')
        let cardStock = cardPriceInfo.find('span.variant-main-info > span.variant-short-info')
        console.log(cardStock.text());
        let cardPrice = cardPriceInfo.find('span.variant-buttons div.product-price-qty > span')

        //transforming the data into JS arrays so I can use it more easily.
        var cardTitleArray = cardTitle.toArray().map((element) => { return $(element) });
        var cardStockArray = cardStock.toArray().map((element) => { return $(element).text() });
        var cardPriceArray = cardPrice.toArray().map((element) => { return $(element).text() });
        var cardLinkArray = cardLink.toArray().map((element) => {return $(element) });
        
        //fills the array with JS objects containing the card's title/set, its price, and the seller who is selling it.
        for (var i = 0; i < cardTitle.length; i++){
            //if the card is not in stock, do not include it in the search
            if (cardStockArray[i].includes('Hors stock')){
                continue;
            } else {
                var listing = {
                    title: cardTitleArray[i].attr('title'),
                    price: cardPriceArray[i],
                    seller: "gamekeeperverdun.com",
                    link: "https://www.gamekeeperverdun.com" + cardLinkArray[i].attr('href'),
                }
                cardListings.push(listing);
            }
        }

        return cardListings;
        
    } catch (error) {
        throw error;
    }
} 

//takes a string input and appropriately formats the facetoface url to be functional
function createAppropriateURL(cardName){
    var url = "https://www.gamekeeperverdun.com/products/search?q=" + cardName;
    return url;
}

getGamekeeperVerdun("monster reborn")
.then((cardListings) => console.log(cardListings));