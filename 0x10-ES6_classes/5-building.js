// Task(5) Implement a class named Building

export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building) {
      if (!this.evacuationWarningMessage) {
        throw Error('Class extending Building must override evacuationWarningMessage');
      }
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    this._sqft = newSqft;
  }
}
