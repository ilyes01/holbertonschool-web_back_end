export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
  return this._code;
  }

  get name() {
    this._name;
  }

  set code(code) {
  return this._code = code;
  }

  set name(name) {
    this._name = name;
  }

  displayFullCurrency() {
    return `${this._name} (${this.code})`;
  }
}
