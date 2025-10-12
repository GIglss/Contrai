from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.schema_type import SchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_defs import SchemaDefs
    from ..models.schema_dependent_required import SchemaDependentRequired
    from ..models.schema_properties import SchemaProperties
    from ..models.schema_x_yapily_annotations import SchemaXYapilyAnnotations
    from ..models.schema_x_yapily_validations import SchemaXYapilyValidations


T = TypeVar("T", bound="Schema")


@_attrs_define
class Schema:
    """
    Attributes:
        title (Union[Unset, str]):
        maximum (Union[Unset, float]):
        exclusive_maximum (Union[Unset, float]):
        minimum (Union[Unset, float]):
        exclusive_minimum (Union[Unset, float]):
        pattern (Union[Unset, str]):
        max_items (Union[Unset, int]):
        min_items (Union[Unset, int]):
        unique_items (Union[Unset, bool]):
        required (Union[Unset, list[str]]):
        enum (Union[Unset, list[Any]]):
        type_ (Union[Unset, SchemaType]):
        contains (Union[Unset, Schema]):
        not_ (Union[Unset, Schema]):
        if_ (Union[Unset, Schema]):
        then (Union[Unset, Schema]):
        else_ (Union[Unset, Schema]):
        all_of (Union[Unset, list['Schema']]):
        one_of (Union[Unset, list['Schema']]):
        any_of (Union[Unset, list['Schema']]):
        items (Union[Unset, Schema]):
        properties (Union[Unset, SchemaProperties]):
        description (Union[Unset, str]):
        format_ (Union[Unset, str]):
        default (Union[Unset, Any]):
        example (Union[Unset, Any]):
        dependent_required (Union[Unset, SchemaDependentRequired]): dependentRequired keyword is used to satisfy
            dependency between fields
        defs (Union[Unset, SchemaDefs]):
        ref (Union[Unset, str]):
        x_yapily_annotations (Union[Unset, SchemaXYapilyAnnotations]):
        x_yapily_validations (Union[Unset, SchemaXYapilyValidations]):
    """

    title: Union[Unset, str] = UNSET
    maximum: Union[Unset, float] = UNSET
    exclusive_maximum: Union[Unset, float] = UNSET
    minimum: Union[Unset, float] = UNSET
    exclusive_minimum: Union[Unset, float] = UNSET
    pattern: Union[Unset, str] = UNSET
    max_items: Union[Unset, int] = UNSET
    min_items: Union[Unset, int] = UNSET
    unique_items: Union[Unset, bool] = UNSET
    required: Union[Unset, list[str]] = UNSET
    enum: Union[Unset, list[Any]] = UNSET
    type_: Union[Unset, SchemaType] = UNSET
    contains: Union[Unset, "Schema"] = UNSET
    not_: Union[Unset, "Schema"] = UNSET
    if_: Union[Unset, "Schema"] = UNSET
    then: Union[Unset, "Schema"] = UNSET
    else_: Union[Unset, "Schema"] = UNSET
    all_of: Union[Unset, list["Schema"]] = UNSET
    one_of: Union[Unset, list["Schema"]] = UNSET
    any_of: Union[Unset, list["Schema"]] = UNSET
    items: Union[Unset, "Schema"] = UNSET
    properties: Union[Unset, "SchemaProperties"] = UNSET
    description: Union[Unset, str] = UNSET
    format_: Union[Unset, str] = UNSET
    default: Union[Unset, Any] = UNSET
    example: Union[Unset, Any] = UNSET
    dependent_required: Union[Unset, "SchemaDependentRequired"] = UNSET
    defs: Union[Unset, "SchemaDefs"] = UNSET
    ref: Union[Unset, str] = UNSET
    x_yapily_annotations: Union[Unset, "SchemaXYapilyAnnotations"] = UNSET
    x_yapily_validations: Union[Unset, "SchemaXYapilyValidations"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        maximum = self.maximum

        exclusive_maximum = self.exclusive_maximum

        minimum = self.minimum

        exclusive_minimum = self.exclusive_minimum

        pattern = self.pattern

        max_items = self.max_items

        min_items = self.min_items

        unique_items = self.unique_items

        required: Union[Unset, list[str]] = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        enum: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        contains: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contains, Unset):
            contains = self.contains.to_dict()

        not_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.not_, Unset):
            not_ = self.not_.to_dict()

        if_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.if_, Unset):
            if_ = self.if_.to_dict()

        then: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.then, Unset):
            then = self.then.to_dict()

        else_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.else_, Unset):
            else_ = self.else_.to_dict()

        all_of: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.all_of, Unset):
            all_of = []
            for all_of_item_data in self.all_of:
                all_of_item = all_of_item_data.to_dict()
                all_of.append(all_of_item)

        one_of: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.one_of, Unset):
            one_of = []
            for one_of_item_data in self.one_of:
                one_of_item = one_of_item_data.to_dict()
                one_of.append(one_of_item)

        any_of: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.any_of, Unset):
            any_of = []
            for any_of_item_data in self.any_of:
                any_of_item = any_of_item_data.to_dict()
                any_of.append(any_of_item)

        items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        description = self.description

        format_ = self.format_

        default = self.default

        example = self.example

        dependent_required: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dependent_required, Unset):
            dependent_required = self.dependent_required.to_dict()

        defs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defs, Unset):
            defs = self.defs.to_dict()

        ref = self.ref

        x_yapily_annotations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.x_yapily_annotations, Unset):
            x_yapily_annotations = self.x_yapily_annotations.to_dict()

        x_yapily_validations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.x_yapily_validations, Unset):
            x_yapily_validations = self.x_yapily_validations.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if exclusive_maximum is not UNSET:
            field_dict["exclusiveMaximum"] = exclusive_maximum
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if exclusive_minimum is not UNSET:
            field_dict["exclusiveMinimum"] = exclusive_minimum
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if min_items is not UNSET:
            field_dict["minItems"] = min_items
        if unique_items is not UNSET:
            field_dict["uniqueItems"] = unique_items
        if required is not UNSET:
            field_dict["required"] = required
        if enum is not UNSET:
            field_dict["enum"] = enum
        if type_ is not UNSET:
            field_dict["type"] = type_
        if contains is not UNSET:
            field_dict["contains"] = contains
        if not_ is not UNSET:
            field_dict["not"] = not_
        if if_ is not UNSET:
            field_dict["if"] = if_
        if then is not UNSET:
            field_dict["then"] = then
        if else_ is not UNSET:
            field_dict["else"] = else_
        if all_of is not UNSET:
            field_dict["allOf"] = all_of
        if one_of is not UNSET:
            field_dict["oneOf"] = one_of
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of
        if items is not UNSET:
            field_dict["items"] = items
        if properties is not UNSET:
            field_dict["properties"] = properties
        if description is not UNSET:
            field_dict["description"] = description
        if format_ is not UNSET:
            field_dict["format"] = format_
        if default is not UNSET:
            field_dict["default"] = default
        if example is not UNSET:
            field_dict["example"] = example
        if dependent_required is not UNSET:
            field_dict["dependentRequired"] = dependent_required
        if defs is not UNSET:
            field_dict["$defs"] = defs
        if ref is not UNSET:
            field_dict["$ref"] = ref
        if x_yapily_annotations is not UNSET:
            field_dict["x-yapily-annotations"] = x_yapily_annotations
        if x_yapily_validations is not UNSET:
            field_dict["x-yapily-validations"] = x_yapily_validations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_defs import SchemaDefs
        from ..models.schema_dependent_required import SchemaDependentRequired
        from ..models.schema_properties import SchemaProperties
        from ..models.schema_x_yapily_annotations import SchemaXYapilyAnnotations
        from ..models.schema_x_yapily_validations import SchemaXYapilyValidations

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        maximum = d.pop("maximum", UNSET)

        exclusive_maximum = d.pop("exclusiveMaximum", UNSET)

        minimum = d.pop("minimum", UNSET)

        exclusive_minimum = d.pop("exclusiveMinimum", UNSET)

        pattern = d.pop("pattern", UNSET)

        max_items = d.pop("maxItems", UNSET)

        min_items = d.pop("minItems", UNSET)

        unique_items = d.pop("uniqueItems", UNSET)

        required = cast(list[str], d.pop("required", UNSET))

        enum = cast(list[Any], d.pop("enum", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SchemaType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SchemaType(_type_)

        _contains = d.pop("contains", UNSET)
        contains: Union[Unset, Schema]
        if isinstance(_contains, Unset):
            contains = UNSET
        else:
            contains = Schema.from_dict(_contains)

        _not_ = d.pop("not", UNSET)
        not_: Union[Unset, Schema]
        if isinstance(_not_, Unset):
            not_ = UNSET
        else:
            not_ = Schema.from_dict(_not_)

        _if_ = d.pop("if", UNSET)
        if_: Union[Unset, Schema]
        if isinstance(_if_, Unset):
            if_ = UNSET
        else:
            if_ = Schema.from_dict(_if_)

        _then = d.pop("then", UNSET)
        then: Union[Unset, Schema]
        if isinstance(_then, Unset):
            then = UNSET
        else:
            then = Schema.from_dict(_then)

        _else_ = d.pop("else", UNSET)
        else_: Union[Unset, Schema]
        if isinstance(_else_, Unset):
            else_ = UNSET
        else:
            else_ = Schema.from_dict(_else_)

        all_of = []
        _all_of = d.pop("allOf", UNSET)
        for all_of_item_data in _all_of or []:
            all_of_item = Schema.from_dict(all_of_item_data)

            all_of.append(all_of_item)

        one_of = []
        _one_of = d.pop("oneOf", UNSET)
        for one_of_item_data in _one_of or []:
            one_of_item = Schema.from_dict(one_of_item_data)

            one_of.append(one_of_item)

        any_of = []
        _any_of = d.pop("anyOf", UNSET)
        for any_of_item_data in _any_of or []:
            any_of_item = Schema.from_dict(any_of_item_data)

            any_of.append(any_of_item)

        _items = d.pop("items", UNSET)
        items: Union[Unset, Schema]
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = Schema.from_dict(_items)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, SchemaProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = SchemaProperties.from_dict(_properties)

        description = d.pop("description", UNSET)

        format_ = d.pop("format", UNSET)

        default = d.pop("default", UNSET)

        example = d.pop("example", UNSET)

        _dependent_required = d.pop("dependentRequired", UNSET)
        dependent_required: Union[Unset, SchemaDependentRequired]
        if isinstance(_dependent_required, Unset):
            dependent_required = UNSET
        else:
            dependent_required = SchemaDependentRequired.from_dict(_dependent_required)

        _defs = d.pop("$defs", UNSET)
        defs: Union[Unset, SchemaDefs]
        if isinstance(_defs, Unset):
            defs = UNSET
        else:
            defs = SchemaDefs.from_dict(_defs)

        ref = d.pop("$ref", UNSET)

        _x_yapily_annotations = d.pop("x-yapily-annotations", UNSET)
        x_yapily_annotations: Union[Unset, SchemaXYapilyAnnotations]
        if isinstance(_x_yapily_annotations, Unset):
            x_yapily_annotations = UNSET
        else:
            x_yapily_annotations = SchemaXYapilyAnnotations.from_dict(_x_yapily_annotations)

        _x_yapily_validations = d.pop("x-yapily-validations", UNSET)
        x_yapily_validations: Union[Unset, SchemaXYapilyValidations]
        if isinstance(_x_yapily_validations, Unset):
            x_yapily_validations = UNSET
        else:
            x_yapily_validations = SchemaXYapilyValidations.from_dict(_x_yapily_validations)

        schema = cls(
            title=title,
            maximum=maximum,
            exclusive_maximum=exclusive_maximum,
            minimum=minimum,
            exclusive_minimum=exclusive_minimum,
            pattern=pattern,
            max_items=max_items,
            min_items=min_items,
            unique_items=unique_items,
            required=required,
            enum=enum,
            type_=type_,
            contains=contains,
            not_=not_,
            if_=if_,
            then=then,
            else_=else_,
            all_of=all_of,
            one_of=one_of,
            any_of=any_of,
            items=items,
            properties=properties,
            description=description,
            format_=format_,
            default=default,
            example=example,
            dependent_required=dependent_required,
            defs=defs,
            ref=ref,
            x_yapily_annotations=x_yapily_annotations,
            x_yapily_validations=x_yapily_validations,
        )

        return schema
