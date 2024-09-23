import org.antlr.v4.runtime.tree.AbstractParseTreeVisitor;

public class EvalVisitor extends LabeledExprBaseVisitor<Double> {

    @Override
    public Double visitStat(LabeledExprParser.StatContext ctx) {
        return visit(ctx.expr()); // Evalúa la expresión en la regla de entrada 'stat'
    }

    @Override
    public Double visitExpr(LabeledExprParser.ExprContext ctx) {
        if (ctx.INT() != null) {
            // Si es un número entero
            return Double.parseDouble(ctx.INT().getText());
        } else if (ctx.ID() != null) {
            // Puedes agregar soporte para identificadores aquí
            throw new UnsupportedOperationException("Variables no soportadas en esta versión");
        } else if (ctx.op != null) {
            // Si hay un operador
            double left = visit(ctx.expr(0));
            double right = visit(ctx.expr(1));

            switch (ctx.op.getType()) {
                case LabeledExprParser.ADD:
                    return left + right;
                case LabeledExprParser.SUB:
                    return left - right;
                case LabeledExprParser.MUL:
                    return left * right;
                case LabeledExprParser.DIV:
                    if (right == 0) {
                        throw new ArithmeticException("División por cero");
                    }
                     return left / right;
                case LabeledExprParser.POW:
                    return Math.pow(left, right);
            }
        } else if (ctx.getChildCount() == 3 && ctx.getChild(0).getText().equals("sqrt") && ctx.getChild(1) instanceof LabeledExprParser.ExprContext) {
            // Función de raíz cuadrada
            double value = visit((LabeledExprParser.ExprContext) ctx.getChild(1));
            if (value < 0) {
                throw new ArithmeticException("Raíz cuadrada de un número negativo");
            }
            return Math.sqrt(value);
        } else if (ctx.expr().size() == 1) {
            // Paréntesis
            return visit(ctx.expr(0));
        }

        return 0.0;
    }
}

