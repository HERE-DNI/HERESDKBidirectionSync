---
title: "Search  Reference"
slug: "sdk-for-ios-navigate-search"
---

# Search

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk7AddressV"></span>` `<span id="//apple_ref/swift/Struct/Address" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk7AddressV" class="token"><code>Address</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Information about the address of a location.

  Used in <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC7addressAA7AddressVvp">`Place.address`</a>.

  Note that while `OfflineSearchEngine.suggest` and `OfflineSearchEngine.suggestByText` set all available details, `SearchEngine.suggest` and `SearchEngine.suggestByText` set only <a href="sdk-for-ios-navigate-structs-address#/s:7heresdk7AddressV11addressTextSSvp">`Address.addressText`</a>. Complete address details can be obtained by searching with <a href="sdk-for-ios-navigate-structs-placeidquery">`PlaceIdQuery`</a>.

  <a href="sdk-for-ios-navigate-structs-address" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Address : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11AddressTypeO"></span>` `<span id="//apple_ref/swift/Enum/AddressType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk11AddressTypeO" class="token"><code>AddressType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Address type

  <a href="sdk-for-ios-navigate-enums-addresstype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum AddressType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12AddressQueryV"></span>` `<span id="//apple_ref/swift/Struct/AddressQuery" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12AddressQueryV" class="token"><code>AddressQuery</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options to specify an address query. A <a href="sdk-for-ios-navigate-structs-addressquery#/s:7heresdk12AddressQueryV5querySSvp">`AddressQuery.query`</a> can consist of parts of an address or full addresses, optionally comma separated. `AddressQuery` should only be used to search for parts of the address, excluding the POI name. For example, “Invalidenstraße 116, Berlin, Germany” is appropriate, whereas “HERE, Invalidenstraße 116, Berlin, Germany” is not. To be able to include the POI name, use <a href="sdk-for-ios-navigate-structs-textquery">`TextQuery`</a> instead. <a href="sdk-for-ios-navigate-structs-searchoptions#/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp">`SearchOptions.languageCode`</a> specifies the language of the <a href="sdk-for-ios-navigate-structs-addressquery#/s:7heresdk12AddressQueryV5querySSvp">`AddressQuery.query`</a> and determines the preferred language of the results.

  <a href="sdk-for-ios-navigate-structs-addressquery" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AddressQuery : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8AreaTypeO"></span>` `<span id="//apple_ref/swift/Enum/AreaType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk8AreaTypeO" class="token"><code>AreaType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a type of area like country, state, city, county, etc.

  <a href="sdk-for-ios-navigate-enums-areatype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum AreaType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15BusinessDetailsV"></span>` `<span id="//apple_ref/swift/Struct/BusinessDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15BusinessDetailsV" class="token"><code>BusinessDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains place details such as contacts, opening hours and some electro vehicle info.

  <a href="sdk-for-ios-navigate-structs-businessdetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct BusinessDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV"></span>` `<span id="//apple_ref/swift/Struct/CategoryQuery" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13CategoryQueryV" class="token"><code>CategoryQuery</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options to specify a query by categories.

  <a href="sdk-for-ios-navigate-structs-categoryquery" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CategoryQuery : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7ContactV"></span>` `<span id="//apple_ref/swift/Struct/Contact" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk7ContactV" class="token"><code>Contact</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents contact information.

  <a href="sdk-for-ios-navigate-structs-contact" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Contact : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9DateRangeV"></span>` `<span id="//apple_ref/swift/Struct/DateRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9DateRangeV" class="token"><code>DateRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the date range when the tariff element is valid. This is typically used to indicate seasonal tariffs or to announce an update to the tariff in advance. It may also be used to indicate spot prices, together with time period. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-daterange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DateRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9DayOfWeekO"></span>` `<span id="//apple_ref/swift/Enum/DayOfWeek" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9DayOfWeekO" class="token"><code>DayOfWeek</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the day of the week. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-dayofweek" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DayOfWeek : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7DetailsV"></span>` `<span id="//apple_ref/swift/Struct/Details" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk7DetailsV" class="token"><code>Details</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains details of a specific place, such as contact information, opening hours and assigned categories.

  <a href="sdk-for-ios-navigate-structs-details" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Details : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12EmailAddressV"></span>` `<span id="//apple_ref/swift/Struct/EmailAddress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12EmailAddressV" class="token"><code>EmailAddress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents data related to specific email address.

  <a href="sdk-for-ios-navigate-structs-emailaddress" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EmailAddress : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EMobilityServiceProviderV"></span>` `<span id="//apple_ref/swift/Struct/EMobilityServiceProvider" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk24EMobilityServiceProviderV" class="token"><code>EMobilityServiceProvider</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  eMSP (e-Mobility Service Provider) for which the EV station operator has EV roaming agreements. It is only available for online search.

  <a href="sdk-for-ios-navigate-structs-emobilityserviceprovider" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EMobilityServiceProvider : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9EnergyMixV"></span>` `<span id="//apple_ref/swift/Struct/EnergyMix" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9EnergyMixV" class="token"><code>EnergyMix</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents details on the energy supplied at the charging location. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-energymix" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EnergyMix : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12EnergySourceV"></span>` `<span id="//apple_ref/swift/Struct/EnergySource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12EnergySourceV" class="token"><code>EnergySource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Energy source of EV charging point. EnergyMix contains a list of this representing the energy sources. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-energysource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EnergySource : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16EnergySourceTypeO"></span>` `<span id="//apple_ref/swift/Enum/EnergySourceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk16EnergySourceTypeO" class="token"><code>EnergySourceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents energy source type. EnergySource contains this representing the type of the energy source. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-energysourcetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EnergySourceType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19EnvironmentalImpactV"></span>` `<span id="//apple_ref/swift/Struct/EnvironmentalImpact" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk19EnvironmentalImpactV" class="token"><code>EnvironmentalImpact</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents environmental impact for an environmental impact category. EnergyMix contains an list of this representing the environmental impacts of different categories. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-environmentalimpact" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EnvironmentalImpact : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27EnvironmentalImpactCategoryO"></span>` `<span id="//apple_ref/swift/Enum/EnvironmentalImpactCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk27EnvironmentalImpactCategoryO" class="token"><code>EnvironmentalImpactCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents environmental impacts category of the environmental impact for energy mix. EnvironmentalImpact contains this representing the category of the environmental impact. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-environmentalimpactcategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EnvironmentalImpactCategory : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25EVAccessRestrictionReasonO"></span>` `<span id="//apple_ref/swift/Enum/EVAccessRestrictionReason" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk25EVAccessRestrictionReasonO" class="token"><code>EVAccessRestrictionReason</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the restriction reason of an <a href="sdk-for-ios-navigate-structs-evchargingpool">`EVChargingPool`</a>.

  <a href="sdk-for-ios-navigate-enums-evaccessrestrictionreason" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVAccessRestrictionReason : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12EVAccessTypeO"></span>` `<span id="//apple_ref/swift/Enum/EVAccessType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12EVAccessTypeO" class="token"><code>EVAccessType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the accessibility level of an <a href="sdk-for-ios-navigate-structs-evchargingpool">`EVChargingPool`</a>.

  <a href="sdk-for-ios-navigate-enums-evaccesstype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVAccessType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19EVChargingConnectorV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingConnector" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk19EVChargingConnectorV" class="token"><code>EVChargingConnector</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a connector at the charging point. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingconnector" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingConnector : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EVChargingConnectorGroupV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingConnectorGroup" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk24EVChargingConnectorGroupV" class="token"><code>EVChargingConnectorGroup</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the connector group at the charging location. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingconnectorgroup" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingConnectorGroup : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28EVChargingConnectorReferenceV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingConnectorReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk28EVChargingConnectorReferenceV" class="token"><code>EVChargingConnectorReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a pairing of an EVSE and its connector(s) that belong to a group. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingconnectorreference" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingConnectorReference : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23EVChargingDurationRangeV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingDurationRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk23EVChargingDurationRangeV" class="token"><code>EVChargingDurationRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Duration of the charging session when the tariff element is valid, in seconds. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingdurationrange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingDurationRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVChargingLocationC"></span>` `<span id="//apple_ref/swift/Class/EVChargingLocation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk18EVChargingLocationC" class="token"><code>EVChargingLocation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An electric vehicle (EV) charging location.

  The semantics generally follow the OCPI 2.2.1 standard.

  Known EV-specific acronyms:

  - EV: Electric Vehicle
  - OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, <https://evroaming.org/>)
  - CPO: Charge Point Operator (company that runs the EV charging location)
  - eMSP: e-Mobility Service Provider (customer-facing company)
  - EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)

  A charging location includes a collection of one or more EV supply equipment (EVSE) instances. Typically, the charging location is the exact location of the group of EVSEs, simplified to a single point, but it can also be the entrance of a parking structure which contains these EVSEs. Each EVSE supports more precise position, where applicable.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-evcharginglocation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class EVChargingLocation
  ```

  ``` highlight
  extension EVChargingLocation: NativeBase
  ```

  ``` highlight
  extension EVChargingLocation: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25EVChargingLocationFeatureO"></span>` `<span id="//apple_ref/swift/Enum/EVChargingLocationFeature" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk25EVChargingLocationFeatureO" class="token"><code>EVChargingLocationFeature</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional features that can be requested for EV charging locations. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evcharginglocationfeature" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVChargingLocationFeature : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22EVChargingOpeningHoursV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingOpeningHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk22EVChargingOpeningHoursV" class="token"><code>EVChargingOpeningHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the times when the EVSEs at the charging location can be accessed for charging. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingopeninghours" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingOpeningHours : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31EVChargingOpeningHoursExceptionV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingOpeningHoursException" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk31EVChargingOpeningHoursExceptionV" class="token"><code>EVChargingOpeningHoursException</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents exceptions to the regular opening hours schedule for EV charging locations, such as special closures or extended hours. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingopeninghoursexception" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingOpeningHoursException : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30EVChargingOpeningHoursScheduleV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingOpeningHoursSchedule" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk30EVChargingOpeningHoursScheduleV" class="token"><code>EVChargingOpeningHoursSchedule</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Opening hours schedule for EV charging locations, represented by a list of days of the week during which the location is open in the given time periods. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingopeninghoursschedule" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingOpeningHoursSchedule : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18EVChargingOperatorV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingOperator" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk18EVChargingOperatorV" class="token"><code>EVChargingOperator</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents name and optionally other details about operator, suboperator, or e-Mobility service provider. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingoperator" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingOperator : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21EVChargingPoolDetailsV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingPoolDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk21EVChargingPoolDetailsV" class="token"><code>EVChargingPoolDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Electric vehicle charging pool details.

  <a href="sdk-for-ios-navigate-structs-evchargingpooldetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingPoolDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16EVChargingTariffV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingTariff" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk16EVChargingTariffV" class="token"><code>EVChargingTariff</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tariffs provide detailed pricing information for charging electric vehicles at a specific location. Each tariff describes how costs are calculated based on various factors such as energy consumed, time spent charging, and session duration. Tariffs are typically associated with specific connectors or connector groups, and are only included in the response when relevant data is available and requested. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingtariff" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingTariff : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25EVChargingTariffDimensionO"></span>` `<span id="//apple_ref/swift/Enum/EVChargingTariffDimension" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk25EVChargingTariffDimensionO" class="token"><code>EVChargingTariffDimension</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the dimension the price component, which determines what is being charged and how:

  - time: Price per unit of time spent charging.
  - energy: Price per unit of energy consumed during charging.
  - flat: One-time fee charged per session.
  - parking time: Price per unit of time not charging but parked at the charger.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evchargingtariffdimension" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVChargingTariffDimension : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23EVChargingTariffElementV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingTariffElement" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk23EVChargingTariffElementV" class="token"><code>EVChargingTariffElement</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a tariff element, which defines how pricing is applied. The associated condition assists the client in selecting the appropriate element for a charging session. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingtariffelement" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingTariffElement : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk32EVChargingTariffElementConditionV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingTariffElementCondition" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk32EVChargingTariffElementConditionV" class="token"><code>EVChargingTariffElementCondition</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Condition that the charging session needs to meet to apply the tariff element. Tariff elements may include conditions that define when they apply:

  - Time of day (e.g., 22:00–06:00)
  - Day of week (e.g., weekends only)

  <div class="aside aside-date">

  Date

  Date range (e.g., seasonal pricing)

  </div>

  - Charging session duration
  - Battery level thresholds (e.g., overstay fees)

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingtariffelementcondition" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingTariffElementCondition : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30EVChargingTariffPriceComponentV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingTariffPriceComponent" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk30EVChargingTariffPriceComponentV" class="token"><code>EVChargingTariffPriceComponent</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the price component of an EV charging tariff. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingtariffpricecomponent" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingTariffPriceComponent : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23EVChargingTariffRequestV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingTariffRequest" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk23EVChargingTariffRequestV" class="token"><code>EVChargingTariffRequest</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a search option to choose the eMSP or CPO whose tariff should be included in the response. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingtariffrequest" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingTariffRequest : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20EVChargingTariffTypeO"></span>` `<span id="//apple_ref/swift/Enum/EVChargingTariffType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk20EVChargingTariffTypeO" class="token"><code>EVChargingTariffType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the tariff pricing model (adhoc, emsp, or cpo). **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evchargingtarifftype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVChargingTariffType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26EVChargingTruckRestrictionV"></span>` `<span id="//apple_ref/swift/Struct/EVChargingTruckRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk26EVChargingTruckRestrictionV" class="token"><code>EVChargingTruckRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents access restrictions for trucks and light commercial vehicles. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evchargingtruckrestriction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVChargingTruckRestriction : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25EVChargingVehicleCategoryO"></span>` `<span id="//apple_ref/swift/Enum/EVChargingVehicleCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk25EVChargingVehicleCategoryO" class="token"><code>EVChargingVehicleCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the category of the vehicle supported at the charging point. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evchargingvehiclecategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVChargingVehicleCategory : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28EVCP3SearchCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/EVCP3SearchCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk28EVCP3SearchCompletionHandlera" class="token"><code>EVCP3SearchCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method that will be called on the main thread when a search operation in <a href="sdk-for-ios-navigate-classes-evsearchengine">`EVSearchEngine`</a> has been completed. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias EVCP3SearchCompletionHandler = ( _ error : EVSearchError ?, _ chargingLocations : [ EVChargingLocation ]?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>The ev search error.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>chargingLocations</code></em><code> </code></td>
  <td><div>
  <p>The ev charging locations.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4EvseV"></span>` `<span id="//apple_ref/swift/Struct/Evse" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk4EvseV" class="token"><code>Evse</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.

  <a href="sdk-for-ios-navigate-structs-evse" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Evse : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVSearchEngineC"></span>` `<span id="//apple_ref/swift/Class/EVSearchEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk14EVSearchEngineC" class="token"><code>EVSearchEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The `EVSearchEngine` API provides detailed information about charging locations. It requires an online connection to execute the requests. A licence is required to use this API. Details can be found in <a href="https://www.here.com/docs/bundle/ev-charge-points-api-v3-developer-guide/page/topics/quick-start-platform.html">HERE EV Charge Points API v3 - Developer Guide</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-evsearchengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class EVSearchEngine : EVSearchInterface
  ```

  ``` highlight
  extension EVSearchEngine: NativeBase
  ```

  ``` highlight
  extension EVSearchEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EVSearchErrorO"></span>` `<span id="//apple_ref/swift/Enum/EVSearchError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13EVSearchErrorO" class="token"><code>EVSearchError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that <a href="sdk-for-ios-navigate-classes-evsearchengine">`EVSearchEngine`</a> may report. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-evsearcherror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVSearchError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVSearchInterfaceP"></span>` `<span id="//apple_ref/swift/Protocol/EVSearchInterface" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk17EVSearchInterfaceP" class="token"><code>EVSearchInterface</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the protocol for the <a href="sdk-for-ios-navigate-classes-evsearchengine">`EVSearchEngine`</a>. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-evsearchinterface" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol EVSearchInterface : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15EVSearchOptionsV"></span>` `<span id="//apple_ref/swift/Struct/EVSearchOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15EVSearchOptionsV" class="token"><code>EVSearchOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Encapsulates additional options that control the behavior of <a href="sdk-for-ios-navigate-classes-evsearchengine">`EVSearchEngine`</a>. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evsearchoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVSearchOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EVSEConnectorV"></span>` `<span id="//apple_ref/swift/Struct/EVSEConnector" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13EVSEConnectorV" class="token"><code>EVSEConnector</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE connector.

  <a href="sdk-for-ios-navigate-structs-evseconnector" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVSEConnector : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8EVSEInfoV"></span>` `<span id="//apple_ref/swift/Struct/EVSEInfo" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk8EVSEInfoV" class="token"><code>EVSEInfo</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents an EVSE at the charging point. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-evseinfo" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EVSEInfo : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10EVSEStatusO"></span>` `<span id="//apple_ref/swift/Enum/EVSEStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk10EVSEStatusO" class="token"><code>EVSEStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVSE status

  <a href="sdk-for-ios-navigate-enums-evsestatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EVSEStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12FacilityTypeO"></span>` `<span id="//apple_ref/swift/Enum/FacilityType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12FacilityTypeO" class="token"><code>FacilityType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents facility type available at the location. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-facilitytype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum FacilityType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12FuelAdditiveV"></span>` `<span id="//apple_ref/swift/Struct/FuelAdditive" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12FuelAdditiveV" class="token"><code>FuelAdditive</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains fuel additive information for generic fuel type.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-fueladditive" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct FuelAdditive : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16FuelAdditiveTypeO"></span>` `<span id="//apple_ref/swift/Enum/FuelAdditiveType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk16FuelAdditiveTypeO" class="token"><code>FuelAdditiveType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines possible fuel additives that a fuel could contain.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-fueladditivetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum FuelAdditiveType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11FuelStationV"></span>` `<span id="//apple_ref/swift/Struct/FuelStation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk11FuelStationV" class="token"><code>FuelStation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains information about a specific fuel station.

  Use <a href="sdk-for-ios-navigate-classes-placecategory#/s:7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ">`PlaceCategory.businessAndServicesPetrolGasolineStation`</a> to find fuel stations. In the <a href="sdk-for-ios-navigate-structs-details">`Details`</a> of a <a href="sdk-for-ios-navigate-classes-place">`Place`</a> result you can find the associated fuel station information, if any.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-fuelstation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct FuelStation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8FuelTypeO"></span>` `<span id="//apple_ref/swift/Enum/FuelType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk8FuelTypeO" class="token"><code>FuelType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines possible fuel types provided by a fuel station.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-fueltype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum FuelType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GenericFuelV"></span>` `<span id="//apple_ref/swift/Struct/GenericFuel" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk11GenericFuelV" class="token"><code>GenericFuel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains generic fuel type info of fuel station.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-genericfuel" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GenericFuel : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8GeoPlaceV"></span>` `<span id="//apple_ref/swift/Struct/GeoPlace" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk8GeoPlaceV" class="token"><code>GeoPlace</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  GeoPlace struct represents a location object: such as a country, a city, a point of interest (POI) etc. It can be used for PersonalPlace creation, in order to provide search on custom places.

  <a href="sdk-for-ios-navigate-structs-geoplace" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoPlace : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13HighlightTypeO"></span>` `<span id="//apple_ref/swift/Enum/HighlightType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13HighlightTypeO" class="token"><code>HighlightType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies members of Suggestion class to which input query can be matched.

  <a href="sdk-for-ios-navigate-enums-highlighttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum HighlightType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10IndexRangeC"></span>` `<span id="//apple_ref/swift/Class/IndexRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk10IndexRangeC" class="token"><code>IndexRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds information to which part of the text, input query was matched. The first character is denoted by a value of 0.

  <a href="sdk-for-ios-navigate-classes-indexrange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class IndexRange
  ```

  ``` highlight
  extension IndexRange: NativeBase
  ```

  ``` highlight
  extension IndexRange: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13LandlinePhoneV"></span>` `<span id="//apple_ref/swift/Struct/LandlinePhone" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13LandlinePhoneV" class="token"><code>LandlinePhone</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents data related to specific landline phone number.

  <a href="sdk-for-ios-navigate-structs-landlinephone" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LandlinePhone : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15LocationDetailsV"></span>` `<span id="//apple_ref/swift/Struct/LocationDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15LocationDetailsV" class="token"><code>LocationDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains geographical info about location

  <a href="sdk-for-ios-navigate-structs-locationdetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocationDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MobilePhoneV"></span>` `<span id="//apple_ref/swift/Struct/MobilePhone" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk11MobilePhoneV" class="token"><code>MobilePhone</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents data related to specific mobile phone number.

  <a href="sdk-for-ios-navigate-structs-mobilephone" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MobilePhone : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MyPlacesC"></span>` `<span id="//apple_ref/swift/Class/MyPlaces" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk8MyPlacesC" class="token"><code>MyPlaces</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides means to populate personal places data source. Also acts as a owner of the collection of personal places. MyPlaces is memory-only object: nothing is persisted and/or sent over the network. Client has full control on how to store personal places.

  <a href="sdk-for-ios-navigate-classes-myplaces" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MyPlaces
  ```

  ``` highlight
  extension MyPlaces: NativeBase
  ```

  ``` highlight
  extension MyPlaces: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19OfflineSearchEngineC"></span>` `<span id="//apple_ref/swift/Class/OfflineSearchEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk19OfflineSearchEngineC" class="token"><code>OfflineSearchEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The OfflineSearchEngine works without internet and unlocks the search and geocoding capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications.

  It provides the same interfaces as the SearchEngine, but the results may slightly differ as the results are taken from already downloaded map data instead of initiating a new request to a HERE backend service. This way the data may be, for example, older compared to the data you may receive when using the SearchEngine. On the other hand, this class provides results faster as no online connection is necessary.

  In comparison to the SearchEngine, there are a few limitations:

  - The IDs of POIs are different and may differ among different map versions.
  - The implementation is different and the resources are limited, so the results can differ.
  - OfflineSearchEngine sometimes doesn’t return the requested number of results.

  Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data. However, cached data may be incomplete, which can result in searches returning partial or incomplete information. Therefore, it is recommended to use persistent map data. Make sure that at least <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">`LayerConfiguration.Feature.offlineSearch`</a> is enabled. For EV rich attributes also enable <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a>, for truck rich attributes also enable <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">`LayerConfiguration.Feature.truckServiceAttributes`</a>, for fuel station rich attributes also enable <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">`LayerConfiguration.Feature.fuelStationAttributes`</a> in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

  <a href="sdk-for-ios-navigate-classes-offlinesearchengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class OfflineSearchEngine : SearchInterface
  ```

  ``` highlight
  extension OfflineSearchEngine: NativeBase
  ```

  ``` highlight
  extension OfflineSearchEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18OfflineSearchIndexC"></span>` `<span id="//apple_ref/swift/Class/OfflineSearchIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk18OfflineSearchIndexC" class="token"><code>OfflineSearchIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-offlinesearchindex" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class OfflineSearchIndex
  ```

  ``` highlight
  extension OfflineSearchIndex: NativeBase
  ```

  ``` highlight
  extension OfflineSearchIndex: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26OfflineSearchIndexListenerP"></span>` `<span id="//apple_ref/swift/Protocol/OfflineSearchIndexListener" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk26OfflineSearchIndexListenerP" class="token"><code>OfflineSearchIndexListener</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol to get updates about progress of creating persistent map index.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-offlinesearchindexlistener" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol OfflineSearchIndexListener : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12OpeningHoursV"></span>` `<span id="//apple_ref/swift/Struct/OpeningHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12OpeningHoursV" class="token"><code>OpeningHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents opening hours information.

  <a href="sdk-for-ios-navigate-structs-openinghours" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct OpeningHours : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11ParkingTypeO"></span>` `<span id="//apple_ref/swift/Enum/ParkingType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk11ParkingTypeO" class="token"><code>ParkingType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents parking type available at the location. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-parkingtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ParkingType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC"></span>` `<span id="//apple_ref/swift/Class/Place" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk5PlaceC" class="token"><code>Place</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a location object, such as a country, a city, a point of interest (POI) etc.

  <a href="sdk-for-ios-navigate-classes-place" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Place
  ```

  ``` highlight
  extension Place: NativeBase
  ```

  ``` highlight
  extension Place: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13PlaceCategoryC"></span>` `<span id="//apple_ref/swift/Class/PlaceCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13PlaceCategoryC" class="token"><code>PlaceCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a category of place with different levels of granularity. This class also defines a set of most commonly used categories.

  <a href="sdk-for-ios-navigate-classes-placecategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PlaceCategory
  ```

  ``` highlight
  extension PlaceCategory: NativeBase
  ```

  ``` highlight
  extension PlaceCategory: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10PlaceChainV"></span>` `<span id="//apple_ref/swift/Struct/PlaceChain" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk10PlaceChainV" class="token"><code>PlaceChain</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parameters related to HERE Places chain system.

  <a href="sdk-for-ios-navigate-structs-placechain" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PlaceChain : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PlaceFilterV"></span>` `<span id="//apple_ref/swift/Struct/PlaceFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk11PlaceFilterV" class="token"><code>PlaceFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The filter options to specify a place. Consists of fuel, truck and EV options.

  <a href="sdk-for-ios-navigate-structs-placefilter" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PlaceFilter : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13PlaceFoodTypeV"></span>` `<span id="//apple_ref/swift/Struct/PlaceFoodType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13PlaceFoodTypeV" class="token"><code>PlaceFoodType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parameters related to HERE Places cuisine system.

  <a href="sdk-for-ios-navigate-structs-placefoodtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PlaceFoodType : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12PlaceIdQueryV"></span>` `<span id="//apple_ref/swift/Struct/PlaceIdQuery" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12PlaceIdQueryV" class="token"><code>PlaceIdQuery</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options to specify a Place id query.

  <a href="sdk-for-ios-navigate-structs-placeidquery" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PlaceIdQuery : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30PlaceIdSearchCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/PlaceIdSearchCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk30PlaceIdSearchCompletionHandlera" class="token"><code>PlaceIdSearchCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a search by id call has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias PlaceIdSearchCompletionHandler = ( _ searchError : SearchError ?, _ place : Place ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>searchError</code></em><code> </code></td>
  <td><div>
  <p>The search error.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>place</code></em><code> </code></td>
  <td><div>
  <p>The place.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/PlaceIdSearchExtendedCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera" class="token"><code>PlaceIdSearchExtendedCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a search by id call has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias PlaceIdSearchExtendedCompletionHandler = ( _ searchError : SearchError ?, _ place : Place ?, _ responseDetails : ResponseDetails ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>searchError</code></em><code> </code></td>
  <td><div>
  <p>The search error.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>place</code></em><code> </code></td>
  <td><div>
  <p>The place.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>responseDetails</code></em><code> </code></td>
  <td><div>
  <p>The response details.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23PlaceSerializationErrorO"></span>` `<span id="//apple_ref/swift/Enum/PlaceSerializationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk23PlaceSerializationErrorO" class="token"><code>PlaceSerializationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents and error, which occurs during place serialization and deserialization routines.

  <a href="sdk-for-ios-navigate-enums-placeserializationerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PlaceSerializationError : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension PlaceSerializationError : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27PlaceSerializationExceptiona"></span>` `<span id="//apple_ref/swift/Alias/PlaceSerializationException" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk27PlaceSerializationExceptiona" class="token"><code>PlaceSerializationException</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Place serialization exception

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias PlaceSerializationException = PlaceSerializationError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9PlaceTypeO"></span>` `<span id="//apple_ref/swift/Enum/PlaceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9PlaceTypeO" class="token"><code>PlaceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies place type of Place result from a search query.

  <a href="sdk-for-ios-navigate-enums-placetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PlaceType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17POIPaymentDetailsV"></span>` `<span id="//apple_ref/swift/Struct/POIPaymentDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk17POIPaymentDetailsV" class="token"><code>POIPaymentDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Details about the payment options at the POI.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-poipaymentdetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct POIPaymentDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16POIPaymentMethodV"></span>` `<span id="//apple_ref/swift/Struct/POIPaymentMethod" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk16POIPaymentMethodV" class="token"><code>POIPaymentMethod</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds constants that represent payment methods.

  See <a href="sdk-for-ios-navigate-structs-poipaymentdetails">`POIPaymentDetails`</a> for usage.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-poipaymentmethod" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct POIPaymentMethod
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15ResponseDetailsV"></span>` `<span id="//apple_ref/swift/Struct/ResponseDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15ResponseDetailsV" class="token"><code>ResponseDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Structure holding various information received with response to a query.

  <a href="sdk-for-ios-navigate-structs-responsedetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ResponseDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15ScheduleDetailsV"></span>` `<span id="//apple_ref/swift/Struct/ScheduleDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15ScheduleDetailsV" class="token"><code>ScheduleDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Encapsulates schedule details complying with the iCalendar specification: <https://tools.ietf.org/html/rfc5545>.

  <a href="sdk-for-ios-navigate-structs-scheduledetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ScheduleDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23SearchCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/SearchCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk23SearchCompletionHandlera" class="token"><code>SearchCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a search call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias SearchCompletionHandler = ( _ searchError : SearchError ?, _ places : [ Place ]?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>searchError</code></em><code> </code></td>
  <td><div>
  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>places</code></em><code> </code></td>
  <td><div>
  <p>The list of search results. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31SearchExtendedCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/SearchExtendedCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk31SearchExtendedCompletionHandlera" class="token"><code>SearchExtendedCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a search call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias SearchExtendedCompletionHandler = ( _ searchError : SearchError ?, _ places : [ Place ]?, _ responseDetails : ResponseDetails ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>searchError</code></em><code> </code></td>
  <td><div>
  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>places</code></em><code> </code></td>
  <td><div>
  <p>The list of search results. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>responseDetails</code></em><code> </code></td>
  <td><div>
  <p>Additional information provided with response. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12SearchEngineC"></span>` `<span id="//apple_ref/swift/Class/SearchEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12SearchEngineC" class="token"><code>SearchEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications. It enables to search for HERE points of interests, forward and reverse geocode addresses and geographic coordinates from the HERE map and search for suggested addresses or place candidates based on incomplete or misspelled queries.

  It also allows to search along a given <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a> set inside a <a href="sdk-for-ios-navigate-structs-geocorridor">`GeoCorridor`</a> as part of a <a href="sdk-for-ios-navigate-structs-textquery">`TextQuery`</a>.

  The SearchEngine API requires an online connection to execute the requests.

  **Note:** All methods are provided in two flavors. One uses a <a href="sdk-for-ios-navigate-search#/s:7heresdk23SearchCompletionHandlera">`SearchCompletionHandler`</a> and the other uses a <a href="sdk-for-ios-navigate-search#/s:7heresdk31SearchExtendedCompletionHandlera">`SearchExtendedCompletionHandler`</a>: The later adds a <a href="sdk-for-ios-navigate-structs-responsedetails">`ResponseDetails`</a> result type that provides the `requestId` of a search request and a `correlationId` to identify multiple, related queries. This may be useful for debug purposes.

  <a href="sdk-for-ios-navigate-classes-searchengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SearchEngine : SearchInterface
  ```

  ``` highlight
  extension SearchEngine: NativeBase
  ```

  ``` highlight
  extension SearchEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11SearchErrorO"></span>` `<span id="//apple_ref/swift/Enum/SearchError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk11SearchErrorO" class="token"><code>SearchError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may result from a search query.

  <a href="sdk-for-ios-navigate-enums-searcherror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum SearchError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15SearchInterfaceP"></span>` `<span id="//apple_ref/swift/Protocol/SearchInterface" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15SearchInterfaceP" class="token"><code>SearchInterface</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the protocol for the online and offline search engines.

  <a href="sdk-for-ios-navigate-protocols-searchinterface" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol SearchInterface : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13SearchOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SearchOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk13SearchOptionsV" class="token"><code>SearchOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Encapsulates options that control the behavior of search and suggest operations.

  <a href="sdk-for-ios-navigate-structs-searchoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SearchOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15StructuredQueryV"></span>` `<span id="//apple_ref/swift/Struct/StructuredQuery" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15StructuredQueryV" class="token"><code>StructuredQuery</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options to specify a structured query. Only supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-structuredquery" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct StructuredQuery : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SuggestionC"></span>` `<span id="//apple_ref/swift/Class/Suggestion" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk10SuggestionC" class="token"><code>Suggestion</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Suggestion is meant to provide relevant suggestions to partial queries, like “restaur”, “starbu”, “eiffel”. Represents a relevant response to user queries. Suggestions (please check <a href="sdk-for-ios-navigate-enums-suggestiontype">`SuggestionType`</a>) are either: Place: <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5placeyA2CmF">`SuggestionType.place`</a> Query: <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5chainyA2CmF">`SuggestionType.chain`</a> or <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">`SuggestionType.category`</a>

  With “Place” you get data for a concrete place in the world. With “Query” something to follow-up, a way to perform more focused search.

  <a href="sdk-for-ios-navigate-classes-suggestion" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Suggestion
  ```

  ``` highlight
  extension Suggestion: NativeBase
  ```

  ``` highlight
  extension Suggestion: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14SuggestionTypeO"></span>` `<span id="//apple_ref/swift/Enum/SuggestionType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk14SuggestionTypeO" class="token"><code>SuggestionType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the type of suggestion returned for query.

  <a href="sdk-for-ios-navigate-enums-suggestiontype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum SuggestionType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24SuggestCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/SuggestCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk24SuggestCompletionHandlera" class="token"><code>SuggestCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a suggest call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias SuggestCompletionHandler = ( _ searchError : SearchError ?, _ suggestions : [ Suggestion ]?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>searchError</code></em><code> </code></td>
  <td><div>
  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>suggestions</code></em><code> </code></td>
  <td><div>
  <p>The list of suggestion results. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk32SuggestExtendedCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/SuggestExtendedCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk32SuggestExtendedCompletionHandlera" class="token"><code>SuggestExtendedCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a suggest call has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time. This API is not supported by offline search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias SuggestExtendedCompletionHandler = ( _ searchError : SearchError ?, _ suggestions : [ Suggestion ]?, _ responseDetails : ResponseDetails ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>searchError</code></em><code> </code></td>
  <td><div>
  <p>An error enum indicating what went wrong. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>suggestions</code></em><code> </code></td>
  <td><div>
  <p>The list of suggestion results. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>responseDetails</code></em><code> </code></td>
  <td><div>
  <p>Additional information provided with response. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17SupplierReferenceV"></span>` `<span id="//apple_ref/swift/Struct/SupplierReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk17SupplierReferenceV" class="token"><code>SupplierReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the place as provided by the supplier

  <a href="sdk-for-ios-navigate-structs-supplierreference" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SupplierReference : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9TextQueryV"></span>` `<span id="//apple_ref/swift/Struct/TextQuery" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9TextQueryV" class="token"><code>TextQuery</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options to specify a text query.

  <a href="sdk-for-ios-navigate-structs-textquery" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TextQuery : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14TimeOfDayRangeV"></span>` `<span id="//apple_ref/swift/Struct/TimeOfDayRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk14TimeOfDayRangeV" class="token"><code>TimeOfDayRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time period when the tariff element is valid, in local time. The time period wraps around to the next day, when end time of the period <a href="sdk-for-ios-navigate-structs-timeofdayrange#/s:7heresdk14TimeOfDayRangeV2toSSvp">`TimeOfDayRange.to`</a> is smaller than the beginning <a href="sdk-for-ios-navigate-structs-timeofdayrange#/s:7heresdk14TimeOfDayRangeV4fromSSvp">`TimeOfDayRange.from`</a>. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-timeofdayrange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TimeOfDayRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14TruckAmenitiesV"></span>` `<span id="//apple_ref/swift/Struct/TruckAmenities" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk14TruckAmenitiesV" class="token"><code>TruckAmenities</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck amenities struct, represents availability (true/false) for each feature, except shower_count - number of showers, if data is available. Note: This is a BETA feature and thus subject to change.

  <a href="sdk-for-ios-navigate-structs-truckamenities" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TruckAmenities : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9TruckFuelV"></span>` `<span id="//apple_ref/swift/Struct/TruckFuel" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9TruckFuelV" class="token"><code>TruckFuel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains truck fuel type info of fuel station. Note: This is a BETA feature and thus subject to change.

  <a href="sdk-for-ios-navigate-structs-truckfuel" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TruckFuel : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10WebDetailsV"></span>` `<span id="//apple_ref/swift/Struct/WebDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk10WebDetailsV" class="token"><code>WebDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains information about images, editorials, rating and a urls to them.

  <a href="sdk-for-ios-navigate-structs-webdetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WebDetails : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12WebEditorialV"></span>` `<span id="//apple_ref/swift/Struct/WebEditorial" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk12WebEditorialV" class="token"><code>WebEditorial</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains information about editorial article and a link to it.

  <a href="sdk-for-ios-navigate-structs-webeditorial" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WebEditorial : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8WebImageV"></span>` `<span id="//apple_ref/swift/Struct/WebImage" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk8WebImageV" class="token"><code>WebImage</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains image information and direct link to it.

  <a href="sdk-for-ios-navigate-structs-webimage" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WebImage : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9WebRatingV"></span>` `<span id="//apple_ref/swift/Struct/WebRating" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9WebRatingV" class="token"><code>WebRating</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains information about rating and a url to review.

  <a href="sdk-for-ios-navigate-structs-webrating" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WebRating : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14WebsiteAddressV"></span>` `<span id="//apple_ref/swift/Struct/WebsiteAddress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk14WebsiteAddressV" class="token"><code>WebsiteAddress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents data related to specific website address

  <a href="sdk-for-ios-navigate-structs-websiteaddress" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WebsiteAddress : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9WebSourceV"></span>` `<span id="//apple_ref/swift/Struct/WebSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9WebSourceV" class="token"><code>WebSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains information about provider of the item and a direct link to the item.

  <a href="sdk-for-ios-navigate-structs-websource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WebSource : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15W3WSearchEngineC"></span>` `<span id="//apple_ref/swift/Class/W3WSearchEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk15W3WSearchEngineC" class="token"><code>W3WSearchEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  what3words is an alternative geocode system designed to identify any location on the planet. The system divides the world into a grid of 57 trillion 3-by-3-metre squares, each of which has a three-word address. For example, the front door of HERE’s Berlin office is identified by “///wage.mere.heap”. `W3WSearchEngine` allows you to convert 3 word addresses to coordinates and also coordinates to 3 word addresses.

  **Note:** Using W3WSearchEngine requires a licence to access HERE what3words APIs.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-w3wsearchengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class W3WSearchEngine
  ```

  ``` highlight
  extension W3WSearchEngine: NativeBase
  ```

  ``` highlight
  extension W3WSearchEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14W3WSearchErrorO"></span>` `<span id="//apple_ref/swift/Enum/W3WSearchError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk14W3WSearchErrorO" class="token"><code>W3WSearchError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may result from a w3w search query.

  <a href="sdk-for-ios-navigate-enums-w3wsearcherror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum W3WSearchError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9W3WSquareV"></span>` `<span id="//apple_ref/swift/Struct/W3WSquare" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk9W3WSquareV" class="token"><code>W3WSquare</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains information about one of the squares in the what3words geocode system.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-w3wsquare" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct W3WSquare : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26W3WSearchCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/W3WSearchCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-search#/s:7heresdk26W3WSearchCompletionHandlera" class="token"><code>W3WSearchCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method that will be called on the main thread when a search operation in <a href="sdk-for-ios-navigate-classes-w3wsearchengine">`W3WSearchEngine`</a> has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias W3WSearchCompletionHandler = ( _ searchError : W3WSearchError ?, _ square : W3WSquare ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>searchError</code></em><code> </code></td>
  <td><div>
  <p>The w3w search error.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>square</code></em><code> </code></td>
  <td><div>
  <p>The w3w square.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

