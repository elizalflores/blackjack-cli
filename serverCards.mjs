const suits = ["\u2660", "\u2665", "\u2663", "\u2666"]; // S = Spades, H = Hearts, C = Clubs, D = Diamonds
const ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'];

const shuffleDeck = (deck) => {
    let shuffledDeck = [];
    while (deck.length > 0) {
        const randomIndex = Math.floor(Math.random() * deck.length);
        const card = deck.splice(randomIndex, 1)[0];
        shuffledDeck.push(card);
    }

    return shuffledDeck;
}

const createDeck = () => {
    let deck = [];
    for (let suit of suits) {
        for (let rank of ranks) {
            const card = `${suit} ${rank}`;
            deck.push(card);
        }
    }

    return deck;
}


export {createDeck, shuffleDeck};