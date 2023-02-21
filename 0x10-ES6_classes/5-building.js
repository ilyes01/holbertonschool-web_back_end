// Building class
export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  // Getters
  get sqft() {
    return this._sqft;
  }

  // Abstract method for evacuation warning message
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
