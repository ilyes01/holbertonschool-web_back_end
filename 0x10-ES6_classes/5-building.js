export default class Building {
  constructor(sqft) {
    if (this.constructor !== building) {
      if (!this.evacuationWarningMessage) throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }
}
