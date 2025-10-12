from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credentials_type import CredentialsType
from ..models.environment_type import EnvironmentType
from ..models.feature_enum import FeatureEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.country import Country
    from ..models.media import Media


T = TypeVar("T", bound="Institution")


@_attrs_define
class Institution:
    """Typically, a bank or business unit within a bank e.g. (AIB Business, AIB Ireland, AIB UK).

    Attributes:
        id (Union[Unset, str]): Unique identifier for the `Institution`.
        name (Union[Unset, str]): The friendly name of the `Institution`.
        full_name (Union[Unset, str]): The full name of the `Institution`.
        countries (Union[Unset, list['Country']]): An array of `Country` denoting which regions the `Institution`
            provides coverage for
        environment_type (Union[Unset, EnvironmentType]): The environment type. <br><br>See [Institution
            Configuration](https://docs.yapily.com/pages/key-concepts/institutions/#configuration) for more information
        credentials_type (Union[Unset, CredentialsType]): The type of credentials required to register the `Institution`
        media (Union[Unset, list['Media']]): Contains links to the logo and the icons for the `Institution`
        features (Union[Unset, list[FeatureEnum]]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    countries: Union[Unset, list["Country"]] = UNSET
    environment_type: Union[Unset, EnvironmentType] = UNSET
    credentials_type: Union[Unset, CredentialsType] = UNSET
    media: Union[Unset, list["Media"]] = UNSET
    features: Union[Unset, list[FeatureEnum]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        full_name = self.full_name

        countries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = []
            for countries_item_data in self.countries:
                countries_item = countries_item_data.to_dict()
                countries.append(countries_item)

        environment_type: Union[Unset, str] = UNSET
        if not isinstance(self.environment_type, Unset):
            environment_type = self.environment_type.value

        credentials_type: Union[Unset, str] = UNSET
        if not isinstance(self.credentials_type, Unset):
            credentials_type = self.credentials_type.value

        media: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        features: Union[Unset, list[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value
                features.append(features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if countries is not UNSET:
            field_dict["countries"] = countries
        if environment_type is not UNSET:
            field_dict["environmentType"] = environment_type
        if credentials_type is not UNSET:
            field_dict["credentialsType"] = credentials_type
        if media is not UNSET:
            field_dict["media"] = media
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.country import Country
        from ..models.media import Media

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        full_name = d.pop("fullName", UNSET)

        countries = []
        _countries = d.pop("countries", UNSET)
        for countries_item_data in _countries or []:
            countries_item = Country.from_dict(countries_item_data)

            countries.append(countries_item)

        _environment_type = d.pop("environmentType", UNSET)
        environment_type: Union[Unset, EnvironmentType]
        if isinstance(_environment_type, Unset):
            environment_type = UNSET
        else:
            environment_type = EnvironmentType(_environment_type)

        _credentials_type = d.pop("credentialsType", UNSET)
        credentials_type: Union[Unset, CredentialsType]
        if isinstance(_credentials_type, Unset):
            credentials_type = UNSET
        else:
            credentials_type = CredentialsType(_credentials_type)

        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = Media.from_dict(media_item_data)

            media.append(media_item)

        features = []
        _features = d.pop("features", UNSET)
        for features_item_data in _features or []:
            features_item = FeatureEnum(features_item_data)

            features.append(features_item)

        institution = cls(
            id=id,
            name=name,
            full_name=full_name,
            countries=countries,
            environment_type=environment_type,
            credentials_type=credentials_type,
            media=media,
            features=features,
        )

        institution.additional_properties = d
        return institution

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
