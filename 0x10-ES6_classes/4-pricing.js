// Import Currency class
import { Currency } from './3-currency.js';

// Pricing class
class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // Getters and setters
  get amount() {
    return this._amount;
  }

  set amount(amount) {
    this._amount = amount;
  }

  get currency() {
    return this._currency;
  }

  set currency(currency) {
    this._currency = currency;
  }

  // Display full price method
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static method to convert price
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
