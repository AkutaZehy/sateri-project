export function flipCoin(): number {
  const random = Math.random();
  return random < 0.5 ? 0 : 1;
}