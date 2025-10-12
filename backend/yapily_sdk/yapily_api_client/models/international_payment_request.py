from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.charge_bearer_type import ChargeBearerType
from ..models.priority_code_enum import PriorityCodeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchange_rate_information import ExchangeRateInformation


T = TypeVar("T", bound="InternationalPaymentRequest")


@_attrs_define
class InternationalPaymentRequest:
    """__Conditional__. Used to specify properties to define an international payment. <br><br>Must be specified when the
    payment `type` is one of the following:<ul>     <li><code>INTERNATIONAL_SINGLE_PAYMENT</code></li>
    <li><code>INTERNATIONAL_SCHEDULED_PAYMENT</code></li>     <li><code>INTERNATIONAL_PERIODIC_PAYMENT</code></li></ul>

        Attributes:
            currency_of_transfer (str): __Mandatory__. The currency to be transferred to the payee. This may differ from the
                currency the payment is denoted in and the currency of the payer's account. Specified as a 3-letter code (ISO
                4217).
            exchange_rate_information (Union[Unset, ExchangeRateInformation]): __Optional__. Used to provide details on the
                currency exchange rate and contract.
            purpose (Union[Unset, str]): __Optional__. Used to indicate the external purpose as a [ISO20022 purpose
                code](https://www.rba.hr/documents/20182/183267/External+purpose+codes+list/8a28f888-1f83-5e29-d6ed-
                fce05f428689?version=1.1) value.
            priority (Union[Unset, PriorityCodeEnum]):
            charge_bearer (Union[Unset, ChargeBearerType]): __Conditional__. Depending on the bank and payment type for
                international Euro payments. The field ChargeBearer specifies which party/parties will bear the charges
                associated with the processing of the payment transaction. Valid values are:<ul><li>`DEBT` - All transaction
                charges are to be borne by the debtor.</li><li>`CRED` - All transaction charges are to be borne by the
                creditor.</li><li>`SHAR` - In a credit transfer context, means that transaction charges on the sender side are
                to be borne by the debtor, transaction charges on the receiver side are to be borne by the
                creditor</li><li>`SLEV` - Charges are to be applied following the rules agreed in the service level and/or
                scheme.</li></ul>
    """

    currency_of_transfer: str
    exchange_rate_information: Union[Unset, "ExchangeRateInformation"] = UNSET
    purpose: Union[Unset, str] = UNSET
    priority: Union[Unset, PriorityCodeEnum] = UNSET
    charge_bearer: Union[Unset, ChargeBearerType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_of_transfer = self.currency_of_transfer

        exchange_rate_information: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exchange_rate_information, Unset):
            exchange_rate_information = self.exchange_rate_information.to_dict()

        purpose = self.purpose

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        charge_bearer: Union[Unset, str] = UNSET
        if not isinstance(self.charge_bearer, Unset):
            charge_bearer = self.charge_bearer.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currencyOfTransfer": currency_of_transfer,
            }
        )
        if exchange_rate_information is not UNSET:
            field_dict["exchangeRateInformation"] = exchange_rate_information
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if priority is not UNSET:
            field_dict["priority"] = priority
        if charge_bearer is not UNSET:
            field_dict["chargeBearer"] = charge_bearer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_rate_information import ExchangeRateInformation

        d = dict(src_dict)
        currency_of_transfer = d.pop("currencyOfTransfer")

        _exchange_rate_information = d.pop("exchangeRateInformation", UNSET)
        exchange_rate_information: Union[Unset, ExchangeRateInformation]
        if isinstance(_exchange_rate_information, Unset):
            exchange_rate_information = UNSET
        else:
            exchange_rate_information = ExchangeRateInformation.from_dict(_exchange_rate_information)

        purpose = d.pop("purpose", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, PriorityCodeEnum]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = PriorityCodeEnum(_priority)

        _charge_bearer = d.pop("chargeBearer", UNSET)
        charge_bearer: Union[Unset, ChargeBearerType]
        if isinstance(_charge_bearer, Unset):
            charge_bearer = UNSET
        else:
            charge_bearer = ChargeBearerType(_charge_bearer)

        international_payment_request = cls(
            currency_of_transfer=currency_of_transfer,
            exchange_rate_information=exchange_rate_information,
            purpose=purpose,
            priority=priority,
            charge_bearer=charge_bearer,
        )

        international_payment_request.additional_properties = d
        return international_payment_request

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
