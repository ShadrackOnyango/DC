import typing
from collections import OrderedDict
from typing import Any, Callable, Mapping, NoReturn

from parsimonious.expressions import _CALLABLE_TYPE, Expression, Literal, Lookahead, Not, OneOf, Regex, Sequence, TokenMatcher
from parsimonious.nodes import Node, NodeVisitor

class Grammar(OrderedDict[str, Expression]):
    default_rule: Expression | Any
    def __init__(self, rules: str = ..., **more_rules: Expression | _CALLABLE_TYPE) -> None: ...
    def default(self, rule_name: str) -> Grammar: ...
    def parse(self, text: str, pos: int = ...) -> Node: ...
    def match(self, text: str, pos: int = ...) -> Node: ...

class TokenGrammar(Grammar): ...
class BootstrappingGrammar(Grammar): ...

rule_syntax: str

class LazyReference(str):
    name: str

class RuleVisitor(NodeVisitor):
    quantifier_classes: dict[str, type[Expression]]
    visit_expression: Callable[[RuleVisitor, Node, typing.Sequence[Any]], Any]
    visit_term: Callable[[RuleVisitor, Node, typing.Sequence[Any]], Any]
    visit_atom: Callable[[RuleVisitor, Node, typing.Sequence[Any]], Any]
    custom_rules: dict[str, Expression]
    def __init__(self, custom_rules: Mapping[str, Expression] | None = ...) -> None: ...
    def visit_rules(
        self, node: Node, rules_list: typing.Sequence[Any]
    ) -> tuple[OrderedDict[str, Expression], Expression | None]: ...
    def visit_rule(self, node: Node, rule: typing.Sequence[Any]) -> Expression: ...
    def visit_label(self, node: Node, label: typing.Sequence[Any]) -> str: ...
    def visit_ored(self, node: Node, ored: typing.Sequence[Any]) -> OneOf: ...
    def visit_or_term(self, node: Node, or_term: typing.Sequence[Any]) -> Expression: ...
    def visit_sequence(self, node: Node, sequence: typing.Sequence[Any]) -> Sequence: ...
    def visit_not_term(self, node: Node, not_term: typing.Sequence[Any]) -> Not: ...
    def visit_lookahead_term(self, node: Node, lookahead_term: typing.Sequence[Any]) -> Lookahead: ...
    def visit_quantified(self, node: Node, quantified: typing.Sequence[Any]) -> Expression: ...
    def visit_quantifier(self, node: Node, quantifier: typing.Sequence[Any]) -> Node: ...
    def visit_reference(self, node: Node, reference: typing.Sequence[Any]) -> LazyReference: ...
    def visit_literal(self, node: Node, literal: typing.Sequence[Any]) -> Literal: ...
    def visit_spaceless_literal(self, spaceless_literal: Node, visited_children: typing.Sequence[Any]) -> Literal: ...
    def visit_regex(self, node: Node, regex: typing.Sequence[Any]) -> Regex: ...
    def visit_parenthesized(self, node: Node, parenthesized: typing.Sequence[Any]) -> Expression: ...
    def generic_visit(self, node: Node, visited_children: typing.Sequence[Any]) -> typing.Sequence[Any] | Node: ...  # type: ignore

class TokenRuleVisitor(RuleVisitor):
    def visit_spaceless_literal(self, spaceless_literal: Node, visited_children: typing.Sequence[Any]) -> TokenMatcher: ...
    def visit_regex(self, node: Node, regex: typing.Sequence[Any]) -> NoReturn: ...

rule_grammar: Grammar
