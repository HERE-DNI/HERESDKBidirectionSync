---
title: "EVChargingLocation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evcharginglocation"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.search.EVChargingLocation →
com.here.NativeBase → com.here.sdk.search.EVChargingLocation

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">EVChargingLocation</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

An electric vehicle (EV) charging location. The semantics generally
follow the OCPI 2.2.1 standard. Known EV-specific acronyms: EV: Electric
Vehicle OCPI: Open Charge Point Interface (a standard with a rather wide
adoption worldwide, https://evroaming.org/) CPO: Charge Point Operator
(company that runs the EV charging location) eMSP: e-Mobility Service
Provider (customer-facing company) EVSE: Electric Vehicle Supply
Equipment (the actual charger that can charge one car at a time) A
charging location includes a collection of one or more EV supply
equipment (EVSE) instances. Typically, the charging location is the
exact location of the group of EVSEs, simplified to a single point, but
it can also be the entrance of a parking structure which contains these
EVSEs. Each EVSE supports more precise position, where applicable. Note:
This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a
deprecation process.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingconnectorgroup"
  title="class in com.here.sdk.search"><code>EVChargingConnectorGroup</code></a><code>&gt;</code></td>
  <td><pre><code>getConnectorGroups()</code></pre></td>
  <td><div class="block">
  Gets the connector groups for the location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getCpoID()</code></pre></td>
  <td><div class="block">
  Gets the CPO's own ID for the location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingoperator"
  title="class in com.here.sdk.search"><code>EVChargingOperator</code></a><code>&gt;</code></td>
  <td><pre><code>getEMobilityServiceProviders()</code></pre></td>
  <td><div class="block">
  Gets the list of eMSPs with a roaming agreement enabling access to the
  EV charging location.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-energymix"
  title="class in com.here.sdk.search"><code>EnergyMix</code></a></td>
  <td><pre><code>getEnergyMix()</code></pre></td>
  <td><div class="block">
  Gets the details on the energy supplied at the charging location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingoperator"
  title="class in com.here.sdk.search"><code>EVChargingOperator</code></a></td>
  <td><pre><code>getEvChargingOperator()</code></pre></td>
  <td><div class="block">
  Gets the operator of the charging point, if available.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingoperator"
  title="class in com.here.sdk.search"><code>EVChargingOperator</code></a></td>
  <td><pre><code>getEvChargingSubOperator()</code></pre></td>
  <td><div class="block">
  Gets the suboperator of the charging point, if available.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-evseinfo"
  title="class in com.here.sdk.search"><code>EVSEInfo</code></a><code>&gt;</code></td>
  <td><pre><code>getEvses()</code></pre></td>
  <td><div class="block">
  Gets the list of EVSEs at the charging station.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-facilitytype"
  title="enum class in com.here.sdk.search"><code>FacilityType</code></a><code>&gt;</code></td>
  <td><pre><code>getFacilityTypes()</code></pre></td>
  <td><div class="block">
  Gets the list of facilities available at the charging location, for
  example hotel, wifi, parking lot etc.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getID()</code></pre></td>
  <td><div class="block">
  Gets the unique identifier of the charging location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getName()</code></pre></td>
  <td><div class="block">
  Gets the display name of the charging location, if available.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingopeninghours"
  title="class in com.here.sdk.search"><code>EVChargingOpeningHours</code></a></td>
  <td><pre><code>getOpeningHours()</code></pre></td>
  <td><div class="block">
  Gets the times when the EVSEs at the charging location can be accessed
  for charging.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-search-parkingtype"
  title="enum class in com.here.sdk.search"><code>ParkingType</code></a></td>
  <td><pre><code>getParkingType()</code></pre></td>
  <td><div class="block">
  Gets the type of parking at the charging location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-evaccessrestrictionreason"
  title="enum class in com.here.sdk.search"><code>EVAccessRestrictionReason</code></a><code>&gt;</code></td>
  <td><pre><code>getRestrictions()</code></pre></td>
  <td><div class="block">
  Gets the list of restrictions.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingvehiclecategory"
  title="enum class in com.here.sdk.search"><code>EVChargingVehicleCategory</code></a><code>&gt;</code></td>
  <td><pre><code>getSupportedVehicles()</code></pre></td>
  <td><div class="block">
  Gets the list of vehicle categories this charging location can support.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getSupportPhoneNumber()</code></pre></td>
  <td><div class="block">
  Gets the phone number that EV drivers should call when need assistance
  at the charge location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingtariff"
  title="class in com.here.sdk.search"><code>EVChargingTariff</code></a><code>&gt;</code></td>
  <td><pre><code>getTariffs()</code></pre></td>
  <td><div class="block">
  Gets the list of tariffs or price plans for the connectors of the
  charging station.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><pre><code>getTimeZone()</code></pre></td>
  <td><div class="block">
  Gets the time zone of the charging location.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-evchargingtruckrestriction"
  title="class in com.here.sdk.search"><code>EVChargingTruckRestriction</code></a></td>
  <td><pre><code>getTruckRestrictions()</code></pre></td>
  <td><div class="block">
  Gets the access restrictions for trucks and light commercial vehicles.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="getID()" class="section detail">

    ### getID

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()

    </div>

    <div class="block">

    Gets the unique identifier of the charging location.

    </div>

    Returns:  
    A unique identifier of the charging location.

    </div>

  - <div id="getName()" class="section detail">

    ### getName

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()

    </div>

    <div class="block">

    Gets the display name of the charging location, if available.

    </div>

    Returns:  
    Display name of the charging location, if available.

    </div>

  - <div id="getCpoID()" class="section detail">

    ### getCpoID

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getCpoID</span>()

    </div>

    <div class="block">

    Gets the CPO's own ID for the location. This ID may be relevant for
    some clients to map the charging location data to their own or 3rd
    party systems. Available only if
    EVChargingLocationFeature.LOCATION_INFO is included in
    EVSearchOptions.additional_features , otherwise null .

    </div>

    Returns:  
    CPO's own ID for the location.

    </div>

  - <div id="getEvChargingOperator()" class="section detail">

    ### getEvChargingOperator

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingOperator](sdk-for-android-explore-com-here-sdk-search-evchargingoperator "class in com.here.sdk.search")</span> <span class="element-name">getEvChargingOperator</span>()

    </div>

    <div class="block">

    Gets the operator of the charging point, if available.

    </div>

    Returns:  
    Operator of the charging point, if available.

    </div>

  - <div id="getEvChargingSubOperator()" class="section detail">

    ### getEvChargingSubOperator

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingOperator](sdk-for-android-explore-com-here-sdk-search-evchargingoperator "class in com.here.sdk.search")</span> <span class="element-name">getEvChargingSubOperator</span>()

    </div>

    <div class="block">

    Gets the suboperator of the charging point, if available.

    </div>

    Returns:  
    Suboperator of the charging point, if available.

    </div>

  - <div id="getEMobilityServiceProviders()" class="section detail">

    ### getEMobilityServiceProviders

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[EVChargingOperator](sdk-for-android-explore-com-here-sdk-search-evchargingoperator "class in com.here.sdk.search")></span> <span class="element-name">getEMobilityServiceProviders</span>()

    </div>

    <div class="block">

    Gets the list of eMSPs with a roaming agreement enabling access to
    the EV charging location. Available only if
    EVChargingLocationFeature.EMSPS is included in
    EVSearchOptions.additional_features , otherwise empty.

    </div>

    Returns:  
    eMSPs with a roaming agreement enabling access to the EV charging
    location.

    </div>

  - <div id="getFacilityTypes()" class="section detail">

    ### getFacilityTypes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[FacilityType](sdk-for-android-explore-com-here-sdk-search-facilitytype "enum class in com.here.sdk.search")></span> <span class="element-name">getFacilityTypes</span>()

    </div>

    <div class="block">

    Gets the list of facilities available at the charging location, for
    example hotel, wifi, parking lot etc. Available only if
    EVChargingLocationFeature.NEARBY is included in
    EVSearchOptions.additional_features , otherwise empty.

    </div>

    Returns:  
    Facilities available at the charging location, for example hotel,
    wifi, parking lot etc.

    </div>

  - <div id="getParkingType()" class="section detail">

    ### getParkingType

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[ParkingType](sdk-for-android-explore-com-here-sdk-search-parkingtype "enum class in com.here.sdk.search")</span> <span class="element-name">getParkingType</span>()

    </div>

    <div class="block">

    Gets the type of parking at the charging location. Available only if
    EVChargingLocationFeature.LOCATION_INFO is included in
    EVSearchOptions.additional_features , otherwise null .

    </div>

    Returns:  
    The type of parking at the charging location.

    </div>

  - <div id="getEnergyMix()" class="section detail">

    ### getEnergyMix

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EnergyMix](sdk-for-android-explore-com-here-sdk-search-energymix "class in com.here.sdk.search")</span> <span class="element-name">getEnergyMix</span>()

    </div>

    <div class="block">

    Gets the details on the energy supplied at the charging location.

    </div>

    Returns:  
    Details on the energy supplied at the charging location. Available
    only if `EVChargingLocationFeature.LOCATION_INFO` is included in
    `EVSearchOptions.additional_features`, otherwise `null`.

    </div>

  - <div id="getEvses()" class="section detail">

    ### getEvses

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[EVSEInfo](sdk-for-android-explore-com-here-sdk-search-evseinfo "class in com.here.sdk.search")></span> <span class="element-name">getEvses</span>()

    </div>

    <div class="block">

    Gets the list of EVSEs at the charging station. Available only if
    EVChargingLocationFeature.EVSES is included in
    EVSearchOptions.additional_features , otherwise empty.

    </div>

    Returns:  
    List of EVSEs at the charging station.

    </div>

  - <div id="getTariffs()" class="section detail">

    ### getTariffs

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[EVChargingTariff](sdk-for-android-explore-com-here-sdk-search-evchargingtariff "class in com.here.sdk.search")></span> <span class="element-name">getTariffs</span>()

    </div>

    <div class="block">

    Gets the list of tariffs or price plans for the connectors of the
    charging station. Tariffs are typically connector-type specific.
    Hence, they are always linked with connectors and/or connector
    groups, by indexes to this list. This property is set only when data
    is available and when EVSearchOptions.additional_features include
    either EVChargingLocationFeature.EVSES or
    EVChargingLocationFeature.CONNECTOR_GROUPS . By default, the list
    includes tariffs for ad-hoc charging, per connector type, for EVSEs
    that accept payment without registering.

    </div>

    Returns:  
    List of tariffs or price plans for the connectors of the charging
    station.

    </div>

  - <div id="getConnectorGroups()" class="section detail">

    ### getConnectorGroups

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[EVChargingConnectorGroup](sdk-for-android-explore-com-here-sdk-search-evchargingconnectorgroup "class in com.here.sdk.search")></span> <span class="element-name">getConnectorGroups</span>()

    </div>

    <div class="block">

    Gets the connector groups for the location. Provides an overview of
    the charging connectors in the location by type and power. Available
    only if EVChargingLocationFeature.CONNECTOR_GROUPS is included in
    EVSearchOptions.additional_features , otherwise empty.

    </div>

    Returns:  
    Connector groups for the location.

    </div>

  - <div id="getSupportedVehicles()" class="section detail">

    ### getSupportedVehicles

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[EVChargingVehicleCategory](sdk-for-android-explore-com-here-sdk-search-evchargingvehiclecategory "enum class in com.here.sdk.search")></span> <span class="element-name">getSupportedVehicles</span>()

    </div>

    <div class="block">

    Gets the list of vehicle categories this charging location can
    support. For example, the same location can be suitable for charging
    passenger cars and motorcycles. There may be some further
    restrictions specified in other attributes, for example the
    available connector types may not be suitable for all vehicles in
    the supported category.

    </div>

    Returns:  
    List of vehicle categories this charging location can support. For
    example, the same location can be suitable for charging passenger
    cars and motorcycles.

    </div>

  - <div id="getTruckRestrictions()" class="section detail">

    ### getTruckRestrictions

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingTruckRestriction](sdk-for-android-explore-com-here-sdk-search-evchargingtruckrestriction "class in com.here.sdk.search")</span> <span class="element-name">getTruckRestrictions</span>()

    </div>

    <div class="block">

    Gets the access restrictions for trucks and light commercial
    vehicles. Restricted, only available to customers having a specific
    contract with HERE and if requested by including
    EVChargingLocationFeature.TRUCK_RESTRICTIONS in
    EVSearchOptions.additional_features , otherwise null .

    </div>

    Returns:  
    Access restrictions for trucks and light commercial vehicles.

    </div>

  - <div id="getOpeningHours()" class="section detail">

    ### getOpeningHours

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[EVChargingOpeningHours](sdk-for-android-explore-com-here-sdk-search-evchargingopeninghours "class in com.here.sdk.search")</span> <span class="element-name">getOpeningHours</span>()

    </div>

    <div class="block">

    Gets the times when the EVSEs at the charging location can be
    accessed for charging. Available only if
    EVChargingLocationFeature.LOCATION_INFO is included in
    EVSearchOptions.additional_features , otherwise null .

    </div>

    Returns:  
    The times when the EVSEs at the charging location can be accessed
    for charging.

    </div>

  - <div id="getRestrictions()" class="section detail">

    ### getRestrictions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[EVAccessRestrictionReason](sdk-for-android-explore-com-here-sdk-search-evaccessrestrictionreason "enum class in com.here.sdk.search")></span> <span class="element-name">getRestrictions</span>()

    </div>

    <div class="block">

    Gets the list of restrictions.

    </div>

    Returns:  
    Reason(s) for restricted access.

    </div>

  - <div id="getSupportPhoneNumber()" class="section detail">

    ### getSupportPhoneNumber

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getSupportPhoneNumber</span>()

    </div>

    <div class="block">

    Gets the phone number that EV drivers should call when need
    assistance at the charge location. Available only if
    EVChargingLocationFeature.LOCATION_INFO is included in
    EVSearchOptions.additional_features , otherwise null .

    </div>

    Returns:  
    The phone number that EV drivers should call when need assistance at
    the charge location, in E.164 format.

    </div>

  - <div id="getTimeZone()" class="section detail">

    ### getTimeZone

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getTimeZone</span>()

    </div>

    <div class="block">

    Gets the time zone of the charging location. Based on IANA tzdata's
    TZ-values. Available only if EVChargingLocationFeature.LOCATION_INFO
    is included in EVSearchOptions.additional_features , otherwise null
    .

    </div>

    Returns:  
    The time zone of the charging location. Based on IANA tzdata's
    TZ-values.

    </div>

  </div>

</div>

