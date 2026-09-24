import { BattleFacade, EquipmentFactory, GameSettings } from "./game.js";

const app = document.querySelector("#app");
const settings = new GameSettings();
let theme = settings.theme;
let factory = new EquipmentFactory(theme);
let battle = new BattleFacade(factory);

function render(message = "Choose a weapon and attack.", attackKind = "") {
  app.className = theme;
  const health = battle.dragon.health / battle.dragon.maxHealth * 100;
  const defeated = battle.isOver;
  const status = defeated ? "💀 Dragon defeated! You win!" : message;
  const disabled = defeated ? " disabled" : "";
  app.innerHTML = `<section class="arena"><header><p class="eyebrow">${theme.toUpperCase()} EQUIPMENT</p><h1>Dungeon Arena</h1></header><div class="dragon-panel"><div class="dragon">${defeated ? "☠️" : "🐉"}</div><h2>${defeated ? "Dragon Defeated" : "Dragon"}</h2><div class="bar"><span style="width:${health}%"></span></div><p>${battle.dragon.health} / ${battle.dragon.maxHealth} health</p></div><div class="stats"><span>✨ Mana ${battle.player.mana} / ${battle.player.maxMana}</span><span>⚔️ ${battle.statistics.successfulAttacks} attacks · ${battle.statistics.totalDamage} damage</span><label>Distance <input id="distance" type="number" min="0" value="10"${disabled}></label></div><div class="weapons"><button data-weapon="sword"${disabled}>⚔️ ${factory.createSword().name}</button><button data-weapon="bow"${disabled}>🏹 ${factory.createBow().name}</button><button data-weapon="staff"${disabled}>🔮 ${factory.createStaff().name}</button></div><button id="undo" class="theme"${battle.invoker.history.length ? "" : " disabled"}>Undo last attack</button><button id="theme" class="theme">Switch to ${theme === "fire" ? "Ice" : "Fire"} theme</button><button id="restart" class="theme">Restart battle</button><p id="message" class="message">${status}</p></section>`;
  const scene = document.createElement("div");
  scene.className = `battlefield${message.includes("dealt") ? " attack-animation" : ""}`;
  const effect = attackKind === "sword" ? "⚔️" : attackKind === "bow" ? "➳" : "🔮";
  scene.innerHTML = `<div class="moon"></div><div class="mountains"></div><div class="ground"></div><div class="fighter player">🧙</div><div class="projectile ${attackKind}">${effect}</div><div class="fighter dragon-sprite">${defeated ? "☠️" : "🐉"}</div><div class="impact">💥</div>`;
  document.querySelector(".dragon-panel").before(scene);
  document.querySelectorAll("[data-weapon]").forEach((button) => button.addEventListener("click", () => attack(button.dataset.weapon)));
  document.querySelector("#theme").addEventListener("click", switchTheme);
  document.querySelector("#undo").addEventListener("click", () => { const undone = battle.undoLast(); render(undone ? "Last attack undone." : "Nothing to undo."); });
  document.querySelector("#restart").addEventListener("click", () => { battle.restart(); render("A new Dragon enters the arena."); });
}

function attack(kind) {
  const weapons = { sword: factory.createSword(), bow: factory.createBow(), staff: factory.createStaff() };
  const result = battle.attack(weapons[kind], Number(document.querySelector("#distance").value));
  render(result.success ? `${battle.player.weapon.name} dealt ${result.damage} ${result.damageType} damage!` : `Attack failed: ${result.reason}`, kind);
}

function switchTheme() { theme = theme === "fire" ? "ice" : "fire"; settings.theme = theme; factory = new EquipmentFactory(theme); battle = new BattleFacade(factory); render(); }

render();
