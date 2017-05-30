public class Collatz {
	public static void main(String[] args) {
		int arg = Integer.parseInt(args[0]);

		while (arg != 1) {
			if (arg % 2 == 0) {
				arg = arg / 2;
			} else {
				arg = 3 * arg + 1;
			}

			System.out.println("Arg = " + arg);
		}
	}
}