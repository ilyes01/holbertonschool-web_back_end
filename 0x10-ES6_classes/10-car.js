export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() { return this; }

  cloneCar() {
    const DerivedObj = this.constructor[Symbol.species];
    return new DerivedObj(this._brand, this._motor, this._color);
  }

  toString() {
    return `${this._color} ${this._brand} with ${this._motor} motor`;
  }
}
