from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentRisk")


@_attrs_define
class PaymentRisk:
    """Additional information about the payment that may be used for risk scoring

    Attributes:
        context_type (Union[Unset, str]): __Optional__. The payment context code. Allowed values are [BILL_IN_ADVANCE,
            BILL_IN_ARREARS, ECOMMERCE_MERCHANT, FACE_TO_FACE_POS, TRANSFER_TO_SELF,TRANSFER_TO_THIRD_PARTY, PISP_PAYEE ].
    """

    context_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_type = self.context_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_type is not UNSET:
            field_dict["contextType"] = context_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_type = d.pop("contextType", UNSET)

        payment_risk = cls(
            context_type=context_type,
        )

        payment_risk.additional_properties = d
        return payment_risk

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
