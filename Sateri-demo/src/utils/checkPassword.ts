// checkPassword.ts
export function checkPassword(inputPassword: string): boolean {
  const correctPassword = '45DA-YSBE-FORE';
	const formattedInput = inputPassword.replace(/[\s-]/g, "").toLowerCase();
	const formattedCorrectPassword = correctPassword.replace(/[\s-]/g, "").toLowerCase();
	return formattedInput === formattedCorrectPassword;
}