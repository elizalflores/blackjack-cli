import axios from 'axios';
import 'dotenv/config';

const PORT = process.env.PORT || 5000;
const microservice_url = `http://localhost:${PORT}`;

async function testShuffle(numDecks) {
    try {
        const response = await axios.get(`${microservice_url}/api/shuffle?numDecks=${numDecks}`);
        console.log(`Test: Valid Request (numDecks = ${numDecks})`, response.data);
    } catch (error) {
        console.error(`Test: (Invalid Request (numDecks = ${numDecks})`, error.response.data);
    }
  }
  
  async function testReshuffle(cards) {
    try {
        const request_body = { "cards": cards };
        const response = await axios.put(`${microservice_url}/api/reshuffle`, request_body);
        console.log(`Test: Valid Request (cards = [${cards}])`, response.data);
    } catch (error) {
        console.error(`Test: Invalid Request (cards = ${cards})`, error.response.data);
    }
  }
  
  // Shuffle Tests
  testShuffle(1);
  testShuffle(2);
  testShuffle(10);
  testShuffle(0);
  testShuffle(11);
  testShuffle(1.5);
  testShuffle('"1"');
  testShuffle('"one"');
  testShuffle(undefined);
  
  // Reshuffle Tests
  testReshuffle(["H3", "S4", "C11", "H13", "D1", "H3", "S4", "C11", "H13", "D1"]);
  testReshuffle(["H3", "S4", "C11", "H13", "D1", "H3", "S4", "C11", "H13", "D1", "H8", "S2", "D11", "H3", "C1"]);
  testReshuffle([]);
  testReshuffle(undefined);
  testReshuffle("H3, S4, D5, C6, H7, S8, D9, C10, H11, S12, D13");
  