import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class TrigCalculator {

    public static void main(String[] args) throws IOException {
        // Leer el archivo expr.in
        try (Scanner scanner = new Scanner(new FileInputStream("expr.in"))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine().trim();
                if (!line.isEmpty()) {
                    // Crear un input stream para ANTLR
                    CharStream input = CharStreams.fromString(line);

                    // Crear el lexer y el parser
                    TrigLexer lexer = new TrigLexer(input);
                    CommonTokenStream tokens = new CommonTokenStream(lexer);
                    TrigParser parser = new TrigParser(tokens);

                    // Parsear la expresión
                    ParseTree tree = parser.parse();

                    // Evaluar la expresión
                    double result = evaluate(tree);
                    System.out.println(result);
                }
            }
        }
    }

    private static double evaluate(ParseTree tree) {
        if (tree instanceof TrigParser.ExprContext) {
            TrigParser.ExprContext ctx = (TrigParser.ExprContext) tree;
            String func = ctx.function().getText();
            double angle = Double.parseDouble(ctx.number().getText());

            // Convertir grados a radianes
            double radians = Math.toRadians(angle);

            switch (func) {
                case "Sin":
                    return Math.sin(radians);
                case "Cos":
                    return Math.cos(radians);
                case "Tan":
                    return Math.tan(radians);
                default:
                    throw new IllegalArgumentException("Unknown function: " + func);
            }
        }
        throw new IllegalArgumentException("Invalid parse tree");
    }
}

