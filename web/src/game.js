export class GameSettings {
  static instance;
  constructor() { if (GameSettings.instance) return GameSettings.instance; this.theme = "fire"; this.soundEnabled = false; GameSettings.instance = this; }
}

export class Dragon {
  constructor(health = 50, armor = 3) { this.maxHealth = health; this.health = health; this.armor = armor; }
  receiveDamage(amount, type = "physical") { this.health = Math.max(0, this.health - (type === "physical" ? Math.max(0, amount - this.armor) : amount)); }
  get isAlive() { return this.health > 0; }
}

export class EnemyGroup {
  constructor(targets = []) { this.targets = targets; }
  add(target) { this.targets.push(target); }
  receiveDamage(amount, type) { this.targets.forEach((target) => target.receiveDamage(amount, type)); }
  get isAlive() { return this.targets.some((target) => target.isAlive); }
}

export class ProtectedTargetProxy {
  constructor(target) { this.target = target; this.unlocked = false; }
  unlock() { this.unlocked = true; }
  receiveDamage(amount, type) { if (!this.unlocked) throw new Error("Object needs to be unlocked first"); this.target.receiveDamage(amount, type); }
  get isAlive() { return this.target.isAlive; }
}

export class Sword { constructor(element = "physical") { this.name = element === "physical" ? "Sword" : `${element} Sword`; this.element = element; } attack() { return { success: true, damage: 10, damageType: this.element, manaCost: 0 }; } }
export class Bow { constructor(element = "physical") { this.name = element === "physical" ? "Bow" : `${element} Bow`; this.element = element; } attack(distance) { return { success: true, damage: distance < 10 ? 5 : 15, damageType: this.element, manaCost: 0 }; } }
export class Staff { constructor(element = "magical") { this.name = element === "magical" ? "Magic Staff" : `${element} Staff`; this.element = element; } attack(_distance, mana) { return mana < 5 ? { success: false, reason: "Not enough mana", manaCost: 0 } : { success: true, damage: 20, damageType: this.element, manaCost: 5 }; } }
export class EmpoweredWeapon { constructor(weapon) { this.weapon = weapon; this.name = `Empowered ${weapon.name}`; } attack(distance, mana) { const result = this.weapon.attack(distance, mana); return result.success ? { ...result, damage: result.damage + 5 } : result; } }
export class AncientAxe { strike() { return 18; } }
export class AncientAxeAdapter { constructor() { this.name = "Ancient Axe"; this.axe = new AncientAxe(); } attack() { return { success: true, damage: this.axe.strike(), damageType: "physical", manaCost: 0 }; } }

export class EquipmentFactory { constructor(theme) { this.theme = theme; } createSword() { return new Sword(this.theme); } createBow() { return new Bow(this.theme); } createStaff() { return new Staff(this.theme); } }

class NormalState { canAttack() { return true; } canSwitch() { return true; } }
class StunnedState { canAttack() { return false; } canSwitch() { return true; } }
class DeadState { canAttack() { return false; } canSwitch() { return false; } }
export class Player {
  constructor(factory) { this.maxMana = 10; this.mana = 10; this.weapon = factory.createSword(); this.state = new NormalState(); }
  switchWeapon(weapon) { if (this.state.canSwitch()) this.weapon = weapon; }
  stun() { this.state = new StunnedState(); }
  die() { this.state = new DeadState(); }
  attack(target, distance) { if (!this.state.canAttack()) return { success: false, reason: "Player can't attack", manaCost: 0 }; const result = this.weapon.attack(distance, this.mana); if (result.success) { this.mana -= result.manaCost; target.receiveDamage(result.damage, result.damageType); } return result; }
}

export class AttackEventPublisher { constructor() { this.observers = new Set(); } subscribe(observer) { this.observers.add(observer); } publish(event) { this.observers.forEach((observer) => observer.onAttack(event)); } }
export class BattleLog { constructor() { this.events = []; } onAttack(event) { this.events.push(event); } }
export class DamageStatistics { constructor() { this.successfulAttacks = 0; this.totalDamage = 0; } onAttack(event) { if (event.success) { this.successfulAttacks += 1; this.totalDamage += event.damage; } } }

class DistanceHandler { setNext(next) { this.next = next; return next; } handle(request) { if (request.distance < 0) return { success: false, reason: "Distance can't be negative", manaCost: 0 }; return this.next.handle(request); } }
class TargetAliveHandler { setNext(next) { this.next = next; return next; } handle(request) { if (!request.target.isAlive) return { success: false, reason: "Target is already defeated", manaCost: 0 }; return this.next.handle(request); } }
class PerformAttackHandler { handle(request) { return request.player.attack(request.target, request.distance); } }
function createAttackChain() { return new DistanceHandler().setNext(new TargetAliveHandler()).setNext(new PerformAttackHandler()); }

class AttackCommand { constructor(player, target, distance) { this.player = player; this.target = target; this.distance = distance; this.beforeHealth = null; this.beforeMana = null; } execute() { this.beforeHealth = this.target.health; this.beforeMana = this.player.mana; return createAttackChain().handle({ player: this.player, target: this.target, distance: this.distance }); } undo() { if (this.beforeHealth === null) return false; this.target.health = this.beforeHealth; this.player.mana = this.beforeMana; return true; } }
class CommandInvoker { constructor() { this.history = []; } execute(command) { const result = command.execute(); if (result.success) this.history.push(command); return result; } }
export class BattleFlow {
  runTurn(weapon, distance) { this.prepareTurn(); const result = this.performAttack(weapon, distance); this.processResult(result); this.finishTurn(); return result; }
  prepareTurn() {}
  performAttack(_weapon, _distance) { throw new Error("Concrete battle flow must implement performAttack"); }
  processResult(_result) {}
  finishTurn() {}
}
class StandardBattleFlow extends BattleFlow {
  constructor(facade) { super(); this.facade = facade; }
  performAttack(weapon, distance) { return this.facade.executeAttack(weapon, distance); }
}

export class BattleFacade {
  constructor(factory) { this.factory = factory; this.publisher = new AttackEventPublisher(); this.log = new BattleLog(); this.statistics = new DamageStatistics(); this.publisher.subscribe(this.log); this.publisher.subscribe(this.statistics); this.restart(); this.flow = new StandardBattleFlow(this); }
  restart() { this.player = new Player(this.factory); this.dragon = new Dragon(); this.invoker = new CommandInvoker(); }
  get isOver() { return !this.dragon.isAlive; }
  executeAttack(weapon, distance) {
    if (this.isOver) return { success: false, reason: "The Dragon is already defeated", manaCost: 0 };
    this.player.switchWeapon(weapon);
    const result = this.invoker.execute(new AttackCommand(this.player, this.dragon, distance));
    this.publisher.publish({ weapon: this.player.weapon.name, success: result.success, damage: result.damage ?? 0, reason: result.reason });
    return result;
  }
  attack(weapon, distance) { return this.flow.runTurn(weapon, distance); }
  undoLast() { const command = this.invoker.history.pop(); return command ? command.undo() : false; }
}
