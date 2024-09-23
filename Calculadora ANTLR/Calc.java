import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Calc {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        while (true) {
            System.out.println("Ingrese una expresión (o 'salir' para terminar):");
            String inputString = reader.readLine();
            
            if (inputString.equalsIgnoreCase("salir")) {
                break;
            }
            
            CharStream input = CharStreams.fromString(inputString);
            LabeledExprLexer lexer = new LabeledExprLexer(input);
            CommonTokenStream tokens = new CommonTokenStream(lexer);
            LabeledExprParser parser = new LabeledExprParser(tokens);

            ParseTree tree = parser.stat(); // Usa 'stat' como la regla de entrada principal
            System.out.println("Árbol de sintaxis: " + tree.toStringTree(parser));

            EvalVisitor eval = new EvalVisitor();

            try {
                Double result = eval.visit(tree); // Llama al visitante para evaluar la expresión
                System.out.println("Resultado: " + result);
            } catch (Exception e) {
                System.out.println("Error en la expresión: " + e.getMessage());
            }
        }
    }
}

