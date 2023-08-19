import express from 'express';
import cors from 'cors';
import 'dotenv/config';

import { createDeck, shuffleDeck } from './serverCards.mjs';

const PORT = process.env.PORT || 5000;

const app = express();
app.use(cors());
app.use(express.json());

/* 
 * GET /api/shuffle Endpoint
 * (Query Parameters: numDecks[Integer])
 * Returns respoonse with numDecks number of shuffled decks
*/
app.get('/api/shuffle', (req, res) => {
    // Get Query Parameters
    console.log("Request:", req.query.numDecks)
    let numDecks = req.query.numDecks;
    
    // Default Query Parameters
    if (numDecks === undefined) {
        numDecks = 1;
    }

    // Validate Query Parameters
    if (numDecks < 1 || numDecks > 10 || numDecks % 1 !== 0 | isNaN(numDecks)) {
        res.status(400).send({"error": "Invalid number of decks. Please choose an integer between 1 and 10."});
        return;
    }

    // Handle Request
    let cards = [];

    for (let i = 0; i < numDecks; i++) {
        cards = cards.concat(createDeck());
    }

    const deck = shuffleDeck(cards);

    // Response and Logging
    res.status(200).send({"cards": deck});
    console.info(`[/api/shuffle] ${numDecks} new decks shuffled`)
});

/* 
 * PUT /api/reshuffle Endpoint
 * (Query Parameters: cards[Array])
 * Returns respoonse with cards in a new order
*/
app.put('/api/reshuffle', (req, res) => {
    // Get Request Body
    const cards = req.body.cards;

    // Validate Request Body
    if (cards === undefined) {
        res.status(400).send({"error": "Please specify the cards to shuffle."});
        return;
    }

    if (!Array.isArray(cards)) {
        res.status(400).send({"error": "Invalid cards. Please send an array of cards."});
        return;
    }

    // Handle Request
    const reshuffledCards = shuffleDeck(cards);
    
    // Response and Logging
    res.status(200).send({"cards": reshuffledCards});
    console.info(`[/api/reshuffle] ${reshuffledCards.length} cards shuffled`)
});


app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`)
});
